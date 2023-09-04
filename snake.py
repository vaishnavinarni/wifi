# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:06:27 2023

@author: VAISHNAVI
"""

import streamlit as st
import random
import time

# Streamlit UI setup
st.title("Snake Game")
st.sidebar.header("Controls")
st.sidebar.markdown("Use arrow keys to move the snake.")
start_button = st.sidebar.button("Start")

# Game setup
width = 20
height = 10
snake = [(5, 5)]
food = (random.randint(0, width - 1), random.randint(0, height - 1))
direction = (0, -1)
score = 0
game_over = False

# Game loop
while start_button:
    if not game_over:
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            new_head[0] < 0
            or new_head[0] >= width
            or new_head[1] < 0
            or new_head[1] >= height
            or new_head in snake
        ):
            game_over = True
        else:
            snake.insert(0, new_head)

            if snake[0] == food:
                score += 1
                food = (random.randint(0, width - 1), random.randint(0, height - 1))
            else:
                snake.pop()

    st.write(f"Score: {score}")

    for y in range(height):
        for x in range(width):
            if (x, y) == food:
                st.write("🍎", end=" ")
            elif (x, y) in snake:
                st.write("🐍", end=" ")
            else:
                st.write(" ", end=" ")
        st.write("")

    if game_over:
        st.write("Game Over!")
        start_button = False

    time.sleep(0.2)

st.write("Click 'Start' to play the Snake game.")
