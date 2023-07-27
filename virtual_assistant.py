import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipediaapi

def initialize_virtual_assistant():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    return recognizer, engine

def listen_for_user_input(recognizer):
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    return audio

def recognize_user_input(recognizer, audio):
    try:
        user_input = recognizer.recognize_google(audio).lower()
        print("User: " + user_input)
        return user_input
    except sr.UnknownValueError:
        print("Assistant: I'm sorry, I didn't catch that. Can you please repeat?")
        return ""
    except sr.RequestError as e:
        print("Assistant: Oops! There was a problem with the service; {0}".format(e))
        return ""

def process_user_input(user_input):
    if "exit" in user_input:
        print("Assistant: Exiting the virtual assistant.")
        return False
    else:
        
        # Use the Wolfram Alpha API and Wikipedia API for answering queries

        client = wolframalpha.Client("7PLJJK-4QVWWJ6AVT")
        res = client.query(user_input)
        if res.success:
            print("Assistant: " + next(res.results).text)
        else:
            # If Wolfram Alpha doesn't have an answer, try Wikipedia
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page = wiki_wiki.page(user_input)
            if page.exists():
                print("Assistant: " + page.summary[:200] + "...")
            else:
                print("Assistant: I'm sorry, I don't know the answer.")
        return True

def run_virtual_assistant():
    recognizer, engine = initialize_virtual_assistant()
    print("AI-powered Virtual Assistant started.")
    while True:
        audio = listen_for_user_input(recognizer)
        user_input = recognize_user_input(recognizer, audio)
        if not process_user_input(user_input):
            break

if __name__ == "__main__":
    run_virtual_assistant()
