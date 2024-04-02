import streamlit as st
import numpy as np
import joblib 
from predict_cost import predict # modeli çağırdığımız dosyadaki fonksiyon.

# INTERFACE

st.markdown('## Emlak Fiyat Tahmini')

st.write('---------------------------------')

# Her parametre için Entry Space açıyoruz :

longitude = st.number_input('Longitude :')
latitude = st.number_input('Latitude :')
housing_median_age = st.number_input('Housing Median Age :')
total_rooms = st.number_input('Total Rooms :')
total_bedrooms = st.number_input('Total Bedrooms :')
population = st.number_input('Population :')
households = st.number_input('Households :')
median_income = st.number_input('Median Income :')
ocean_proximity = st.number_input('Ocean Proximity :(1H OCEAN = 0;INLAND = 1;ISLAND = 2;NEAR BAY = 3;NEAR OCEAN = 4 )')

# PREDICT BUTTON

if st.button('Ev Fiyatını Tahmin Et ') :
        fiyat = predict(np.array([[longitude, latitude,               housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity]]))
        st.text(fiyat[0])
        