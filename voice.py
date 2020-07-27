import speech_recognition #you need to download the library in computer first
words = input("Say something!\n").lower()

if "hello" in words:
    print("Hello to you too!")
elif "how are you" in words:
    print("I am well, thankds!")
elif "goodbye" in words:
    print("Goodbye to you too!")
else:
    print("Huh?")

#with speech recognition
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)
print("Google Speech Recofnition thinks you said: ")
print(recognizer.recognize_google(audio))

