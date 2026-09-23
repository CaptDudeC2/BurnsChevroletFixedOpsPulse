import streamlit as st

st.set_page_config(page_title="Fixed Ops Pulse", layout="centered")

st.title("Burns Chevrolet Fixed Ops Pulse")
st.caption("Service operations at a glance — pick a report below.")

APPS = [
    (
        "Executive Pulse",
        "Daily service performance: sales, production, CSI, BDC, labor ops.",
        "https://burnschevroletofgaffneyservice-vipyms3xywhkigqrwqqvcx.streamlit.app/",
    ),
    (
        "RO Audit",
        "Daily customer-pay RO audit with inspection videos, labeled by RO.",
        "https://burnschevroletroaudit-nrgdfuwkgrtkegci8arhpy.streamlit.app/",
    ),
    (
        "Dispatch",
        "Shop dispatch board for technicians and advisors.",
        "https://burns-chevy-gaffney-service-dispatch-semhvpgvchbys2hijj5tmr.streamlit.app/",
    ),
    (
        "Tech Pulse",
        "Technician view: your videos, MPVIs, and efficiency.",
        "https://tech-pulse-gaffney.streamlit.app/",
    ),
]

for name, desc, url in APPS:
    with st.container(border=True):
        st.subheader(name)
        st.caption(desc)
        st.link_button(f"Open {name}", url, use_container_width=True)

st.divider()
st.caption("Coming soon: Advisor Performance Pulse · Parts Metrics")
