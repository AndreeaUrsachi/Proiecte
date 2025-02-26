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


def preprocesare(A,k):
    B=A
    media = np.mean(A, axis=1)
    A = (A.T - media).T
    L = np.dot(A.T, A)
    d, V = np.linalg.eig(L)
    idx = np.argsort(d)
    idx_k = idx[-1:-k-1:-1]
    V = np.dot(A,V)
    V = V[:, idx_k]
    hqpb = V
    proiectie = np.dot(A.T,V)
    A = B
    return media,hqpb,proiectie
media,hqpb,proiectie = preprocesare(A,k)


def interogare(poza_test,k):
    poza_test = np.reshape(poza_test,(-1,))
    poza_test = poza_test - media
    poza_test = np.reshape(poza_test, rezolutie)
    pr_test = np.dot(poza_test,hqpb)
    pozitia = nn(proiectie.T,pr_test,norma)
    #print(pr_test.shape)
    return pozitia

#print(proiectie.shape)

def nn(A, pr_test, norma):
    z = np.zeros(len(A[0]))

    for i in range(0,len(z)):
        if norma == 1:
            z[i] = np.linalg.norm(pr_test - A[:, i], 1)
        elif norma == 2:
            z[i] = np.linalg.norm(pr_test - A[:, i], 2)
        elif norma == 3:
            z[i] = np.linalg.norm(pr_test - A[:, i], np.inf)
        elif norma == 4:
            z[i] = 1 - (np.dot(A[:, i], pr_test) / (np.linalg.norm(pr_test) * np.linalg.norm(A[:, i])))

    idx = np.argmin(z)
    return idx


caleDSTest = caleDS + r'\s3\9.pgm'

def apel():
    incercare = cv2.imread(caleDSTest,0)
    plt.imshow(incercare,cmap='gray')
    #plt.show()

    poza_test = cv2.imread(caleDSTest,0)
    poza_test = np.array(poza_test)
    poz = interogare(poza_test,k)
    caleDSF = caleDS + r'\s' + str((poz // nrPozaPers + 1)) + r'\\' + str((poz % nrPozaPers + 1)) + '.pgm'
    #print(caleDSF)
    img = cv2.imread(caleDSF,0)
    image = plt.imshow(img, cmap='gray')
    #plt.show()
    #print(interogare(poza_test))"""

    rows = 4
    cols = 5
    fig, axes = plt.subplots(rows, cols, figsize=(10, 8))
    fig.suptitle("20 Eigenfaces", fontsize=16)

    for i in range(k):
        eigenface = hqpb[:, i].reshape(112, 92)
        ax = axes[i // cols, i % cols]
        ax.imshow(eigenface, cmap='gray')
        ax.axis('off')
        ax.set_title(f'Eigenface {i + 1}')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    #plt.show()
    return caleDSF


#apel()
def testare():
    return caleDS + rf'\s3\{10-nrTestare+1}.pgm'
