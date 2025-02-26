import json
import random
import pickle
import nltk
from keras import Model
from nltk.stem import WordNetLemmatizer
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.layers import Input, Dense,Dropout
from tensorflow.keras.optimizers import SGD
import numpy as np
import pandas as pd

#nltk.download('wordnet')

file = "dataset.csv"
df = pd.read_csv(file)
intents = {"intents" : []}
for _,row in df.iterrows():
    disease = row['Disease']
    sympotms = row[1:].dropna().tolist() #elimina valorile NaN

    intent = {
        "tag" : disease,
        "patterns": sympotms,
        "responses": [f"The disease you might have is {disease}."]
    }
    intents["intents"].append(intent)


"""with open("intent.json", "w") as json_file:
    json.dump(intents,json_file, indent=4)"""

lemmatizer = WordNetLemmatizer()
words = []
classes = []
documents = []

ignore_letters = ["?", "!", ".", ","]

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])
words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#pregatim data pentru a antrena reteaua neuronala
dataset = []
template = [0]*len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns ]

    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(template)
    output_row[classes.index(document[1])] = 1
    dataset.append([bag,output_row])
random.shuffle(dataset)
dataset = np.array(dataset)

train_x = list(dataset[:, 0])
train_y = list(dataset[:, 1])



# Modelul squential merge foarte bine
"""model = Sequential()
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(learning_rate = 0.01, decay = 1e-6,
          momentum = 0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])
hist = model.fit(np.array(train_x),np.array(train_y),
                 epochs = 200, batch_size=5, verbose = 1)
model.save("ChatBot_model.h5")"""

#Modelul ANN, nu da rezultate foarte bune

input_layer = Input(shape=(len(train_x[0]),))
x = Dense(256, activation='relu')(input_layer)
x = Dropout(0.5)(x)
x = Dense(128,activation='relu')(x)
x = Dropout(0.5)(x)
output_layer = Dense(len(train_y[0]),activation='softmax')(x)
model = Model(inputs=input_layer, outputs = output_layer)

sgd = SGD(learning_rate = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
model.compile(loss = 'categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
hist = model.fit(
    np.array(train_x),
    np.array(train_y),
    epochs=200,
    batch_size=5,
    verbose=1
)
model.save("chatBotModel.h5")
print("Done!")
