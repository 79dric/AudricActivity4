import streamlit as st


edad= st.number_input(
  "La edad de esta persona es:",
  value=18 
)

st.checkbox("Tiene identificación")
            
