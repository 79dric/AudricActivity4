import streamlit as st


edad= st.number_input(
  "La edad de esta persona es:",
  value=18 
)

identificacion= st.checkbox("Tiene identificación")

if 18<=edad and identificación= True:
  st.write("puede ingresar")
else:
  st.write("no puede ingresar")
            
