# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:43:49 2023

@author: Dell
"""
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_user_agent")

city ="NASHIK"
country ="INDIA"

loc = geolocator.geocode(city+','+ country)

a=loc.latitude
b=loc.longitude

print(a)
print(b)
# print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)


