"""
Chem-Sports Theme for Streamlit.
Transforms the app into a high-energy Chemistry Stadium / Sports Arena aesthetic.
"""

import streamlit as st

CHEM_SPORTS_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&family=Teko:wght@500;700&display=swap');

/* ---------- Page background: Stadium Night Turf Pattern ---------- */
.stApp {
    background-color: #0b1329;
    background-image: 
        radial-gradient(circle at 50% 20%, rgba(34, 197, 94, 0.12) 0%, transparent 50%),
        linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9));
}

/* ---------- Top Stadium Banner / Header ---------- */
[data-testid="stHeader"] {
    background: linear-gradient(90deg, #1e293b, #0f172a);
    border-bottom: 4px solid #22c55e;
    box-shadow: 0 4px 20px rgba(34, 197, 94, 0.3);
}

/* ---------- Main Content Arena Panel ---------- */
.block-container {
    background: rgba(30, 41, 59, 0.85);
    border: 2px solid #334155;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(10px);
    padding: 2.5rem !important;
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
}

/* ---------- Typography ---------- */
.stApp p, .stApp label, .stApp li, .stApp input, .stApp textarea,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 1rem;
    color: #e2e8f0;
}

h1, h2, h3, h4, .main-title, .section-title {
    font-family: 'Teko', sans-serif !important;
    letter-spacing: 1px;
    text-transform: uppercase;
}

h1 { font-size: 2.5rem !important; color: #4ade80 !important; text-shadow: 0 2px 10px rgba(74, 222, 128, 0.3); }
h2 { font-size: 2rem !important; color: #38bdf8 !important; }
h3 { font-size: 1.5rem !important; color: #facc15 !important; }
h4 {
