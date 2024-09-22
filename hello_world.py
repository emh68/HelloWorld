import pyttsx3

# Get user's name
name = input("What is your name? ")

# Initialize the speech synthesizer module
engine = pyttsx3.init()

# Print and speak output
engine.say(f"Hello, {name}! Would you like to play a game? ")
print(f"Hello,{name}! Would you like to play a game? ")
engine.runAndWait()
