# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:58:05 2023

@author: VAISHNAVI
"""

import streamlit as st
import random

# Streamlit UI setup
st.title("CAR RACING")
st.sidebar.header("Controls")
speed = st.sidebar.slider("Speed", min_value=1, max_value=20, step=1, value=10)
start_button = st.sidebar.button("Start")
quit_button = st.sidebar.button("Quit")

# Car and obstacle setup
car_x = 400
car_y = 470
car_width = 56
obs_x = random.randint(200, 650)
obs_y = -750
obs_width = 56
obs_height = 125
car_passed = 0
score = 0

# Game loop
while start_button:
    st.image("grass.jpg", width=800)
    st.image("y_strip.jpg", width=400)
    st.image("strip.jpg", width=20)

    st.image("car1.jpg", use_column_width=True, output_format="JPEG")
    st.image("car2.jpg", use_column_width=True, output_format="JPEG")

    car_x += st.slider("Move Car", min_value=-5, max_value=5, step=1, value=0)
    car_x = max(120, min(car_x, 680 - car_width))

    st.image("car1.jpg", use_column_width=True, output_format="JPEG")

    obs_y -= (speed / 4)
    st.image("car2.jpg", width=obs_width)
    obs_y += speed

    if obs_y > 600:
        obs_y = 0 - obs_height
        obs_x = random.randint(170, 600)
        car_passed += 1
        score = car_passed * 10

    st.image("car1.jpg", use_column_width=True, output_format="JPEG")

    if car_x + car_width > obs_x and car_x < obs_x + obs_width and car_y < obs_y + obs_height:
        st.header("CAR CRASHED")
        start_button = False

    st.write(f"Passed: {car_passed}")
    st.write(f"Score: {score}")

    if car_passed > 0 and car_passed % 10 == 0:
        st.write(f"Level: {car_passed // 10 + 1}")

    if quit_button:
        start_button = False

st.write("Game Over!")
