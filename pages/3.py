import streamlit as st 
import pandas as pd 
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
#import re
#import altair as alt

from st_pages import check_and_vis_artworks

def main():
    data = pd.read_csv('Data/corrected_artDataset.csv')
    price = data['price_amount']

    #---------------------------------------------
    # Replace NaN values in 'period' column with 'unknown'
    data['period'] = data['period'].replace('[nan]', 'unknown')
    period = data['period']
    data.dropna(subset=['clean_yearCreation'], inplace=True)
    # Convert 'clean_yearCreation' column to datetime (converting the column to string, removing non-digit characters, removing the last character, and then converting the result to datetime using pd.to_datetime())
    data['clean_yearCreation'] = pd.to_datetime((data['clean_yearCreation'].astype(str)).str.replace(r'\D', '', regex=True).str[:-1], format='%Y')
    fig = go.Figure( go.Pie(labels=period, values=price))

    st.header("% of artworks for every period")
    st.plotly_chart(fig)

    #---------------------------------------------
    unknown_artworks = data[data['period'] == 'unknown']
    unknown_count = unknown_artworks.shape[0]    
    st.markdown(f"Number of artworks with 'unknown' period: {unknown_count}")
    
    if unknown_count > 0:
        st.subheader("Artworks with 'unknown' period:")
        st.dataframe(unknown_artworks[['artist', 'title', 'price', 'period']])

        # Allow user to toggle whether they want to check the artworks or not
        check_artwork = st.checkbox('Click to check the artworks with unknown period')

        # If the toggle is on, then proceed to display the artworks
        if check_artwork:
            # Allow user to select an artist
            selected_artist = st.selectbox('Look at the artwork of:', unknown_artworks['artist'].unique())

            # Filter unknown_artworks DataFrame based on selected artist
            selected_artist_data = unknown_artworks[unknown_artworks['artist'] == selected_artist]

            # Display artworks by the selected artist
            if not selected_artist_data.empty:
                check_and_vis_artworks(selected_artist_data)
    #---------------------------------------------
    
    # Replace NaN values in 'period' column with 'unknown'
    data['movement'] = data['movement'].replace('[nan]', 'unknown')


    
    st.header("Artworks by movement")
    options = st.multiselect(
        'Chose one or more movements',
        data['movement'].unique())
    
    if options:
        filtered_data = data[data['movement'].isin(options)]
        st.bar_chart(filtered_data, x='clean_yearCreation', y='movement')


    # ----------------------
    # Add blank space 
    st.markdown("<br>", unsafe_allow_html=True)
    # ----------------------
    
    # Sidebar widgets for selection
    
    # Convert 'clean_yearCreation' to datetime
    data['clean_yearCreation'] = pd.to_datetime(data['clean_yearCreation'])
    
    # Sidebar widget for selecting movement
    selected_movement = st.sidebar.selectbox('Select Movement', data['movement'].unique())
    
    # Filter data based on selected movement
    filtered_data = data[data['movement'] == selected_movement]
    # ----------------------
    # Add blank space 
    st.markdown("<br>", unsafe_allow_html=True)
    # ----------------------
    st.subheader('Ckeck the artwork by art movement and year:')
    if not filtered_data.empty:
        # Extract available years for the selected movement
        available_years = filtered_data['clean_yearCreation'].dt.year.unique()

        # Sidebar widget for selecting year
        selected_year = st.sidebar.selectbox('Select Year', available_years)

        # Filter data based on selected year
        filtered_data = filtered_data[filtered_data['clean_yearCreation'].dt.year == selected_year]
        
        # Display titles corresponding to the selected filters
        if not filtered_data.empty:
            art = filtered_data[['artist', 'title']]
            st.write("Titles:")
            st.write(art)
            check_and_vis_artworks(filtered_data)
            
        else:
            st.write("No titles found for the selected year.")
    else:
        st.write("No data found for the selected movement.")

    
    

if __name__ == "__main__":
    main()