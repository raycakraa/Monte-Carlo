import pandas
import streamlit as st
import pandas as pd
import os
import random
import locale

st.title('Penjualan Tableware')
st.subheader('Ray Cakradiningrat - 152017039')
st.sidebar.subheader('Monte-Carlo')


def find_sum(d):
    res = 0

    for i in range(len(d)):
        res += d[i]

    return res


def rupiah_format(angka, with_prefix=False, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp. {}".format(rupiah)
    return rupiah


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

    res = 0
    reslist = []
    for i in range(len(y)):
        res += y[i] / frek
        st.sidebar.text("Probabilitas Komulatif " +
                        str(i)+": "+str(round(res, 3)))
        reslist.append(res)
    st.sidebar.text("")

    # st.text(reslist[1])
    aa = 0
    ab = 0
    for i in range(len(y)):
        aa += y[i] / frek
        st.sidebar.text("BB Interval "+str(i)+": "+str(round(ab, 5)))
        ab = aa + 0.001

else:
    st.write("Silahkan Pilih file csv yang akan digunakan !")
