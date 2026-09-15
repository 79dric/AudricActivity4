import streamlit as st

st.title("Clasificador de temperatura")
Temperatura= st.number_input(
  "Introduce la temperatura=",
  value=20
)



if Temperatura<=10:
  st.write("Hace frio")
elif 10<=Temperatura<=24:
  st.write("La temperatura es agradable")
else:
  st.write ("hace calor")
