# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:34:50 2023

@author: Dell
"""
from geopy.geocoders import Nominatim
import pickle

geolocator = Nominatim(user_agent="my_user_agent")

city =" Aundh, Pune"
country ="INDIA"

loc = geolocator.geocode(city+','+ country)

a=loc.latitude
b=loc.longitude

# # # #### load machine learning model
loaded_model = pickle.load(open('knn_model.sav', 'rb'))
locs = loaded_model.predict([[a, b]])
print(locs)
