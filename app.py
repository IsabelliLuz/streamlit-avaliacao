import pandas as pd
import streamlit as st
import altair as alt  


df = pd.read_csv("dataset.csv")


chart = alt.Chart(df).mark_bar().encode(
    x="Segment:N",
    y="count(Product):Q",
    color="Segment:N"
)


st.title("Distribuição de Produtos por Segmento")
st.altair_chart(chart, use_container_width=True)
