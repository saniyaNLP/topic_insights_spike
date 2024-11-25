import streamlit as st
import pickle
from campaign import display_compaign_topics
from iab_class import display_iab_topics


st.set_page_config(
    page_title="Topic Insights",
    page_icon="👁️‍🗨️",
)


tab1, tab2 = st.tabs(["Campaign", "IAB Cats" ])

with tab1:
    display_compaign_topics()

with tab2:
    display_iab_topics()
