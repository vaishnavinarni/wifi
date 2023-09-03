# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:19:30 2023

@author: VAISHNAVI
"""

import streamlit as st
import subprocess

# Define a function to retrieve Wi-Fi profiles and passwords
def get_wifi_profiles():
    command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
    
    wifi_data = []
    
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        
        try:
            password = results[0]
        except IndexError:
            password = ""
        
        wifi_data.append({"Profile": i, "Password": password})
    
    return wifi_data

# Streamlit app
st.title("Wi-Fi Profiles and Passwords")

# Retrieve and display Wi-Fi profiles and passwords
wifi_profiles = get_wifi_profiles()

if wifi_profiles:
    st.write("List of Wi-Fi Profiles and Passwords:")
    for wifi_profile in wifi_profiles:
        st.write(f"Profile: {wifi_profile['Profile']}")
        st.write(f"Password: {wifi_profile['Password']}")
        st.write("-" * 30)
else:
    st.write("No Wi-Fi profiles found.")

# Display a button to close the app
if st.button("Close"):
    st.stop()
