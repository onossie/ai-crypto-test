import streamlit as st
from bitvavo import Bitvavo
import pandas as pd

# API-keys uit secrets
API_KEY = st.secrets["bitvavo"]["apiKey"]
API_SECRET = st.secrets["bitvavo"]["apiSecret"]

# Initialiseer Bitvavo client
bitvavo = Bitvavo({
    'APIKEY': API_KEY,
    'APISECRET': API_SECRET
})

st.title("🤖 Crypto AI Trader - v0.1")

# Toon beschikbare markten
markets = bitvavo.markets({})
symbols = [m['market'] for m in markets]
selected = st.selectbox("Kies een markt", symbols)

if st.button("Toon huidige prijs"):
    ticker = bitvavo.tickerPrice({'market': selected})
    st.metric(label=f"Huidige prijs ({selected})", value=f"{ticker['price']} EUR")

# Placeholder voor reinforcement learning agent
st.subheader("AI Trading Agent (Coming Soon 🚧)")
st.info("Zelflerend model en backtesting worden momenteel geïntegreerd.")