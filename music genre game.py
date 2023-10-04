#!/usr/bin/env python

import random
import time

def timer(time_sec):
    """Timer function to count down"""
    start_time = time.time()
    end_time = start_time + time_sec
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        mins, secs = divmod(remaining_time, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        yield timeformat

def main():
    """Start guess a genre"""
    print("Welcome to the Music Genre Guessing Game!")
    correct_guesses = 0

    while True:
        print("\nRound {}: Guess a genre".format(correct_guesses + 1))

        music = [
            "hiphop",
            "popular music",
            "pop music",
            "rock",
            "jazz",
            "country music",
            "dance music"
        ]
        x = random.choice(music)
        print(x)
        guess = None

        time_sec = 10  # Set the time limit to 10 seconds

        # Start the timer generator
        timer_gen = timer(time_sec)
        timer_value = next(timer_gen)

        while x != guess:
            guess = input("Time left: {}   What music am I thinking of: ".format(timer_value))
            timer_value = next(timer_gen)  # Get the next timer value
            
            if x == guess:
                print("\nYou guessed {}. Congratulations, you got it!".format(guess))
                correct_guesses += 1
                break
            else:
                print("\nYou guessed {}. Unfortunately, you got the wrong answer!".format(guess))

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print("\nThanks for playing! You got {} correct guesses.".format(correct_guesses))

if __name__ == "__main__":
    main()
