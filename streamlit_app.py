import streamlit as st
import base64
import pathlib

st.set_page_config(
    page_title="eTMF AI QC Dashboard",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Nuke every Streamlit chrome element ──────────────────────────────────────
st.markdown("""
<style>
  #MainMenu, header, footer,
  [data-testid="stToolbar"],
  [data-testid="stDecoration"],
  [data-testid="stStatusWidget"],
  section[data-testid="stSidebar"] { display: none !important; }

  /* Zero out every wrapper so the iframe is truly edge-to-edge */
  html, body,
  .stApp,
  [data-testid="stAppViewContainer"],
  [data-testid="stVerticalBlock"],
  .block-container,
  .main,
  .css-1d391kg,        /* older Streamlit builds */
  .css-18e3th9 {
      margin: 0 !important;
      padding: 0 !important;
      max-width: 100% !important;
      width: 100% !important;
  }
  iframe { border: none !important; display: block !important; }
</style>
""", unsafe_allow_html=True)

# ── Read HTML and inject it via a full-viewport iframe using a data URI ──────
html_bytes = pathlib.Path("index.html").read_bytes()
b64 = base64.b64encode(html_bytes).decode("utf-8")
data_uri = f"data:text/html;base64,{b64}"

# The outer div + iframe fill 100 vh with no scrollbar on the Streamlit layer
st.markdown(f"""
<div style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;margin:0;padding:0;">
  <iframe
    src="{data_uri}"
    style="width:100%;height:100%;border:none;display:block;"
    allow="fullscreen"
  ></iframe>
</div>
""", unsafe_allow_html=True)
