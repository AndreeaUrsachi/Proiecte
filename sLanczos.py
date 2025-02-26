import os
import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import alg
import cv2
import numpy as np
import time
import csv
import pandas as pd
from statistics import mode
import plotly.express as px
import eigenfaces
import cv2
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
def interogare(poza_test, hqpb,media, proiectii, norma):
    poza_testV = np.reshape(poza_test,(-1,))
    poza_testV = poza_testV - media
    pr_test = np.dot(poza_testV,hqpb)
    pozitia = nn(proiectii.T,pr_test,norma)
    return pozitia

def nn(proiectii, pr_test, norma):
    nrProiectii = proiectii.shape[1]
    z = np.zeros(nrProiectii)

    for i in range(nrProiectii):
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




norme = [1, 2, 3, 4]
k = [20,40,60,80]

def genereaza_grafice(rr, tmi, tp):
    # Graficul Ratei de Recunoaștere
    plt.figure(figsize=(10, 5))
    for norma in norme:
        plt.plot(k, rr[norma], marker='o', label=f'norma = {norma}')
    plt.title('Rata de Recunoaștere în Funcție de Normă și k')
    plt.xlabel('Norma')
    plt.xticks( norme)
    plt.ylabel('Rata de Recunoaștere')
    plt.legend(title='Valoarea lui k')
    plt.grid(True)
    plt.savefig("grafic_rr_Lanczos")
    plt.show()

    # Graficul Timpului Mediu de Interogare
    plt.figure(figsize=(10, 5))
    for norma in norme:
        plt.plot(k, tmi[norma], marker='o', label=f'norma = {norma}')
    plt.title('Timpul Mediu de Interogare în Funcție de Normă și k')
    plt.xlabel('Norma')
    plt.xticks( norme)
    plt.ylabel('Timp Mediu de Interogare (secunde)')
    plt.legend(title='Valoarea lui k')
    plt.grid(True)
    plt.savefig("grafic_tmi_Lanczos")
    plt.show()

    """#Graficul Timpului de preprocesare
    plt.figure(figsize=(10, 5))
    for norma in norme:
        plt.plot(k, tp[norma], marker='o', label=f'norma = {norma}')
    plt.title('Timpul de Preprocesare în Funcție de Normă și k')
    plt.xlabel('Norma')
    plt.xticks(norme)
    plt.ylabel('Timp de Preprocesare (secunde)')
    plt.legend(title='Valoarea lui k')
    plt.grid(True)
    plt.savefig("grafic_tp_Lanczos")
    plt.show()"""

def statistici(k):
    rr = {norma: [] for norma in norme}
    tmi = {norma: [] for norma in norme}
    tp = {norma: [] for norma in norme}
    suma_timp_aqt = 0
    procent = alg.nrPozaPers
    nrTotalTeste = A.shape[1]
    #print(nrTotalTeste)
    suma_timp = 0
    caleS = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala'
    for normaa in norme:
        for ks in k:
            contor = 0
            t0 = time.time()
            preprocesare(A, ks)
            t1 = time.time()
            durata = t1-t0
            suma_timp += durata
            for i in range(1, 41):
                for j in range(9, 11):
                    cale = caleS + f'\\s{i}\\{j}.pgm'
                    pozaTest = cv2.imread(cale,0)
                    pozaTestVec = np.array(pozaTest)
                    #print("norma: " + str(normaa)+" k: "+str(ks))
                    media, hqpb, proiectii = preprocesare(A, ks)
                    t2 = time.time()
                    i0 = interogare(pozaTestVec, media, hqpb, proiectii, normaa)
                    t3 = time.time()
                    #print(i0)
                    p0 = i0 // 8 + 1
                    print(f" Lanczos norma {normaa}, k {ks},Poza testată {j}, Persoana {i}, Predicție {p0}, Etichetă reală {i}")
                    #print(i0//eigenfaces.nrPozaPers)
                    if p0 == i:
                        contor += 1

                    d = t3 - t2
                    suma_timp_aqt += d
            #print(contor)
            rr[normaa].append(contor / 80)
            tmi[normaa].append(suma_timp_aqt / 80)
        tp[normaa].append(suma_timp / 80)
    cale_fisier = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\s_lanczos.csv'
    cale_fisier1 = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\s_lanczos1.csv'
    cale_fisier2 = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\s_lanczos2.csv'


    # Salvăm rezultatele într-un fișier CSV
    try:
        with open(cale_fisier, 'w', newline='') as file:
            writer = csv.writer(file)

            # Scriem titlurile coloanelor
            writer.writerow(['Timpul mediu de interogare'])
            writer.writerow([' ', 'norma', '1', '2', 'inf', 'cos'])
            writer.writerow(['k'])
            # Scriem timpul mediu de interogare
            for i,ks in enumerate(k):
                row = [ks] + [' '] + [tmi[norma][i] for norma in norme]
                writer.writerow(row)


        with open(cale_fisier1, 'w', newline='') as file:
            writer = csv.writer(file)

            # Scriem rata de recunoaștere
            writer.writerow(['Rata de recunoastere'])
            writer.writerow([' ', 'norma', '1', '2', 'inf', 'cos'])
            writer.writerow(['k'])
            for i,ks in enumerate(k):
                row = [ks] + [' '] + [round(rr[norma][i], 4) for norma in norme]
                writer.writerow(row)

        with open(cale_fisier2, 'w', newline='') as file:
            writer = csv.writer(file)

            # Scriem timpul de preprocesare
            writer.writerow(['Timpul de preprocesare'])
            writer.writerow([' ', 'norma', '1', '2', 'inf', 'cos'])
            writer.writerow(['k'])
            for i in k:
                row = [i] + [' '] + [round(tp[norma][0], 4) for norma in norme]
                writer.writerow(row)

        print("Salvarea în fișierul CSV a fost realizată cu succes.")
    except Exception as e:
        print(f"A apărut o eroare la salvarea fișierului: {e}")
    #genereaza_grafice(rr, tmi)
    return rr, tmi, tp

statistici(k)


rr1, tmi1, tp1 = statistici(k)
genereaza_grafice(rr1, tmi1,tp1)

