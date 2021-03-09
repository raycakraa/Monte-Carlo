import pandas
import streamlit as st
import pandas as pd
import os

st.title('Penjualan Tableware')
st.subheader('Ray Cakradiningrat - 152017039')
st.sidebar.subheader('Monte-Carlo')


def find_sum(d):
    res = 0

    for i in range(len(d)):
        res += d[i]

    return res


uploaded_file = st.file_uploader("Pilih file csv yang akan digunakan")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    x = df.iloc[:, :-1].values
    y = df.iloc[:, 1].values

    frek = int(find_sum(y))

    st.sidebar.text("Frekuensi : "+str(frek))
    st.sidebar.text("")
    for i in range(len(y)):
        prob = y[i] / frek
        st.sidebar.text("Probabilitas "+str(i)+": "+str(round(prob, 3)))
    st.sidebar.text("")

else:
    st.write("Silahkan Pilih file csv yang akan digunakan !")
