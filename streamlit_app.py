import csv
import urllib.request

import streamlit as st

st.set_page_config(page_title="Fixed Ops Pulse", page_icon="🍑", layout="centered")

CHEVY_BLUE = "#0B74C5"
PEACH = "#E2572B"
PEACH_DARK = "#C9471F"
GOLD = "#C89B4B"
DEEP_NAVY = "#0A2A7B"

# Public KPI feed: "Fixed Ops Pulse KPIs (feed)" sheet, KPIs tab.
# The 4:30 AM Service Daily Tracking run refreshes these values daily.
FEED_ID = "1uQRnUVYCn5Q4HgnRHbPoz3pu4A0x8cl-H_sKTRs_UD8"
FEED_GID = "1331581290"
FEED_URL = f"https://docs.google.com/spreadsheets/d/{FEED_ID}/export?format=csv&gid={FEED_GID}"

KPI_ORDER = ["CSI", "MTD Labor Gross", "Tracking Gross", "Shop Efficiency", "Unapplied Labor"]


@st.cache_data(ttl=900)
def load_kpis():
    with urllib.request.urlopen(FEED_URL, timeout=20) as r:
        rows = list(csv.reader(r.read().decode("utf-8").splitlines()))
    kpis = {}
    for row in rows[1:]:
        if not row:
            continue
        metric = row[0].strip()
        value = row[1].strip() if len(row) > 1 else ""
        updated = row[2].strip() if len(row) > 2 else ""
        if metric:
            kpis[metric] = (value, updated)
    return kpis


def tidy(value):
    """Display cleanup: 87.50% -> 87.5%. Dollar values untouched."""
    if value.endswith("%"):
        num = value[:-1]
        if "." in num:
            num = num.rstrip("0").rstrip(".")
        return num + "%"
    return value


st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(180deg, #F4F8FD 0%, #FFF6EF 100%);
    }}
    .hero {{
        background: linear-gradient(135deg, #0A2A7B 0%, #0B74C5 100%);
        border-radius: 18px;
        padding: 2.2rem 1.5rem 1.8rem;
        text-align: center;
        color: white;
        border-bottom: 6px solid {PEACH};
        box-shadow: 0 8px 24px rgba(10, 42, 123, 0.28);
        margin-bottom: 1.6rem;
    }}
    .hero h1 {{
        color: white !important;
        font-weight: 800;
        margin: 0.3rem 0 0.5rem;
        font-size: 1.9rem;
        letter-spacing: 0.5px;
    }}
    .hero p {{
        color: #DCE9F7;
        margin: 0;
        font-size: 1.02rem;
    }}
    .hero .peach {{
        font-size: 2.4rem;
        line-height: 1;
    }}
    .hero .gold-rule {{
        width: 64px;
        height: 3px;
        background: {GOLD};
        border-radius: 2px;
        margin: 0.9rem auto 0;
    }}
    .kpi-strip {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 0.4rem;
    }}
    .kpi-card {{
        flex: 1 1 130px;
        background: #FFFFFF;
        border-radius: 12px;
        border-left: 5px solid {PEACH};
        box-shadow: 0 2px 10px rgba(10, 42, 123, 0.08);
        padding: 0.65rem 0.8rem;
    }}
    .kpi-label {{
        font-size: 0.7rem;
        color: #8A8A8A;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-weight: 600;
    }}
    .kpi-value {{
        font-size: 1.3rem;
        color: {DEEP_NAVY};
        font-weight: 800;
        margin-top: 0.15rem;
    }}
    .kpi-updated {{
        text-align: center;
        color: #9A9A9A;
        font-size: 0.78rem;
        margin-bottom: 1.2rem;
    }}
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background: #FFFFFF;
        border-radius: 14px;
        border-left: 5px solid {PEACH} !important;
        box-shadow: 0 2px 10px rgba(10, 42, 123, 0.08);
    }}
    div[data-testid="stVerticalBlockBorderWrapper"] h3 {{
        color: {DEEP_NAVY};
        font-weight: 700;
    }}
    .stLinkButton a {{
        background: {PEACH} !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
    }}
    .stLinkButton a:hover {{
        background: {PEACH_DARK} !important;
        color: white !important;
    }}
    .coming-soon {{
        text-align: center;
        color: #9A9A9A;
        font-size: 0.88rem;
        margin-top: 1.2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="peach">🍑</div>
        <h1>Burns Chevrolet Fixed Ops Pulse</h1>
        <p>Fixed Ops, fresh from the Peach Capital — pick a report below.</p>
        <div class="gold-rule"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Executive KPI strip (reads the public feed sheet; never the Master workbook).
try:
    kpis = load_kpis()
except Exception:
    kpis = {}

cards = [(m, kpis[m]) for m in KPI_ORDER if m in kpis and kpis[m][0]]
if cards:
    html = '<div class="kpi-strip">'
    for metric, (value, _updated) in cards:
        html += (
            '<div class="kpi-card">'
            f'<div class="kpi-label">{metric}</div>'
            f'<div class="kpi-value">{tidy(value)}</div>'
            "</div>"
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)
    updated = next((u for _m, (_v, u) in cards if u), "")
    if updated:
        try:
            y, mo, d = updated.split("-")
            stamp = f"{int(mo)}/{int(d)}/{y}"
        except Exception:
            stamp = updated
        st.markdown(f'<div class="kpi-updated">Numbers as of {stamp}</div>', unsafe_allow_html=True)

APPS = [
    (
        "📊 Executive Pulse",
        "Daily service performance: sales, production, CSI, BDC, labor ops.",
        "https://burnschevroletofgaffneyservice-vipyms3xywhkigqrwqqvcx.streamlit.app/",
    ),
    (
        "🔍 RO Audit",
        "Daily customer-pay RO audit with inspection videos, labeled by RO.",
        "https://burnschevroletroaudit-nrgdfuwkgrtkegci8arhpy.streamlit.app/",
    ),
    (
        "🛠️ Dispatch",
        "Shop dispatch board for technicians and advisors.",
        "https://burns-chevy-gaffney-service-dispatch-semhvpgvchbys2hijj5tmr.streamlit.app/",
    ),
    (
        "🔧 Tech Pulse",
        "Technician view: your videos, MPVIs, and efficiency.",
        "https://tech-pulse-gaffney.streamlit.app/",
    ),
]

for name, desc, url in APPS:
    with st.container(border=True):
        st.subheader(name)
        st.caption(desc)
        st.link_button(f"Open {name.split(' ', 1)[1]} →", url, use_container_width=True)

st.markdown(
    '<div class="coming-soon">Coming soon: Advisor Performance Pulse &middot; Parts Metrics</div>',
    unsafe_allow_html=True,
)
