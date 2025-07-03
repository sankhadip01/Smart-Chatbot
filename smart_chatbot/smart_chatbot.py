import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

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

def speak(text):
    print(f"Bot: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def text_mode():
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        speak(response)
        if "bye" in user_input.lower():
            break

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
#I imported two important Python libraries:
#speech_recognition for listening to voice
#pyttsx3 for making the bot speak
#I created a recognizer object to hear and understand what we say.
#I also created a text-to-speech engine so the bot can reply by speaking
#I made a simple function get_response().

#It checks the user’s input:
	#If you say ‘hello’, it replies Hello!
		#If you say ‘bye’, it says ‘Goodbye!’ and stops.
	#For anything else, it says it didn’t understand.
    
    # in the main() function:
#The bot asks you if you want to use text or voice.
#Depending on your choice, it runs text_mode() or voice_mode().”


