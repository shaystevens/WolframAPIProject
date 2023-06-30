# Project Name: Voice Query - Wolfram Alpha

## Description

This Python project allows a user to ask a question verbally, have it transcribed to text, sent to the Wolfram Alpha API for processing, and then verbally delivers the answer back to the user. The project uses the Google Text-to-Speech (gTTS) library, the SpeechRecognition library, and the Wolfram Alpha API.

## Getting Started

### Dependencies

- Python 3.6 or later.
- Libraries: gTTS, speech_recognition, wolframalpha, and mpg123 player installed on the system.
- Internet connection (required by gTTS and Wolfram Alpha API)

### Installing

- Clone this repository to your local machine.
- Install the required libraries using pip:
```
pip install gTTS speech_recognition wolframalpha
```
- Make sure you have mpg123 player installed on your system for audio playback.

### Executing Program

- Replace 'WOLFRAM_APP_ID' in the `answer` function with your actual Wolfram Alpha app ID.
- Run the script:
```
python voice_query_wolfram.py
```
- Ask your question when you see 'Listening...' in the console.

## Functions

- `speak(text)`: Converts the input text into speech, saves it as an mp3 file, and plays the file.

- `listen()`: Listens to a user's speech input, converts it into text and returns the text. If it fails to recognize the speech, it returns `None`.

- `answer(query)`: Takes a string query as input, sends it to the Wolfram Alpha API, and speaks out the answer it receives.

## Author

Shay Stevens

June 2023

## Version History

* 0.1
    * Initial Release

## Acknowledgments

- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Wolfram Alpha API](https://products.wolframalpha.com/api/)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the LICENSE.md file for details.
