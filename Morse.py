# Import required libraries
import tkinter as tk
import tkinter.font
import RPi.GPIO as GPIO
import pygame.mixer
import time

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
}

# Initialize the mixer module for sound
pygame.mixer.init()

# GPIO setup for the Raspberry Pi
GPIO.setmode(GPIO.BCM)
LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to play a short beep sound
def play_dot_sound():
    # Replace with the path to your dot sound file
    sound = pygame.mixer.Sound('dot.wav')
    sound.play()

# Function to play a long beep sound
def play_dash_sound():
    # Replace with the path to your dash sound file
    sound = pygame.mixer.Sound('dash.wav')
    sound.play()

# Function to blink LED in Morse code
def blink_morse_code(word):
    for char in word:
        if char == ' ':
            time.sleep(3)  # Pause for 3 seconds between words
        else:
            morse_char = morse_code.get(char.upper(), '')
            for symbol in morse_char:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
                    play_dot_sound()  # Play a short beep
                    time.sleep(0.2)  # Duration of a dot
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on the LED
                    play_dash_sound()  # Play a long beep
                    time.sleep(0.8)  # Duration of a dash
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off the LED
                time.sleep(0.2)  # Gap between symbols
            time.sleep(0.4)  # Gap between characters

# Function to clean up GPIO and close the window
def close():
    GPIO.cleanup()  # Clean up GPIO resources
    pygame.mixer.quit()  # Quit the pygame mixer
    win.destroy()  # Close the GUI window

# Create the GUI window
win = tk.Tk()
win.title("LED SWITCHER")
myFont = tkinter.font.Font(family='Helvetica', size=14, weight='bold')

# Function to handle button click
def on_button_click():
    word = entry.get()  # Get the word from the text box
    blink_morse_code(word)

# Create a label for user instructions
label = tk.Label(win, text="Enter a word (max 12 characters):")
label.pack()

# Create an entry box for user input
entry = tk.Entry(win, width=20)
entry.pack()

# Create a button to trigger LED blinking
button = tk.Button(win, text="Blink Morse Code", command=on_button_click)
button.pack()

# Create an exit button to close the program
exitbutton = tk.Button(win, text='EXIT', font=myFont, command=close, bg="red", height=1, width=8)
exitbutton.pack()

# Handle window close event to perform cleanup
win.protocol("WM_DELETE_WINDOW", close)

# Start the GUI main loop
win.mainloop()
