pip install gTTS

# Texto para áudio

from gtts import gTTS
from IPython.display import Audio
import time

def textToAudio(text, language):
  gtts_object = gTTS(text = text,
                  lang = language,
                  slow = False)

  gtts_object.save("/content/gtts.wav")

texto = input("Digite o texto para ser convertido em áudio: ")
linguagem = input("Informe a sigla do idioma (pt, en, fr, etc.): ")
textToAudio(texto, linguagem)

# Reproduzir o áudio
Audio("/content/gtts.wav")
