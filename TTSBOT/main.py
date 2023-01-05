import time
import pyttsx3
engine = pyttsx3.init()
f = open("Words.txt")
for word in f:
    time.sleep(0)
    engine.say(word)
engine.runAndWait()