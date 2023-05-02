import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('Prediksi_Prod_Minyak_Mesir.sav', 'rb'))

df = pd.read_csv("oil_prod_percapita.csv")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)

st.title('Forecasting Produksi Minyak Per Capita Di Benua Africa (Dalam satuan US bbl oil)')
year = st.slider("Tentukan tahun untuk memprediksi produksi minyak", 1,50, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['oil_prod_per_capita'])

if st.button("Prediction"):
    
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax =plt.subplots()
        df['oil_prod_per_capita'].plot(style='--', color='green', legend = True, label = 'known')
        pred['oil_prod_per_capita'].plot(color='b', legend= True, label= 'Prediction')
        st.pyplot(fig)
