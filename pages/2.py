import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import re


from st_pages import plot_scatter_with_regression, check_and_vis_artworks


def main():
    st.title("Exploring Art Value")


    # ----------------------
    # Add blank space 
    st.markdown("<br>"*3, unsafe_allow_html=True)
    # ----------------------


    # Load your dataset
    data = pd.read_csv('Data/corrected_artDataset.csv') 
    data_cat = pd.read_csv('Data/nlp_artDataset.csv')

    #-------------------------------------------------
   
    # Plot scatter plot with regression lines
    plot_scatter_with_regression(data)
    st.markdown("The scatter plot with regression lines provides insights into the relationship between the year of creation and the price of the signed artworks sold at the Sotheby's auctions. Signed artworks exhibit slightly higher prices compared to unsigned ones. However, the observed difference in prices between signed and unsigned artworks is relatively small, indicating that signing may not significantly affect the valuation of artworks within this specific auction setting.")
    
    # ----------------------
    # Add blank space 
    st.markdown("<br>"*3, unsafe_allow_html=True)
    # ----------------------
        
    # assigning 'category', 'clean_yearCreation', 'price_amount' to filtered_data_cat 
    filtered_data_cat = data_cat[['artist', 'title', 'filename', 'category', 'clean_yearCreation', 'price_amount', 'price']]
    # Remove rows with missing values in the 'clean_yearCreation' column
    filtered_data_cat.dropna(subset=['clean_yearCreation'], inplace=True)
    # Convert 'clean_yearCreation' column to datetime (converting the column to string, removing non-digit characters, removing the last character, and then converting the result to datetime using pd.to_datetime())
    filtered_data_cat['clean_yearCreation'] = pd.to_datetime((filtered_data_cat['clean_yearCreation'].astype(str)).str.replace(r'\D', '', regex=True).str[:-1], format='%Y')
    # create a line_chart graph
    st.line_chart(filtered_data_cat, x='clean_yearCreation', y='price_amount', color='category')
    st.markdown("The line chart presents the price of every artwork sold during the Sotheby's auctions in relation to their condition (good, very good, acceptable, and unknown) and the year of their creation. We can observe that the condition doesn't appear to be strongly related to the price. Surprisingly, artworks categorized as 'very good' condition are not necessarily the priciest in this auction.")

    # ----------------------
    # Add blank space 
    st.markdown("<br>", unsafe_allow_html=True)
    # ----------------------
    # Count how many artworks have 'unknown' condition
    unknown_artworks = filtered_data_cat[filtered_data_cat['category'] == 'unknown']
    unknown_count = unknown_artworks.shape[0]    
    st.markdown(f"Number of artworks with 'unknown' condition: {unknown_count}")
    
    # Display details of artworks with 'unknown' condition
    if unknown_count > 0:
        st.subheader("Artworks with 'unknown' condition:")
        #unknown_artworks = filtered_data_cat[filtered_data_cat['category'] == 'unknown']
        st.dataframe(unknown_artworks[['artist', 'title', 'price']])
        on = st.toggle('Click to check the artworks with unknown condition? ')
        if on:
            option = st.selectbox('Look at the artwork of:', unknown_artworks['artist'].unique())
            if option:
                selected_artist_data = unknown_artworks[unknown_artworks['artist'] == option]
                check_and_vis_artworks(selected_artist_data)

    # --------------------
    st.markdown("---")  # Add vertical space





   


if __name__ == "__main__":
    main()
