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

    aa = 0
    ab = 0
    for i in range(len(y)):
        aa += y[i] / frek
        st.sidebar.text("BB Interval "+str(i)+": "+str(round(ab, 5)))
        ab = aa + 0.001

    des = 229900
    st.text("Harga Tableware: Rp."+str(rupiah_format(des)))
    col1, col2, col3 = st.beta_columns(3)
    randomlist = []
    for i in range(1, 16):
        n = random.random()
        col1.text("Angka acak "+str(i)+": "+str(round(n, 3)))
        randomlist.append(n)

    a = 1
    perlist = []
    for i in range(len(randomlist)):
        if (randomlist[i] <= reslist[0]):
            b = 0
            col2.text("Permintaan "+str(a)+": "+str(b))
        elif (randomlist[i] <= reslist[1]):
            b = 1
            col2.text("Permintaan "+str(a)+": "+str(b))
        elif (randomlist[i] <= reslist[2]):
            b = 2
            col2.text("Permintaan "+str(a)+": "+str(b))
        elif (randomlist[i] <= reslist[3]):
            b = 3
            col2.text("Permintaan "+str(a)+": "+str(b))
        elif (randomlist[i] <= reslist[4]):
            b = 4
            col2.text("Permintaan "+str(a)+": "+str(b))
        perlist.append(b)
        a = a+1

    c = 1
    pemlist = []
    for i in range(len(perlist)):
        d = perlist[i]*int(des)
        col3.text("Pemasukan "+str(c)+": Rp."+str(rupiah_format(d)))
        pemlist.append(d)
        c = c+1

    per = int(find_sum(perlist))
    st.text("")
    st.text("Jumlah Permintaan : "+str(per))
    aver_per = int(find_sum(perlist))/len(perlist)
    st.text("Rata-rata Permintaan Per Hari: "+str(aver_per))
    aver_pem = int(find_sum(pemlist))/len(pemlist)
    st.text("Rata-rata Pemasukan Per Hari: Rp."+str(rupiah_format(aver_pem)))
else:
    st.write("Silahkan Pilih file csv yang akan digunakan !")
