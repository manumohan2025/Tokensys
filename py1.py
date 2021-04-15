from gtts import gTTS
from playsound import playsound
token = input ("Please enter a token number")
txt = "VLe numéro de jeton saisi est" + token
ob = gTTS(txt,lang='fr')
ob.save("token.mp3")
playsound("token.mp3")
