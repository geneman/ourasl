import streamlit as st
from oura_ring import OuraClient
OURA_ACCESS_TOKEN=st.secrets["OURA_ACCESS_TOKEN"]
client = OuraClient(OURA_ACCESS_TOKEN)

print(client.get_sleep_periods('2024-10-22'))