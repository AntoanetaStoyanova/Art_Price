
from pathlib import Path

import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')





st.set_page_config(page_title="Art Price", page_icon=":art:", layout="wide")

st.title("Art Price Visualization")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

#st.sidebar.success("Select a demo above.")

st.image('images/artDataset/image_26.png', caption='Wayne Thiebaud, Dark Canyon Bluffs, 2014')



st.caption("Welcome to ART PRICE ! Discover the fascinating world of art prices with our interactive platform powered by data from Sotheby's, one of the world's most renowned auction houses. Our app allows you to explore and analyze the prices of artworks and sculptures that have been offered for sale at Sotheby's auctions. By leveraging a dataset sourced from Kaggle, we bring you a comprehensive view of the art market trends over time. Through intuitive visualization tools built with Python libraries and deployed using Streamlit, you can delve into the nuances of art pricing, uncovering insights and patterns that shape this dynamic industry. Let's embark on a journey through the world of art prices together!")
