import speech_recognition as sr
r = sr.Recognizer()
#r.recognize_google()
testaudio = sr.AudioFile('welcome.wav')

with testaudio as source:
    audio = r.record(source)
type(audio)

output = r.recognize_google(audio)
print (output)