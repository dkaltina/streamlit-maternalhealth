import pickle
import streamlit as st

# load save model
model = pickle.load(open('Martial_Model.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Tingkat Intensitas Resiko Selama Kehamilan')

st.subheader('Nama : Dede Kaltina')
st.subheader('Nim : 211352020')

# Form Input
Age = st.text_input('Masukan Umur')

SystolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Tinggi') 

DiastolicBP = st.text_input('Masukan Nilai Tekanan Darah Yang Lebih Rendah')

Bs = st.text_input('Masukan Nilai Kadar Glukosa Dalam Darah')

BodyTemp = st.text_input('Masukan Nilai Temperatur Badan')

HeartRate = st.text_input('Masukan Nilai Detak Jantung Dalam Keadaan Normal')


# kode Prediksi
Maternal_diagnosis = ' '

#Button Prediksi
if st.button('Prediksi Resiko'):
    Maternal_prediction = model.predict([[Age, SystolicBP, DiastolicBP,Bs, BodyTemp, HeartRate]])

    if(Maternal_prediction[0]==0):
        Maternal_diagnosis = 'Tingkat Resiko Rendah'

    elif(Maternal_prediction[0]==1):
          Maternal_diagnosis = 'Tingkat Resiko Sedang'

    else:
         Maternal_diagnosis = 'Tingkat Resiko Tinggi'

st.success(Maternal_diagnosis)
