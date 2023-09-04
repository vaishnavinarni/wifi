# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:58:12 2023

@author: VAISHNAVI
"""

import streamlit as st
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Streamlit UI setup
st.title("Phone Number Information")
phone_number = st.text_input("Enter Phone number with country code (+xx xxxxxxxxx):")
check_button = st.button("Check")

# Function to validate and retrieve phone number information
def get_phone_info(phone_number):
    try:
        phone_number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(phone_number):
            region = timezone.time_zones_for_number(phone_number)
            service_provider = carrier.name_for_number(phone_number, "en")
            country = geocoder.description_for_number(phone_number, "en")
            return region, service_provider, country
        else:
            return None
    except Exception as e:
        return None

# Display phone number information if valid
if check_button:
    if phone_number:
        info = get_phone_info(phone_number)
        if info:
            st.write('Phone Number belongs to region:', info[0])
            st.write('Service Provider:', info[1])
            st.write('Phone number belongs to country:', info[2])
        else:
            st.write("Please enter a valid mobile number")
    else:
        st.write("Please enter a mobile number")
