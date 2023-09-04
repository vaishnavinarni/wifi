# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:03:50 2023

@author: VAISHNAVI
"""

import streamlit as st
import requests

# Streamlit UI setup
st.title("Sudoku Solver")
st.sidebar.header("Options")
difficulty = st.sidebar.selectbox("Select Difficulty", ["easy", "medium", "hard"])
solve_button = st.sidebar.button("Solve")

# Fetch Sudoku board from API
response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={difficulty}")
sudoku_board = response.json()["board"]
original_board = [row[:] for row in sudoku_board]

# Function to solve Sudoku
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Sudoku solved

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, num, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False  # No solution

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid_move(board, num, row, col):
    return (
        is_valid_in_row(board, num, row)
        and is_valid_in_col(board, num, col)
        and is_valid_in_box(board, num, row - row % 3, col - col % 3)
    )

def is_valid_in_row(board, num, row):
    return num not in board[row]

def is_valid_in_col(board, num, col):
    return num not in [board[row][col] for row in range(9)]

def is_valid_in_box(board, num, row, col):
    return num not in [
        board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)
    ]

# Streamlit app
if solve_button:
    if solve_sudoku(sudoku_board):
        st.success("Sudoku Solved!")
    else:
        st.error("No solution found!")

for i in range(9):
    row = ""
    for j in range(9):
        if original_board[i][j] == 0:
            row += st.text_input("", value=str(sudoku_board[i][j]), key=(i, j))
        else:
            row += st.text_input("", value=str(sudoku_board[i][j]), key=(i, j), disabled=True)
        if j < 8:
            row += " | "
    st.write(row)
    if i < 8:
        st.write("-" * 47)
