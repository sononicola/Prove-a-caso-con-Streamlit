import streamlit as st
import pandas as pd

# -- DATA --
carichi = ["G1", "G2", "Snow"]
sfav_or_fav = ["sfav", "fav"]
gamma_coef = ["EQU", "A1", "A2"]
# Timber: 
service_classes = ["1", "2", "3"]
timber_materials = ["Massiccio-Lamellare-LVL"] #  tab 4.4.IV NTC

# -- GENERAL PAGE SETUP --
st.set_page_config(
     page_title = "Load Combinations",
     page_icon = "👷‍♂️",
     initial_sidebar_state = "expanded"
)
# -- SIDEBAR --
gamma_type = st.sidebar.radio(
            label = f"Tipologia di coefficiente gamma", 
            options = gamma_coef, 
            index = 1,
            key = "gamma_type"            
) 
is_Timber = st.sidebar.checkbox(
    label = "Is this a Timber structure?",
    help = "So it will be used kmod coefficients too"
)
if is_Timber:
    service_class = st.sidebar.radio(
            label = "Classe di servizio", 
            options = service_classes, 
            index = 0,
            key = "service_class"            
    ) 
    timber_material = st.sidebar.selectbox(
            label = "Tipologia di legno secondo Tab 4.4.IV NTC", 
            options = timber_materials, 
            key = "timber_material"            
    ) 

# -- PAGE CONTENT --
st.title("Prove a caso")
st.header("Load Comb")

nCarichi = int(st.number_input(
            label = "n carichi", 
            min_value=1, 
            value=3)
)
c1, c2, c3, c4 = st.columns([1,1.2,0.6,0.5])
with c1:
    a = [
        st.text_input(
            label = f"Nome {i}",
            value = f"Load Name {i}",
            key = f"LoadName {i}" # Streamlit is not able to create an unique key inside a for loop:
            ) 
        for i in range(1,nCarichi+1)
        ]
with c2:
    b = [
        st.number_input(
            label = f"Valore {i}",
            min_value = 1.,
            step = 1.,
            format = "%.3f",
            key = f"LoadValue {i}"
            )
        for i in range(1,nCarichi+1)
        ]
with c3:
    c = [
        st.selectbox(
            label = f"Tipologia {i}", 
            options = carichi, 
            key = f"LoadType {i}"            
            ) 
        for i in range(1,nCarichi+1)
        ]
with c4:
    d = [
        st.selectbox(
            label = f"Sfav or Fav {i}", 
            options = sfav_or_fav, 
            key = f"Load_sfav_or_fav {i}"            
            ) 
        for i in range(1,nCarichi+1)
        ]
    
st.table(pd.DataFrame(list(zip(a,b,c,d))))
