
from pandas.core.indexes.base import Index
from plotly import plot
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px

df = pd.read_csv("E:\Xethon\Retail Product Recommender.csv")
df["InvoiceDate"]=df["InvoiceDate"].astype('datetime64[ns]')
df["StockCode"]=df["StockCode"].astype('string')
df = df[df.Quantity > 0]
st.set_page_config(page_title="Sale Analyzer", page_icon=None, layout='centered', initial_sidebar_state='collapsed')
st.title("Sale Analyzer")
drop_down=st.sidebar.selectbox("Click to explore?", ('Top 10 Products', 'Less Sold Products', 'Monthly Sales', 'Review System','Home'),4)
if drop_down=="Home":
    st.write("Product Sale Analyzer")
    st.write("This analyser analysis the followings, which are useful insights for product recommendation")
    st.write("1. Top 10 best performing products")
    st.write("2. Seasonal wise best performing products")
    st.write("3. Review system as additional attributes to enhance the futuristic approach of the product")
    st.write("This web app suggests the products to its customers. And is capable of predicting the reviews which are stored for growth and better scalability of the product itself!")

if drop_down=="Top 10 Products":
    st.write("Top 10 Sold Products ")
    Top_sale=df.groupby(["Description"],as_index=False).sum().sort_values("Quantity",ascending=False).drop(['UnitPrice','CustomerID'], axis = 1)
    Top_sale=Top_sale.reset_index(drop=True)
    Top_sale.index=np.arange(1,len(Top_sale)+1)
    Top_ten_sale=Top_sale.head(10)
    st.table(Top_ten_sale)
    st.write("Top 10 products contribution in the sale")
    img=Image.open("asserts/newplot.png")
    st.image(img)
if drop_down=="Less Sold Products":
    st.write("Less Sold products")
    less_sale=df.groupby(["Description"],as_index=False).sum().sort_values("Quantity").drop(['UnitPrice','CustomerID'], axis = 1)
    less_sale=less_sale.reset_index(drop=True)
    less_sale.index=np.arange(1,len(less_sale)+1)
    less_ten_sale=less_sale.head(10)
    st.table(less_ten_sale)
if drop_down=="Monthly Sales":
    df['year'] = pd.DatetimeIndex(df['InvoiceDate']).year
    df['month'] = pd.DatetimeIndex(df['InvoiceDate']).month
    a1=df.groupby(["Description","month","year"],as_index=False)["Quantity"].sum()
    year2010=a1[a1['year'] == 2010]
    year2011=a1[a1['year'] == 2011]
    year2010=year2010.sort_values('month')
    year2011=year2011.sort_values('month')
    year2010=year2010.loc[year2010.groupby(["month"])["Quantity"].idxmax()]
    year2011=year2011.loc[year2011.groupby(["month"])["Quantity"].idxmax()]
    st.write("Month Wise Top Sold Products in 2010")
    st.table(year2010)
    img=Image.open("asserts\products_2010.png")
    st.image(img)
    plot_bar = px.data.gapminder()
    px.bar(data_frame=year2010, x='Description',y='Quantity',color='Description')
    st.write("Month Wise Top Sold Products in 2011")
    st.table(year2011)
    img1=Image.open("asserts\products_2011.png")
    st.image(img1)