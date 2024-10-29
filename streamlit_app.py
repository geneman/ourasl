import streamlit as st
OURA_ACCESS_TOKEN=st.secrets["OURA_ACCESS_TOKEN"]
client = OuraClient(OURA_ACCESS_TOKEN)

print(client.get_sleep_periods('2024-10-22'))