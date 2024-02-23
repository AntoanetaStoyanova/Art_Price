import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Fonction pour afficher la page d'accueil
def show_home():
    st.title("Home Page")
    st.write("Bienvenue sur la page d'accueil.")

# Fonction pour afficher la page de statistiques
def show_statistics():
    st.title("Statistiques")
    st.write("Voici quelques statistiques intéressantes.")

# Fonction pour afficher la page de tracé
def show_plot():
    st.title("Graphique")
    st.write("Voici un graphique intéressant.")



def find_most_pricey_artwork(data):
    sorted_data = data.sort_values(by='price_amount', ascending=False)
    most_pricey_artwork_title = sorted_data.iloc[0]['title']
    most_pricey_artwork_price = sorted_data.iloc[0]['price']
    most_pricey_artwork_artist = sorted_data.iloc[0]['artist']
    most_pricey_artwork_image = sorted_data.iloc[0]['filename']
    most_pricey_artwork_year = sorted_data.iloc[0]['yearCreation']
    most_pricey_artwork_movement = sorted_data.iloc[0]['movement']
    

    return most_pricey_artwork_title, most_pricey_artwork_price, most_pricey_artwork_artist, most_pricey_artwork_image, most_pricey_artwork_year, most_pricey_artwork_movement

def find_less_pricey_artwork(data):
    sorted_data = data.sort_values(by='price_amount', ascending=True)
    less_pricey_artwork_title = sorted_data.iloc[0]['title']
    less_pricey_artwork_price = sorted_data.iloc[0]['price']
    less_pricey_artwork_artist = sorted_data.iloc[0]['artist']
    less_pricey_artwork_image = sorted_data.iloc[0]['filename']
    less_pricey_artwork_year = sorted_data.iloc[0]['yearCreation']
    less_pricey_artwork_movement = sorted_data.iloc[0]['movement']

    return less_pricey_artwork_title, less_pricey_artwork_price, less_pricey_artwork_artist, less_pricey_artwork_image, less_pricey_artwork_year, less_pricey_artwork_movement



def check_and_visualize_works(data, artist_name, displayed_artworks):
    if artist_name:
        artist_count = (data['artist'] == artist_name).sum()
        if artist_count > 1:
            st.subheader(f"Other Works by {artist_name} in the Dataset:")
            other_works = data[data['artist'] == artist_name]
            for index, row in other_works.iterrows():
                if row['title'] not in displayed_artworks:
                    st.write("Title:", row['title'])
                    st.write("Movement:", row['movement'])
                    st.write("Price:", row['price'])
                    st.image(row['filename'], caption=f"{row['title']}, {row['artist']}, {row['yearCreation']}")
                    st.markdown("---")  # Add vertical space
        else:
            st.write(f"No other works by {artist_name} in the dataset.")


def average_year_price(data, year):
    artworks_same_year = data[data['yearCreation'] == year]
    if len(artworks_same_year) > 0:
        average_price = artworks_same_year['price_amount'].mean()
        return average_price
    else:
        return None
    
def plot_scatter_with_regression(data):
    # Drop rows with NaN values in 'yearCreation' column
    data.dropna(subset=['clean_yearCreation'], inplace=True)

    # Plot scatter plot with regression lines
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='clean_yearCreation', y='price_amount', data=data, hue='clean_signed', ax=ax)
    sns.regplot(x='clean_yearCreation', y='price_amount', data=data, scatter=False, color='blue', label='Signed', ax=ax)
    plt.xlabel('Year of Creation')
    plt.ylabel('Price')
    plt.title('Scatter Plot with Regression')
    plt.legend()
    st.pyplot(fig)


def check_and_vis_artworks(artist_data):
    artist_data['clean_yearCreation'] = pd.to_datetime(artist_data['clean_yearCreation']).dt.year
    st.subheader(f"Artworks by {artist_data.iloc[0]['artist']}: ")
    #st.dataframe(artist_data[['title', 'price']])
    st.image(artist_data['filename'].tolist(), 
             caption=artist_data.apply(lambda x: f"{x['title']}, {x['artist']}, {x['clean_yearCreation']}", axis=1).tolist())

