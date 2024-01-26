import pyttsx3

text_to_speech = pyttsx3.init()

ans = input("What you want to convert to speech: ")
text_to_speech.say(ans)
text_to_speech.runAndWait()