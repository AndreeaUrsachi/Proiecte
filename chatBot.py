import json
import pickle
import random
import time

import nltk
import numpy as np
import pandas as pd
import pyttsx3
from nltk.stem import WordNetLemmatizer
#from tensorflow.keras.activations import load_model
from keras.src.saving.saving_api import load_model
import tensorflow as tf
lemmatizer = WordNetLemmatizer()
file = "dataset.csv"
df = pd.read_csv(file)

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model('ChatBot_model.h5')

def clean_up_sentence(sentence):
    return sentence.lower().split()

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    return [1 if word in sentence_words else 0 for word in words]

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    intent_index = np.argmax(res)
    return [{'intent' : classes[intent_index], 'probability': str(res[intent_index])}]

def get_response(intents_list, intents_json):
    if intents_list:
        return f" {intents_list[0]['intent']}"
    else:
        return "Sorry, I couldn't understand your symptoms. Could you please try again?"

with open("intents.json", "r") as file:
    intents = json.load(file)

def calling_the_bot(txt):
    global res
    predict = predict_class(txt)
    res = get_response(predict,intents)
    if 'no match' in [p['intent'] for p in predict]:
        return("sorry, I couldn't understand your symptoms")
    else:
        tag = predict[0]['intent']
        return("Found it. From our Database we found that you have " + res)
    print("\nResult found in our Database: ", res)
