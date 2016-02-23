import speech_recognition as sr
from os import path

def speechText():
    audioFile = "sample.wav"
    audio = path.join(path.dirname(path.realpath(__file__)), audioFile)
    recognizer = sr.Recognizer()
    with sr.WavFile(audio) as source:
        audio = recognizer.record(source) # read the entire WAV file

    # Google Speech Recognition
    try:
        transcribe = recognizer.recognize_google(audio).lower()
        textFile = open("input.txt",'w')
        textFile.write(transcribe)
        textFile.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
