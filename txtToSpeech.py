from gtts import gTTS
import os

text = input("Enter text to convert to speech=: ")

if text.strip():
    speech = gTTS(text=text, lang='en', slow=False)
    speech.save("voice.mp3")
    os.system("start voice.mp3")
else:
    print("❌ No text provided.")
