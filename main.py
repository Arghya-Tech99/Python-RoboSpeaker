import pyttsx3

def initialize_speaker():
        engine = pyttsx3.init()
        return engine

if __name__ == '__main__':
    speaker = initialize_speaker()

    print("-" * 42)
    print("Welcome to the Interactive Robo Speaker!")
    print("   Type 'exit' to quit the program.")
    print("-" * 42)

    speaker.say("Robo Speaker is ready.")
    speaker.runAndWait()

    while True:
            text_to_speak = input("Enter what you want me to speak: ")  # Get user input

            # Check for the exit condition (case-insensitive)
            if text_to_speak.lower() == "exit":
                speaker.say("Thank you for using Robo Speaker. Goodbye!")
                speaker.runAndWait()
                break  # Exit the infinite loop

            else:
                speaker.say(text_to_speak)
                speaker.runAndWait()

