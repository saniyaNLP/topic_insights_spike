import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from graphs import plot_graphs

def display_compaign_topics():
    if "topics_df" not in st.session_state.keys():
        df =pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike/iab_index_values.csv")
        st.session_state['topics_df'] = df

    if "time_series_df" not in st.session_state.keys():
        df =pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike/avg_attention_time_series.csv")
        st.session_state['time_series_df'] = df

    st.header("Campaign id: 17074")
    st.header("Campaign name: Advertising for TV show Secret Lives of Mormon Wives")

    st.session_state['topics_df'] = st.session_state['topics_df'].sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(st.session_state['topics_df'])
    plot_graphs()

