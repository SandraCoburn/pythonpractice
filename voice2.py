#Responds to a name
#https://pypi.org/project/SpeechRecognition

import re
import speech_recognition

#Obtain audio from the microphone
recognizer = speech_recognition.recognizer()
with speech_recognition.Microphone() as source:
    print("Say somehting")
    audio = recognizer.listen(source)

#Recognize speech using Google speech recognition
words = recognizer.recognize_google(audio)

#Respond to speech
matches = re.search("my name is (.*)", words) #it's searchin for this
if matches:
    print(f"Hey, {matches[1]}.")
else:
    print("Hey, you.")