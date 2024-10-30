import streamlit as st
from oura_ring import OuraClient
import datetime
OURA_ACCESS_TOKEN=st.secrets["OURA_ACCESS_TOKEN"]
client = OuraClient(OURA_ACCESS_TOKEN)
date_today = datetime.datetime.today().strftime('%Y-%m-%d')
st.write(date_today)
try:
    tot_sleep_all=client.get_daily_sleep(date_today)
    tot_sleep=tot_sleep_all[0]['contributors']['total_sleep']
    st.write(tot_sleep)
except:
    st.write("--")

a=1
