import streamlit as st
import pandas as pd
#import seaborn as sns

from st_pages import find_most_pricey_artwork, find_less_pricey_artwork, check_and_visualize_works, average_year_price



def main():
    st.title("Exploring Artistic Value: From Sotheby's Most Expensive to Affordable Auction Gems")

    # Load your dataset
    data = pd.read_csv('Data/corrected_artDataset.csv') 

    displayed_most_expensive_artworks = []
    displayed_less_expensive_artworks = []


    # most expensive 
    most_pricey_artwork_title, most_pricey_artwork_price, most_pricey_artwork_artist, most_pricey_artwork_image, most_pricey_artwork_year, most_pricey_artwork_movement = find_most_pricey_artwork(data)
    # Format caption without parentheses
    caption = f"{most_pricey_artwork_title}, {most_pricey_artwork_artist}, {most_pricey_artwork_year}"    
    st.markdown("---")  # Add vertical space
    st.subheader("Sotheby's Most Expensive Auction Artwork:")

    st.write("Artist: ", most_pricey_artwork_artist)
    st.write("Title: ", most_pricey_artwork_title)
    st.write("Movement: ", most_pricey_artwork_movement)
    st.write("Price: ", most_pricey_artwork_price)

    st.image(most_pricey_artwork_image, caption=caption)
    # Count occurrences of the most expensive artist
    most_expensive_artist_count = (data['artist'] == most_pricey_artwork_artist).sum()
    # Display the results
    st.markdown(f"{most_pricey_artwork_artist} appears {most_expensive_artist_count} times in the [Dataset.](https://www.kaggle.com/datasets/flkuhm/art-price-dataset?select=artDataset)")

    average_price_most_expensive = average_year_price(data, most_pricey_artwork_year)
    st.write(f"Average price of artworks created in the year {most_pricey_artwork_year}: ${average_price_most_expensive:.2f}")


    displayed_most_expensive_artworks.append(most_pricey_artwork_title)

    show_most_expensive = st.radio(f"Show other works by {most_pricey_artwork_artist}?", ("Yes", "No"))
    if show_most_expensive == "Yes":
        check_and_visualize_works(data, most_pricey_artwork_artist, displayed_most_expensive_artworks)

    # --------------------------------------------------------------------------------------------------
    # less expensive
    less_pricey_artwork_title, less_pricey_artwork_price, less_pricey_artwork_artist, less_pricey_artwork_image, less_pricey_artwork_year, less_pricey_artwork_movement = find_less_pricey_artwork(data)
    # Format caption without parentheses
    caption_less = f"{less_pricey_artwork_title}, {less_pricey_artwork_artist}, {less_pricey_artwork_year}"    
    st.subheader("Sotheby's Less Expensive Auction Artwork:")
    st.write("Artist: ", less_pricey_artwork_artist)
    st.write("Title: ", less_pricey_artwork_title)
    st.write("Movement: ", less_pricey_artwork_movement)
    st.write("Price: ", less_pricey_artwork_price)

    st.image(less_pricey_artwork_image, caption=caption_less)

    # Count occurrences of the least expensive artist
    least_expensive_artist_count = (data['artist'] == less_pricey_artwork_artist).sum()
    # Display the results
    st.markdown(f"{less_pricey_artwork_artist} appears {least_expensive_artist_count} times in the [Dataset.](https://www.kaggle.com/datasets/flkuhm/art-price-dataset?select=artDataset)")

    average_price_least_expensive = average_year_price(data, less_pricey_artwork_year)
    st.write(f"Average price of artworks created in the year {less_pricey_artwork_year}: ${average_price_least_expensive:.2f}")

    show_least_expensive = st.radio(f"Show other works by {less_pricey_artwork_artist}?", ("Yes", "No"))
    if show_least_expensive == "Yes":
        check_and_visualize_works(data, less_pricey_artwork_artist, displayed_less_expensive_artworks)
    
    st.markdown("---")  # Add vertical space
if __name__ == "__main__":
    main()
