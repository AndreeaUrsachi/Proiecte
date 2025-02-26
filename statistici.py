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

norme = [1, 2, 3, 4]
ks = [1, 3, 5, 7, 9]

def genereaza_grafice(rr, tmi):
    # Graficul Ratei de Recunoaștere
    plt.figure(figsize=(10, 5))
    for norma in norme:
        plt.plot(ks, rr[norma], marker='o', label=f'norma = {norma}')
    plt.title('Rata de Recunoaștere în Funcție de Normă și k')
    plt.xlabel('Norma')
    plt.xticks( norme)
    plt.ylabel('Rata de Recunoaștere')
    plt.legend(title='Valoarea lui k')
    plt.grid(True)
    #plt.show()
    plt.savefig("grafic_rr_Knn.png")


    # Graficul Timpului Mediu de Interogare
    plt.figure(figsize=(10, 5))
    for norma in norme:
        plt.plot(ks, tmi[norma], marker='o', label=f'norma = {norma}')
    plt.title('Timpul Mediu de Interogare în Funcție de Normă și k')
    plt.xlabel('Norma')
    plt.xticks( norme)
    plt.ylabel('Timp Mediu de Interogare (secunde)')
    plt.legend(title='Valoarea lui k')
    plt.grid(True)
    #plt.show()
    plt.savefig("grafic_tmi_Knn.png")



def statistici():

    procent = alg.nrPozaPers
    rr = {norma: [] for norma in norme}  # Rata de recunoaștere pentru fiecare valoare de k
    tmi = {norma: [] for norma in norme}  # Timpul mediu de interogare
    nr_img_pers = alg.nrPozaPers+alg.nrTestare
    #print(nr_img_pers)
    nrTotalTeste = alg.A.shape[1]
    #print(nrTotalTeste)
    caleS  = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala'

    for normaa in norme:
        for k1 in ks:
            contor = 0
            for j in range(alg.nrPozaPers + 1, alg.nrTestare+alg.nrPozaPers+1):
                suma_timp = 0
                for i in range(1,alg.nrPers + 1):
                    cale = caleS+f'\\s{i}\\{j}.pgm'
                    pozaTest = cv2.imread(cale,0)
                    pozaTestVec = np.reshape(np.array(pozaTest),alg.rezolutie)
                    t0 = time.time()
                    i0 = alg.knn(alg.A,pozaTestVec, normaa,k1)
                    p0 = i0//8+1 #eticheta de clasa
                    #print(f"Poza testată {j}, Persoana {i}, Predicție {p0}, Etichetă reală {i}")
                    if p0 == i:
                        contor += 1
                    t1 = time.time()
                    durata = t1-t0
                    suma_timp = suma_timp +  durata
                    #print(contor)
                # Calculăm rata de recunoaștere și timpul mediu
            rr[normaa].append(contor / 80 )
            tmi[normaa].append(suma_timp / 80 )
            #print(f"Norma {normaa}, k={k1}: Rata recunoaștere={contor / 80}, Timp mediu={suma_timp / 80}")
    cale_fisier = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\rezultate_statistici.csv'
    cale_fisier2 = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\rezultate_statistici2.csv'


    # Salvăm rezultatele într-un fișier CSV
    try:
        with open(cale_fisier, 'w', newline='') as file:
            writer = csv.writer(file)

            # Scriem titlurile coloanelor
            writer.writerow(['Timpul mediu de interogare'])
            writer.writerow([' ', 'norma', '1', '2', 'inf', 'cos'])
            writer.writerow(['k'])
            # Scriem timpul mediu de interogare
            for i, k1 in enumerate(ks):
                row = [k1] +[' '] + [tmi[norma][i] for norma in norme]
                writer.writerow(row)


        with open(cale_fisier2, 'w', newline='') as file:
            writer = csv.writer(file)

            # Scriem rata de recunoaștere
            writer.writerow(['Rata de recunoastere'])
            writer.writerow([' ', 'norma', '1', '2', 'inf', 'cos'])
            writer.writerow(['k'])
            for i, k in enumerate(ks):
                row = [k] +[' '] + [round(rr[norma][i], 4) for norma in norme]
                writer.writerow(row)


        print("Salvarea în fișierul CSV a fost realizată cu succes.")
    except Exception as e:
        print(f"A apărut o eroare la salvarea fișierului: {e}")
    #genereaza_grafice(rr, tmi)
    return rr, tmi
#statistici()

rr1, tmi1 = statistici()

genereaza_grafice(rr1, tmi1)

