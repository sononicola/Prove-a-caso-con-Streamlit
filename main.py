import streamlit as st
import pandas as pd

st.title("Prove a caso")
st.header("Load Comb")

nCarichi = st.number_input("n carichi", min_value=1, value=3)
carichi = ["g1","g2","snow"]

c1, c2, c3 = st.columns(3)
with c1:
    a = [st.number_input(f"ciao {i+1}",min_value=1, max_value=4,key=i) for i in range(0,nCarichi)]
with c2:
    b = [st.selectbox(f"Carico {i+1}", options=carichi, key=i) for i in range(0,nCarichi)]
    
st.dataframe(pd.DataFrame(list(zip(a,b))))
