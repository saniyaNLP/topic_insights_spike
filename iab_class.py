import streamlit as st
import pandas as pd
from graphs import plot_graphs
import boto3
import plotly.express as px


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

    selected_overall_df = st.session_state['overall_results'][st.session_state['overall_results'][
                                                          'iab_cat']==selected_cat].copy()

    selected_overall_df = selected_overall_df.sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(selected_overall_df)

    selected_time_series = st.session_state['time_series_results'][st.session_state['time_series_results'][
                                                          'iab_cat']==selected_cat].copy()
    sorting_columns = ['VIEWABLE_ATTENTION_EVENTS', 'AVG_VIEWABLE_ATTENTION_TIME', 'CTR', 'COUNT']
    selected_column = st.selectbox('Select a column to visualize:', sorting_columns, key='sort_column')
    sorted_df = selected_overall_df.sort_values(by=selected_column, ascending=False).reset_index(drop=True).head(10)
    fig = px.scatter(sorted_df, x='Name', y=selected_column, title="AVERAGE "
                                                                     f"{selected_column} for "
                                                                     f"All Topics",
                     labels={selected_column: f'AVG {selected_column}', 'Name': 'Topic ID'})

    fig.update_layout(
        width=1200,  # Increase the width to spread out the plot
        height=600,  # Adjust height for better aspect ratio
        xaxis_title='Topic ID',
        yaxis_title=f'AVG {selected_column}',
        xaxis=dict(
            tickangle=45,  # Rotate x-axis labels to 45 degrees
            tickmode='array',
            tickvals=sorted_df['Name'],  # Set the tick values to match your data points
        ),
        showlegend=False  # Disable legend if not needed
    )
    st.plotly_chart(fig)
