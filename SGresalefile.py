import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1= int(2)
    elif town_map == 'BUKIT BATOK':
        town_1= int(3)
    elif town_map == 'BUKIT MERAH':
        town_1= int(4)
    elif town_map == 'BUKIT PANJANG':
        town_1= int(5)

    elif town_map == 'BUKIT TIMAH':
        town_1= int(6)
    elif town_map == 'CENTRAL AREA':
        town_1= int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1= int(8)
    elif town_map == 'CLEMENTI':
        town_1= int(9)
    elif town_map == 'GEYLANG':
        town_1= int(10)
    
    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1= int(12)
    elif town_map == 'JURONG WEST':
        town_1= int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1= int(14)
    elif town_map == 'MARINE PARADE':
        town_1= int(15)

    elif town == 'PASIR RIS':
        town_1= int(16)
    elif town == 'PUNGGOL':
        town_1= int(17)
    elif town == 'QUEENSTOWN':
        town_1= int(18)
    elif town == 'SEMBAWANG':
        town_1= int(19)
    elif town == 'SENGKANG':
        town_1= int(20)

    elif town == 'SERANGOON':
        town_1= int(21)
    elif town == 'TAMPINES':
        town_1= int(22)
    elif town == 'TOA PAYOH':
        town_1= int(23)
    elif town == 'WOODLANDS':
        town_1= int(24)        
    elif town == 'YISHUN':
        town_1= int(25)      

    return town_1

def flat_type_mapping(flt_type):

    if flt_type == '1 ROOM':
        flat_type_1= int(0)
    elif flt_type == '2 ROOM':
        flat_type_1= int(1)
    elif flt_type == '3 ROOM':
        flat_type_1= int(2)
    elif flt_type == '4 ROOM':
        flat_type_1= int(3)
    elif flt_type == '5 ROOM':
        flat_type_1= int(4)
    elif flt_type == 'EXECUTIVE':
        flat_type_1= int(5)
    elif flt_type == 'MULTI-GENERATION':
        flat_type_1= int(6)

    return flat_type_1
def flat_model_mapping(fl_m):
    
    if fl_m == '2-room':
        flat_model_1= int(0)
    elif fl_m == '3Gen':
        flat_model_1= int(1)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(2)
    elif fl_m == 'Apartment':
        flat_model_1= int(3)
    elif fl_m == 'DBSS':
        flat_model_1= int(4)
    elif fl_m == 'Improved':
        flat_model_1= int(5)
  
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(6)
    elif fl_m == 'Maisonette':
        flat_model_1

def predict_price(year,town,flat_type,flr_area_sqm,flat_model,stry_start,stry_end,re_les_year,
              re_les_month,les_coms_dt):
    
    year_1= int(year)
    town_2= town_mapping(town)
    flt_ty_2= flat_type_mapping(flat_type)
    flr_ar_sqm_1= int(flr_area_sqm)
    flt_model_2= flat_model_mapping(flat_model)
    str_str= np.log(int(stry_start))
    str_end= np.log(int(stry_end))
    rem_les_year= int(re_les_year)
    rem_les_month= int(re_les_month)
    lese_coms_dt= int(les_coms_dt)


    with open(r"D:\Data Science\Python\Code\SGResaleFlatPrices.pkl","rb") as f:
        regg_model= pickle.load(f)

    user_data = np.array([[year_1,town_2,flt_ty_2,flr_ar_sqm_1,
                           flt_model_2,str_str,str_end,rem_les_year,rem_les_month,
                           lese_coms_dt]])
    y_pred_1 = regg_model.predict(user_data)
    price= np.exp(y_pred_1[0])

    return round(price)



st.set_page_config(layout="wide")

st.title(":blue[SINGAPORE RESALE FLAT PRICE PREDICTION]")
st.write("")

with st.sidebar:
    select= option_menu("MAIN MENU",["Home", "Price Prediction"])

if select == "Home":
    st.write(":green[Singapore Resale Flat Price Prediction aims to predicts the resale prices of flats in Singapore.]")
    st.write("")
    st.write(":green[It helps to assist both potential buyers and sellers in estimating the resale value of a flat.]")
    img= Image.open(r"D:\Data Science\Python\Projects\Project-6 Singapore Resale\Flat.jpg")
    st.image(img,width=400)


elif select == "Price Prediction":

    col1,col2= st.columns(2)
    with col1:

        year= st.selectbox("Select the Year",["2015", "2016", "2017", "2018", "2019", "2020", "2021",
                           "2022", "2023", "2024"])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type= st.selectbox("Select the Flat Type", ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flr_area_sqm= st.number_input("Enter the value of Floor Area sqm")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])
        
    with col2:

        stry_start= st.number_input("Enter the value of Storey Start")

        stry_end= st.number_input("Enter the value of Storey End")

        re_les_year= st.number_input("Enter the value of Remaining Lease Year")

        re_les_month= st.number_input("Enter the value of Remaining Lease Month")
        
        les_coms_dt= st.selectbox("Select the Lease Commence_Date", [str(i) for i in range(1966,2023)])

    button= st.button("Predict the Price", use_container_width= True)

    if button:

            
        pre_price= predict_price(year, town, flat_type, flr_area_sqm, flat_model,
                        stry_start, stry_end, re_les_year, re_les_month, les_coms_dt)

        st.write("## :green[**Predicted Price:**]",pre_price)

