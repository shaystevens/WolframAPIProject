__author__ = "Shay Stevens"
__date__ = "June 2023"

import speech_recognition as sr
from gtts import gTTS
import os
import wolframalpha

"""
This function utilizes the Google Text-to-Speech (gTTS) library to convert text input into speech.

Parameters
----------
text - String input.

"""
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")


"""
This function uses the SpeechRecognition library to convert spoken language into text.

Returns
-------
None - If voice was unrecognizable. 
query - A string that represents the recognized speech from the user.

"""
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-US')
            print(f'User said: {query}\n')
            return query
        except Exception as e:
            print('Could not recognize your voice. Please say it again.')
            return None


"""
This function takes a string query as input and uses the Wolfram Alpha API to get a response to the query.

Parameters
----------
query- String input.

"""
def answer(query):
    app_id = 'WOLFRAM_APP_ID'  # replace with your Wolfram Alpha app ID
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    try:
        answer = next(res.results).text
        print(f'Answer: {answer}')
        speak(answer)
    except StopIteration:
        print("No results from Wolfram Alpha.")
        speak("I am sorry, but I can't find the answer.")

if __name__ == "__main__":
    query = listen()
    if query:
        answer(query)
