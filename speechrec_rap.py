# this is a tool for speechrecognition for rapsongs
# 
import speech_recognition as sr

def transcribe_music_file(filename):
    r = sr.Recognizer()

    with open(filename, "rb") as f:
        audio = f.read()

    try:
        transcript = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        transcript = ""

    return transcript

# add a song here 
if __name__ == "__main__":
    filename = "audio.wav"

    transcript = transcribe_music_file(filename)

    print(transcript)
