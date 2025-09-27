import pyttsx3 # Library for Text-to-Speech(TTS) conversion

if __name__ == '__main__': # Python program starts execution from here
    speaker = pyttsx3.init() # Initialize the TTS speaker
    print("Welcome to RoboSpeaker1.1. Created by Arghya")

    while True: # Speaker used as many times required; infinite while loop
        x = input("Enter what you want me to speak : ") # Whatever is entered will be assigned to x

        if x.lower() == "exit":
            speaker.say("Thank you for using RoboSpeaker1.1")
            speaker.runAndWait()
            break

        speaker.say(x)  # Use the speaker
        speaker.runAndWait()  # Wait for the speech to finish

