import streamlit as st
import pandas as pd
from graphs import plot_graphs
import boto3

def display_iab_topics():
    if "overall_results" not in st.session_state.keys():
        df = pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike/per_iab"
               "/overall_scores.csv")
        st.session_state['overall_results'] = df
    if "time_series_results" not in st.session_state.keys():
        df = pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike/per_iab"
               "/time_series_scores.csv")
        st.session_state['time_series_results'] = df
    iabv3_classes = list(st.session_state['overall_results']['iab_cat'].unique())
    selected_cat = st.selectbox('Select an IAB cat:', iabv3_classes,  key ='iab_cat')

    st.title("Topic insights for campaign id: 17074 per IAB category")

    selected_df = st.session_state['overall_results'][st.session_state['overall_results'][
                                                          'iab_cat']==selected_cat].copy()

    selected_df = selected_df.sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(selected_df)
