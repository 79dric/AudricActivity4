import streamlit as st

st.title("Clasificador de temperatura")
Temperatura= st.number_input(
  "Introduce la temperatura=",
  value=20
)



if Temperatura<=10:
  print ("Hace frio")
elif 10<=Temperatura<=24:
  print ("La temperatura es agradable")
else:
  print ("hace calor")
