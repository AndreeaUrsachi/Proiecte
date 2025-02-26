from statistics import mode
import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
import time
import csv
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import IntVar,Radiobutton,W, Label

nrPers = 40
nrPozaPers = 8
nrTestare = 2
rezolutie = 112 * 92
norma = 4
k=3


caleDS = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala'
def creareMatericeA(caleDS):
    A = np.zeros((rezolutie, nrPers*nrPozaPers))
    A_testare = np.zeros((rezolutie, nrPers * (nrPozaPers - nrTestare)))

    for i in range(1, nrPers + 1):
        caleFolder = caleDS + '\s' + str(i) + '\\'
        for j in range (1, nrPozaPers + 1):
            calePoza = caleFolder + str(j) + '.pgm'
            poza = cv2.imread(calePoza, 0)
            poza = np.array(poza)
            pozaVectorizata = np.reshape(poza, rezolutie)
            A[:, (i-1)*nrPozaPers+j-1] = pozaVectorizata
        #print(A[:,j-1])

    return A
A = creareMatericeA(caleDS)
#print(A)
caleDSTest = caleDS + rf'\s3\{10-nrTestare+1}.pgm'
pozaTest = cv2.imread(caleDSTest,0)
pozaTest = np.array(pozaTest)
pozaTestVec = np.reshape(pozaTest, rezolutie)


#algoritmul NN
def nn(A, pozaTestVec, norma):
    z = np.zeros(nrPers*nrPozaPers)
    for i in range(len(z)):
        if norma == 1:
            z[i] = np.linalg.norm(pozaTestVec - A[:, i], norma)
        if norma == 2:
            z[i] = np.linalg.norm(pozaTestVec - A[:, i], norma)
        if norma == 3:
            z[i] = np.linalg.norm(pozaTestVec - A[:, i], np.inf)
        if norma == 4:
            z[i] = 1 - (np.dot(A[:, i], pozaTestVec) / (np.linalg.norm(pozaTestVec) * np.linalg.norm(A[:, i])))
    idx = np.argmin(z)
    return idx

def knn(A, pozaTestVec, norma, k):
    if k == 1:
        return nn(A, pozaTestVec, norma)
    z = np.zeros(nrPers * nrPozaPers)
    for i  in range(len(z)):
        if norma == 1:
            z[i] = np.linalg.norm(pozaTestVec-A[:, i], norma)
        if norma == 2:
            z[i] = np.linalg.norm(pozaTestVec-A[:,i],norma)
        if norma == 3:
            z[i] = np.linalg.norm(pozaTestVec-A[:,i],np.inf)
        if norma == 4:
            z[i] =1- (np.dot(A[:,i],pozaTestVec)/(np.linalg.norm(pozaTestVec) * np.linalg.norm(A[:,i])))
    idx = np.argsort(z)
    idx_k = idx[:k]
    pers_k = idx_k // nrPozaPers + 1
    p0 = mode(pers_k)
    return (p0-1)*8


def apel():
    poz = knn(A, pozaTestVec, norma,k)
    folder_poza = poz // nrPozaPers + 1
    caleDSf = caleDS + '\s' + str(folder_poza) + '\\'
    i = random.randint(1,nrPozaPers)
    caleDS_final = caleDSf + str(i) + '.pgm'
    #print(caleDS_final)
    #print("")
    #print(rr())
    #img = cv2.imread(caleDS_final,0)
    return caleDS_final
#apel()
def testare():
    return caleDS + rf'\s3\{10-nrTestare+1}.pgm'
