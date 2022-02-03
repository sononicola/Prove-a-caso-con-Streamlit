import streamlit as st
import pandas as pd

st.title("Prove a caso")
st.header("Load Comb")

nCarichi = st.number_input("n carichi", min_value=1, value=3)
carichi = ["g1","g2","snow"]
sfav_or_fav = ["sfav" , "fav"]

c1, c2, c3, c4 = st.columns([1,0.8,0.6,0.5])
with c1:
    a = [
        st.text_input(
            f"Nome {i}",
            value = "Load Name " + str(i),
            key = "LoadName" + str(i)
            ) 
        for i in range(1,nCarichi+1)
        ]
with c2:
    b = [
        st.number_input(
            f"Valore {i}",
            min_value = 1.,
            step = 1.,
            format = "%.4f",
            key = "LoadValue" + str(i)
            ) 
        for i in range(1,nCarichi+1)
        ]
with c3:
    c = [
        st.selectbox(
            f"Tipologia {i}", 
            options = carichi, 
            key = "LoadType" + str(i)            
            ) 
        for i in range(1,nCarichi+1)
        ]
with c4:
    d = [
        st.selectbox(
            f"Sfav or Fav {i}", 
            options = sfav_or_fav, 
            key = "Load_sfav_or_fav" + str(i)            
            ) 
        for i in range(1,nCarichi+1)
        ]
    
st.table(pd.DataFrame(list(zip(a,b,c,d))))
