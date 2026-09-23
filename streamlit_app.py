import streamlit as st

st.set_page_config(page_title="Fixed Ops Pulse", page_icon="🍑", layout="centered")

CHEVY_BLUE = "#0B74C5"
DEEP_NAVY = "#0A2A7B"
PEACH = "#E2572B"
PEACH_DARK = "#C9471F"
GOLD = "#C89B4B"

st.markdown(
    f"""
<style>
.stApp {{
    background: linear-gradient(180deg, #F4F8FD 0%, #FFF6EF 100%);
}}
.hero {{
    background: linear-gradient(135deg, {DEEP_NAVY} 0%, {CHEVY_BLUE} 100%);
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
    (
        "💼 Advisor Performance Pulse",
        "Advisor scorecard: CSI, check-in media, performance vs target, WIP.",
        "https://burnschevroletadvisorpulse-md8vqh6nemazls42ngqbkn.streamlit.app/",
    ),
]

for name, desc, url in APPS:
    with st.container(border=True):
        st.subheader(name)
        st.caption(desc)
        st.link_button(f"Open {name.split(' ', 1)[1]} →", url, use_container_width=True)

st.markdown(
    '<div class="coming-soon">Coming soon: Parts Metrics</div>',
    unsafe_allow_html=True,
)
