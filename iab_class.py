import streamlit as st
import pandas as pd
from graphs import plot_graphs
import boto3
import pickle

s3 = boto3.resource('s3')
bucket = 'gumgum-research-sx'
def display_iab_topics():
    key = 'sn-models/category_entry_points/niche_anomaly/adam_spike/per_iab/overall_results.pkl'
    if "overall_results" not in st.session_state.keys():
        overall_results = pickle.loads(s3.Bucket(bucket).Object(key).get()['Body'].read())
        st.session_state['overall_results'] = overall_results
    iabv3_classes = list(st.session_state['overall_results'].keys())
    selected_cat = st.selectbox('Select an IAB cat:', iabv3_classes)

    st.title("Topic insights for campaign id: 17074 per IAB category")

    selected_df = st.session_state['overall_results'][selected_cat]

    selected_df = selected_df.sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(selected_df)
    plot_graphs()
