import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def display_compaign_topics():
    time_series_df = st.session_state['time_series_df']

    tab1, tab2 = st.tabs("Time Series", "Topics")
    with tab1:
        st.subheader('Time Series')

        all_topics = ['All'] + list(time_series_df['Name'].unique())
        selected_topic = st.selectbox('Select a topic:', all_topics)

        columns = ['VIEWABLE_ATTENTION_EVENTS', 'AVG_VIEWABLE_ATTENTION_TIME', 'CTR', 'COUNT']
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

    with tab2:
        topics_df = st.session_state['topics_df']
        st.subheader('Time Series')

        all_topics = ['All'] + list(topics_df['Name'].unique())
        selected_topic = st.selectbox('Select a topic:', all_topics)

        columns = ['VIEWABLE_ATTENTION_EVENTS', 'AVG_VIEWABLE_ATTENTION_TIME', 'CTR', 'COUNT']
        selected_column = st.selectbox('Select a column to visualize:', columns)

        # Filter the dataframe based on the selected product
        if selected_topic == 'All':
            filtered_df = topics_df
        else:
            filtered_df = topics_df[topics_df['Name'] == selected_topic]

        # Plot the price time series
        fig, ax = plt.subplots(figsize=(10, 6))

        if selected_topic == 'All':
            # If 'All' is selected, plot all products in the same graph with hover tooltips
            fig = px.line(time_series_df, x='Topic', y=selected_column, title="AVERAGE "
                                                                                           f"{selected_column} for "
                                                                                           f"All Topics",
                          labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})
        else:
            # If a specific product is selected, plot only that product
            filtered_df = filtered_df.sort_values(by = selected_column)
            fig = px.line(filtered_df, x='Topic', y=selected_column, title=f"AVERAGE {selected_column} "
                                                                         f"for topic"
                                                                         f" {selected_topic}",
                          labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})

        # Update layout to remove the legend (optional)
        fig.update_layout(showlegend=False)

        # Display the plot
        st.plotly_chart(fig)

