import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Rojo tell me how may i help you")
def takeCommand():
    '''It takes microphone input and return
    string output''' 
    r = sr.Recognizer() 
    with sr.Microphone() as source : 
        print("Listening.....")
        r.pause_threshold = 1 #it help is adujst pause time before completing a sentence
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User ask for: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
if __name__ == "__main__": 
    wishme() 
    while True:

        query = takeCommand().lower()
        #logic for task complition
        if 'rojo' in query: #if speak rojo in query then it speak result from wikipedia
            speak("searching")
            query = query.replace("rojo", "") #it remove rojo from the final query that going to search
            result = wikipedia.summary(query, sentences = 2)  
            speak(result)
        elif 'open' in query:
            
            
            webbrowser.open('google.com')
