import streamlit as st
import random

def play_game():
    st.title("Guess the Number Game")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None
    
    st.write("I'm thinking of a number between 1 and 100.")
    
    while guess != secret_number:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
        attempts += 1
        
        if guess < secret_number:
            st.write("Too low. Try again.")
        elif guess > secret_number:
            st.write("Too high. Try again.")
    
    st.success(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

if __name__ == "__main__":
    play_game()
