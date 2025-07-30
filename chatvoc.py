import nltk
import streamlit as st
from nltk.chat.util import Chat, reflections
import speech_recognition as sr
import speech_recognition as sr
import pyttsx3
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import speech_recognition as sr
import pyttsx3

# Dictionnaire des réponses pré-définies (simples)
reponses = {
    "bonjour": "Bonjour, comment puis-je vous aider ?",
    "solde": "Bien sûr, pouvez-vous me donner votre numéro de compte ?",
    "123456789": "Merci. Un instant pendant que je vérifie.",
    "merci": "Je vous en prie. Avez-vous besoin d'autre chose ?",
    "au revoir": "Au revoir et bonne journée !"
}

# Initialisation du moteur vocal
moteur = pyttsx3.init()
moteur.setProperty("rate", 150)

def parler(texte):
    print("Conseiller :", texte)
    moteur.say(texte)
    moteur.runAndWait()

def ecouter():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Client : (parlez...)")
        audio = r.listen(source)

    try:
        message = r.recognize_google(audio, language="fr-FR")
        print("Client :", message)
        return message.lower()
    except sr.UnknownValueError:
        parler("Désolé, je n'ai pas compris.")
        return ""
    except sr.RequestError:
        parler("Erreur de connexin au service de reconnaissance vocal.")
        return ""
    #Logique du chatbot
def repondre(message):
    if "bonjour" in message:
        return"Bonjour bienvenu chez notre service client. Comment puis je vous aider?"
    elif "Solde" in message:
       return "Pour connaitre votre solde, veillez communiquer votre numéro de compte, ou connecter vous à votre espace client et utiliser l'application mobile"
    elif "Crédit" in message:
       return "Nous proposons plusieurs types de crédits. Souhaitez vous en savoir sur le crédit à la consommation;le crédit logement, le crédit éauipementou le crédit wadial évènement des salariers,ou les crédits TPE  et PME des entrepreneurs "
    elif "au revoir" in message or "merci" in message:
       return "Merci de nous avoir contacter. Bonne journée !"
    else:
      return "Je n'ai pas bien compris. Pouvez vous reformuler votre question?"

    
     #Boucle de conversation
def conversation():
    parler("Bonjour, je suis votre conseiller virtuel. Que puis je faire pour vous? ")
    while True:
        message = ecouter()
        if message  == "":
            continue
        reponse = trouver_reponse(message)
        parler(reponse)
        if "au revoir" in message or "merci" in message:
            break
#Lancer le chatbot
if __name__ == "__main__":
    conversation()



