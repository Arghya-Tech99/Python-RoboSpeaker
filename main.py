import pyttsx3 # Library for Text-to-Speech(TTS) conversion

if __name__ == '__main__':
    speaker = pyttsx3.init() # Initialize the TTS speaker

    print("Welcome to RoboSpeaker1.1. Created by Arghya")
    x = input("Enter what you want me to speak : ") # Whatever is entered will be assigned to x

    speaker.say(x) # Use the speaker
    speaker.runAndWait() # Wait for the speech to finish