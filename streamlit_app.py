import streamlit as st
from oura_ring import OuraClient
OURA_ACCESS_TOKEN=st.secrets["OURA_ACCESS_TOKEN"]
client = OuraClient(OURA_ACCESS_TOKEN)
tot_sleep_all=client.get_daily_sleep()
tot_sleep=tot_sleep_all[0]['contributors']['total_sleep']
st.write(tot_sleep)