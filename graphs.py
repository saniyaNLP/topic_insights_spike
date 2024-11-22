import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


def plot_graphs():
    time_series_df = st.session_state['time_series_df']
    columns = ['VIEWABLE_ATTENTION_EVENTS', 'AVG_VIEWABLE_ATTENTION_TIME', 'CTR', 'COUNT']

    tab1, tab2 = st.tabs(["Time Series", "Topics"])
    with tab1:
        st.write("trial")
        st.subheader('Time Series')

        all_topics = ['All'] + list(time_series_df['Name'].unique())
        selected_topic = st.selectbox('Select a topic:', all_topics)


        selected_column = st.selectbox('Select a column to visualize:', columns)

        # Filter the dataframe based on the selected product
        if selected_topic == 'All':
            filtered_df = time_series_df
        else:
            filtered_df = time_series_df[time_series_df['Name'] == selected_topic]

        fig, ax = plt.subplots(figsize=(10, 6))

        if selected_topic == 'All':
            fig = px.line(time_series_df, x='DAY', y=selected_column, color='Topic', title="AVERAGE "
                                                                                        f"{selected_column} for "
                                                                                           f"All Topics",
                          labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})
        else:
            fig = px.line(filtered_df, x='DAY', y=selected_column, title=f"AVERAGE {selected_column} "
                                                                                   f"for topic"
                                                                  f" {selected_topic}",
                          labels={selected_column: f'AVG {selected_column}', 'DAY': 'Date'})

        fig.update_layout(showlegend=False)

        st.plotly_chart(fig)

    with tab2:
        topics_df = st.session_state['topics_df']
        st.subheader('Time Series')

        selected_column_2 = st.selectbox('Select a column to visualize:', columns, key ='topics')
        sorted_df = topics_df.sort_values(by = selected_column_2, ascending=False).reset_index(drop=True).head(10)
        fig, ax = plt.subplots(figsize=(10, 6))
        fig = px.scatter(sorted_df, x='Name', y=selected_column_2, title="AVERAGE "
                                                                       f"{selected_column_2} for "
                                                                       f"All Topics",
                      labels={selected_column_2: f'AVG {selected_column_2}', 'Name': 'Topic ID'})

        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)

