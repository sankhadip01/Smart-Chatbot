import speech_recognition as sr
import pyttsx3

# Initialize recognizer & TTS engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Basic response logic (replace with GPT API if you want)
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am your smart assistant chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I'm sorry, I didn't understand that. Can you please repeat?"

# Speak the text response
def speak(text):
    print(f"Bot: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

# Text input mode
def text_mode():
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        speak(response)
        if "bye" in user_input.lower():
            break

# Voice input mode
def voice_mode():
    while True:
        with sr.Microphone() as source:
            print("Listening... (Speak now)")
            audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio)
                print(f"You: {user_input}")
                response = get_response(user_input)
                speak(response)
                if "bye" in user_input.lower():
                    break
            except sr.UnknownValueError:
                speak("Sorry, I did not catch that.")
            except sr.RequestError:
                speak("Sorry, speech service is unavailable.")

# Main function to choose mode
def main():
    speak("Hi! Would you like to chat using text or voice?")
    mode = input("Choose mode (text/voice): ").lower()
    if mode == "text":
        text_mode()
    elif mode == "voice":
        voice_mode()
    else:
        print("Invalid mode selected. Exiting.")

if __name__ == "__main__":
    main()
