#Testado com playsound 1.2.2

# Imports para execução
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer

# get mic audio
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não consegui entender.")
        except sr.RequestError:
            speak("Função indisponível.")
    return said.lower()


# speak converted audio to text
def speak(text, language="pt"):
    tts = gTTS(text=text, lang=language)
    filename = "command.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)

    playsound.playsound(filename)
    # Try to play the sound using playsound, but print an error if it fails
    #try:
    #    playsound.playsound(filename)
    #except Exception as e:
    #    print(f"Erro ao tocar o som: {e}")

# function to respond to commands
def respond(text):
    print("Comando reconhecido: " + text)
    if "youtube" in text:
        speak("Pelo que devo pesquisar no Youtube?")
        keyword = getAudio()
        if keyword != "":
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Seguem os resultados encontrados no Youtube sobre {keyword}")
    elif "google" in text:
        speak("Pelo que devo pesquisar no Google?")
        keyword = getAudio()
        if keyword != "":
            url = f"https://www.google.com/search?q={keyword}"
            webbrowser.get().open(url)
            speak(f"Seguem os resultados encontrados no Google para {keyword}")
    elif "tempo" in text:
        speak("Para qual local devo pesquisar a previsão do tempo?")
        keyword = getAudio()
        if keyword != "":
            url = f"https://www.google.com/search?q={keyword}+tempo"
            webbrowser.get().open(url)
            speak(f"Segue a previsão do tempo para {keyword}")
    elif "wiki" in text or "wikipedia" in text or "wikipédia" in text:
        speak("Pelo que devo pesquisar na Wikipédia?")
        keyword = getAudio()
        if keyword != "":
            result = wikipedia.summary(keyword, sentences=3)
            speak(f"Segue o resultado encontrado para {keyword}")
            print(result)
            speak(result)
    elif "piada" in text:
        speak(pyjokes.get_joke(), "en")
    # Funcional somente fora de ambientes colaborativos
    elif "esvaziar lixeira" in text or "limpar lixeira" in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("A lixeira foi esvaziada.")
    elif "hora" in text or "horário" in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    # Para execução dentro do Colab, importar a(s) música(s)
    elif "reproduzir música" in text or "tocar música" in text:
        speak("Reproduzindo a(s) música(s) no diretório especificado...")
        music_dir = "C:\\Songs"  # add your music directory here..
        songs = os.listdir(music_dir)
        # counter = 0
        print(songs)
        playMusic(music_dir + "\\" + songs[0])
    elif "parar música" in text or "interromper música" in text:
        speak("Reprodução interrompida.")
        stopMusic()
    elif "sair" in text or "encerrar" in text:
        speak("Até a próxima!")
        exit()


# play music
def playMusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()


# stop music
def stopMusic():
    mixer.music.stop()


# let's try it
while True:
    print("Aguardando instruções")
    text = getAudio()
    respond(text)
