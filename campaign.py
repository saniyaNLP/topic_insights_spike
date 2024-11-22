import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import ast
import pickle
import os

def display_compaign_topics():
    st.title("Topic insights for campaign id: 17074")
    df = pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike/iab_index_values.csv")
    df = df.sort_values(by = ['Topic']).reset_index(drop=True)
    st.dataframe(df)

    time_series_df = pd.read_csv("s3://gumgum-research-sx/sn-models/category_entry_points/niche_anomaly/adam_spike"
                                 "/avg_attention_time_series.csv")
    st.subheader('AVERAGE VIEWABLE_ATTENTION_EVENTS Time Series')

    all_topics = ['All'] + list(time_series_df['Name'].unique())
    selected_topic = st.selectbox('Select a topic:', all_topics)

    columns = ['VIEWABLE_ATTENTION_EVENTS', 'AVG_VIEWABLE_ATTENTION_TIME', 'CTR']
    selected_column = st.selectbox('Select a column to visualize:', columns)

    # Filter the dataframe based on the selected product
    if selected_topic == 'All':
        filtered_df = time_series_df
    else:
        filtered_df = time_series_df[time_series_df['Name'] == selected_topic]

    # Plot the price time series
    fig, ax = plt.subplots(figsize=(10, 6))

    if selected_topic == 'All':
        # If 'All' is selected, plot all products in the same graph with hover tooltips
        fig = px.line(time_series_df, x='DAY', y=selected_column, color='Topic', title="AVERAGE "
                                                                                    f"{selected_column} for "
                                                                                       f"All Topics",
                      labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})
    else:
        # If a specific product is selected, plot only that product
        fig = px.line(filtered_df, x='DAY', y=selected_column, title=f"AVERAGE {selected_column} "
                                                                               f"for topic"
                                                              f" {selected_topic}",
                      labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})

    # Update layout to remove the legend (optional)
    fig.update_layout(showlegend=False)

    # Display the plot
    st.plotly_chart(fig)