from statistics import mode
import cv2
import random
import numpy as np
from matplotlib import pyplot as plt
import time
import csv
import alg

nrPers = 40
nrPozaPers = 8
nrTestare = 2
rezolutie = 112 * 92
norma = 1
k=20

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




def preprocesare(A, k):
    m = rezolutie
    q = np.zeros((m, k + 2))
    media = np.mean(A, axis=1)
    A = (A.T - media).T

    q[:, 0] = np.zeros(m)
    q[:, 1] = np.ones(m)
    q[:, 1] = q[:, 1] / np.linalg.norm(q[:, 1])

    beta = 0
    alpha = 0
    for i in range(1, k):
        w = np.dot(A, np.dot(A.T, q[:, i])) - beta * q[:, i - 1]

        alpha = np.dot(w, q[:, i])
        w = w - (alpha * q[:, i])

        beta = np.linalg.norm(w)

        if beta != 0:
            q[:, i + 1] = w / beta

    HQPB = q[:, 2:]
    proiectie = np.dot(A.T, HQPB)
    return HQPB, media, proiectie

hqpb,media,proiectii = preprocesare(A, k)


def interogare(poza_test):
    poza_testVec = np.reshape(poza_test,(-1,))
    poza_testVec = poza_testVec - media
    poza_testVec = np.reshape(poza_testVec, rezolutie)
    pr_test = np.dot(poza_testVec,hqpb)
    pozitia = nn(proiectii.T,pr_test,norma)
    #print(pozitia)
    return pozitia

def nn(proiectii, pr_test, norma):
    z = np.zeros(len(A[0]))

    for i in range(0,len(z)):
        if norma == 1:
            z[i] = np.linalg.norm(pr_test - proiectii[:, i], 1)
        elif norma == 2:
            z[i] = np.linalg.norm(pr_test - proiectii[:, i], 2)
        elif norma == 3:
            z[i] = np.linalg.norm(pr_test - proiectii[:, i], np.inf)
        elif norma == 4:
            z[i] = 1 - (np.dot(proiectii[:, i], pr_test) / (np.linalg.norm(pr_test) * np.linalg.norm(proiectii[:, i])))

    idx = np.argmin(z)
    return idx


caleDSTest = caleDS + r'\s13\9.pgm'

def apel():
    incercare = cv2.imread(caleDSTest,0)
    plt.imshow(incercare,cmap='gray')
    #plt.show()

    poza_test = cv2.imread(caleDSTest,0)
    poza_test = np.array(poza_test)
    poz = interogare(poza_test)
    caleDSF = caleDS + r'\s' + str((poz // nrPozaPers+1)) + r'\\' + str((poz % nrPozaPers)) + '.pgm'
    print(caleDSF)
    img = cv2.imread(caleDSF,0)
    image = plt.imshow(img, cmap='gray')
    #plt.show()
    #print(interogare(poza_test))
    rows = 4
    cols = 5
    fig, axes = plt.subplots(rows, cols, figsize=(10, 8))
    fig.suptitle("20 Lanczos", fontsize=16)

    for i in range(k):
        eigenface = hqpb[:, i].reshape(112, 92)
        ax = axes[i // cols, i % cols]
        ax.imshow(eigenface, cmap='gray')
        ax.axis('off')
        ax.set_title(f'Lanczos {i + 1}')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    #plt.show()
    return caleDSF

#apel()
def testare():
    return caleDS + rf'\s3\{10-nrTestare+1}.pgm'
