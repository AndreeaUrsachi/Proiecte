import tkinter.ttk
from tkinter import *

import PIL.Image
import numpy
from tkinter import Canvas
#import statistici
import alg
from PIL import Image, ImageTk
import cv2
from matplotlib import pyplot as plt
import tkinter.messagebox as msgbox
import os
import eigenfaces as e
import eign_rep as er
import lanczos as l
import matplotlib.image as mplt
import matplotlib.pyplot as plt


is_visible = False
vizibil = False

global cale
def main():
    master = Tk()
    master.title("Interfata")

    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()

    def apas_button():
        global is_visible
        if is_visible:
            frameK.grid_remove()
        else:
            frameK.grid(row = 6, column = 3)
            k_diferit()
        if var2.get() == 1:
            frameK.grid_remove()
            is_visible = not is_visible


    frameP = Frame(master)
    frameP.grid_remove()

    def afisare_poza():
        im = apeleaza_algoritm()  # Apel funcție pentru a obține poza
        caleT = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\s13\5.pgm' # Calea imaginii cerute

        if not os.path.exists(caleT):
            print(f"Fișierul '{caleT}' nu există sau calea este incorectă.")
            return

        imgT = cv2.imread(caleT, 0)  # Citește poza cerută
        if imgT is None:
            print(f"Nu s-a putut citi imaginea '{caleT}'.")
            return

        imT = Image.fromarray(imgT)  # Convertă în format Image
        imgtkT = ImageTk.PhotoImage(imT)  # ImageTk pentru poza cerută

        # Deschide fereastra pop-up pentru afișarea pozelor
        popup = Toplevel()
        popup.title("Poze")



        label3 = Label(popup, text="Poza cerută")
        label3.pack()

        label4 = Label(popup, image=imgtkT)
        label4.pack()

        label1 = Label(popup, text="Poza generată de algoritm")
        label1.pack()

        img = Image.fromarray(im)
        imgtk = ImageTk.PhotoImage(img)

        label2 = Label(popup, image=imgtk)
        label2.pack()



        popup.mainloop()

    def update_procent():
        if var2.get() == 1 or var2.get() == 2:
            if var1.get() == 1:
                alg.nrPozaPers = 6
                alg.nrTestare = 4
            elif var1.get() == 2:
                alg.nrPozaPers = 7
                alg.nrTestare = 3
            elif var1.get() == 3:
                alg.nrPozaPers = 8
                alg.nrTestare = 2
            elif var1.get() == 4:
                alg.nrPozaPers = 9
                alg.nrTestare = 1
        if var2.get() == 3:
            if var1.get() == 1:
                e.nrPozaPers = 6
                e.nrTestare = 4
            elif var1.get() == 2:
                e.nrPozaPers = 7
                e.nrTestare = 3
            elif var1.get() == 3:
                e.nrPozaPers = 8
                e.nrTestare = 2
            elif var1.get() == 4:
                e.nrPozaPers = 9
                e.nrTestare = 1
        if var2.get() == 4:
            if var1.get() == 1:
                er.nrPozaPers = 6
                er.nrTestare = 4
            elif var1.get() == 2:
                er.nrPozaPers = 7
                er.nrTestare = 3
            elif var1.get() == 3:
                er.nrPozaPers = 8
                er.nrTestare = 2
            elif var1.get() == 4:
                er.nrPozaPers = 9
                er.nrTestare = 1
        if var2.get() == 5:
            if var1.get() == 1:
                l.nrPozaPers = 6
                l.nrTestare = 4
            elif var1.get() == 2:
                l.nrPozaPers = 7
                l.nrTestare = 3
            elif var1.get() == 3:
                l.nrPozaPers = 8
                l.nrTestare = 2
            elif var1.get() == 4:
                l.nrPozaPers = 9
                l.nrTestare = 1


    def update_norma():
        if var2.get() == 1 or var2.get() == 2:
            if var3.get() == 1:
                alg.norma = 1
            elif var3.get() == 2:
                alg.norma = 2
            elif var3.get() == 3:
                alg.norma = 3
            elif var3.get() == 4:
                alg.norma = 4
        if var2.get() == 3:
            if var3.get() == 1:
                e.norma = 1
            elif var3.get() == 2:
                e.norma = 2
            elif var3.get() == 3:
                e.norma = 3
            elif var3.get() == 4:
                e.norma = 4
        if var2.get() == 4:
            if var3.get() == 1:
                er.norma = 1
            elif var3.get() == 2:
                er.norma = 2
            elif var3.get() == 3:
                er.norma = 3
            elif var3.get() == 4:
                er.norma = 4
        if var2.get() == 5:
            if var3.get() == 1:
                l.norma = 1
            elif var3.get() == 2:
                l.norma = 2
            elif var3.get() == 3:
                l.norma = 3
            elif var3.get() == 4:
                l.norma = 4

    def update_k():
        alg.k = int(options1.get())

    def apeleaza_algoritm():
        update_procent()
        update_norma()
        update_k()
        #1print(f"Algoritm selectat: {var2.get()}, Procent antrenare: {var1.get()}, Norma: {var3.get()}, K: {options1.get()}")
        cale = alg.apel()
        if var2.get() == 1:
            cale = alg.apel()
            print("Cale interfata1:" + str(cale))
        if var2.get() == 2:
            cale = alg.apel()
            print("Cale interfata2:" + str(cale))
        if var2.get() == 3:
            cale = e.apel()
            print("Cale interfata3:"+str(cale))
        if var2.get() == 4:
            cale = er.apel()
            print("Cale interfata4:"+str(cale))
        if var2.get() == 5:
            cale = l.apel()
            print("Cale interfata5: "+str(cale))
        im = cv2.imread(cale,0)
        return im


    def apelare_tot():
        im = apeleaza_algoritm()
        #(alg.nrPozaPers, alg.A)
        return im


    def deschide_fisier_csv():
        if var2.get() == 1:
            try:
                fisier_csv = 'rezultate_statistici.csv'  # Specifică calea către fișierul tău CSV
                fisier_csv2 = 'rezultate_statistici2.csv'
                os.startfile(fisier_csv)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv2)  # Deschide fișierul CSV în editorul implicit
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 2:
            try:
                fisier_csv = 'rezultate_statistici.csv'  # Specifică calea către fișierul tău CSV
                fisier_csv2 = 'rezultate_statistici2.csv'
                os.startfile(fisier_csv)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv2)  # Deschide fișierul CSV în editorul implicit
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 3:
            try:
                fisier_csv = 's_egn.csv'  # Specifică calea către fișierul tău CSV
                fisier_csv2 = 's_egn1.csv'
                fisier_csv3 = 's_egn2.csv'
                os.startfile(fisier_csv)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv2)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv3)
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 4:
            try:
                fisier_csv = 's_egn_rep.csv'  # Specifică calea către fișierul tău CSV
                fisier_csv2 = 's_egn_rep1.csv'
                fisier_csv3 = 's_egn_rep2.csv'
                os.startfile(fisier_csv)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv2)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv3)
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 5:
            try:
                fisier_csv = 's_lanczos.csv'  # Specifică calea către fișierul tău CSV
                fisier_csv2 = 's_lanczos1.csv'
                fisier_csv3 = 's_lanczos2.csv'
                os.startfile(fisier_csv)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv2)  # Deschide fișierul CSV în editorul implicit
                os.startfile(fisier_csv3)
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")


    def afiseaza_grafice():
        if var2.get() == 1:
            try:
                img1 = mplt.imread(r"CC:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_rr_Knn.png")
                plt.imshow(img1)
                plt.show()
                img2 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_tmi_Knn.png")
                plt.imshow(img2)
                plt.show()

            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide poza: {e}")
        if var2.get() == 2:
            try:
                img1 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_rr_Knn.png")
                plt.imshow(img1)
                plt.show()
                img2 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_tmi_Knn.png")
                plt.imshow(img2)
                plt.show()
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide poza: {e}")
        if  var2.get() == 3:
            try:
                img1 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_rr_Egn.png")
                plt.imshow(img1)
                plt.show()
                img2 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_tmi_Egn.png")
                plt.imshow(img2)
                plt.show()
            except Exception as e:
                msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 4:
                try:
                    img1 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_rr_EgnRep.png")
                    plt.imshow(img1)
                    plt.show()
                    img2 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_tmi_EgnRep.png")
                    plt.imshow(img2)
                    plt.show()
                except Exception as e:
                    msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")
        if var2.get() == 5:
                try:
                    img1 = mplt.imread(r"CC:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_rr_Lanczos.png")
                    plt.imshow(img1)
                    plt.show()
                    img2 = mplt.imread(r"C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\grafic_tmi_Lanczos.png")
                    plt.imshow(img2)
                    plt.show()
                except Exception as e:
                    msgbox.showerror("Eroare", f"Nu s-a putut deschide fișierul CSV: {e}")


    def k_diferit():
        if var2.get() == 2:  # K-NN
            options1["values"] = ['3', '5', '7', '9']
            options1.set('3')  # Setează valoarea implicită
        elif var2.get() in [3, 4, 5]:  # Eigenfaces, Eigenfaces cu RC, Lanczos
            options1["values"] = ['20', '40', '60', '80']
            options1.set('20')  # Setează valoarea implicită

    frameK = Frame(master)
    label4 = Label(frameK, text='K: ')
    options1 = tkinter.ttk.Combobox(frameK, width=10)
    options1.set('3')


    label4.grid(row = 0, column = 0)
    options1.grid(row = 0, column = 1)

    labelSpatiu = Label(master, text='')
    label1 = Label(master, text="DS poze")
    Radiobutton(master, text='60%antrenare, 40% testare', variable = var1, value = 1).grid(row=1, sticky = W)
    Radiobutton(master, text='70%antrenare, 30% testare', variable = var1, value = 2).grid(row=2, sticky = W)
    Radiobutton(master, text='80%antrenare, 20% testare', variable = var1, value = 3).grid(row=3, sticky = W)
    Radiobutton(master, text='90%antrenare, 10% testare', variable = var1, value = 4).grid(row=4, sticky = W)
    #Radiobutton(master, text='random', variable = var1, value = 5).grid(row=5, sticky = W)


    label2 = Label(master, text="Algoritmi:")
    Radiobutton(master, text='NN               ', variable=var2, value=1).grid(row = 1,column = 3)
    Radiobutton(master, text='K-NN             ', variable=var2, value=2, command=apas_button).grid(row = 2,column = 3)
    Radiobutton(master, text='Eigenfaces       ', variable=var2, value=3, command=apas_button).grid(row = 3,column = 3)
    Radiobutton(master, text='Eigenfaces cu RC', variable=var2, value=4, command=apas_button).grid(row = 4,column = 3)
    Radiobutton(master, text='Lanczos          ', variable=var2, value=5, command=apas_button).grid(row = 5,column = 3)

    label3 = Label(master,text='Norma')
    Radiobutton(master, text = 'Manhattan(1)', variable = var3, value = 1).grid(row = 1,column = 4)
    Radiobutton(master, text = 'Euclidian(2)', variable = var3, value = 2).grid(row = 2,column = 4)
    Radiobutton(master, text = 'Infinit(3)  ', variable = var3, value = 3).grid(row = 3,column = 4)
    Radiobutton(master, text = 'Cosinus(4)  ', variable = var3, value = 4).grid(row = 4,column = 4)



    """imgtk = numpy.array(apeleaza_algoritm())
    igmtk = plt.imshow(imgtk)
    label7 = Label(frameP, text="Poza gasita").grid(row = 0, column = 1)
    try:
        #label5 = Label(master, image = igmtk).grid(row = 20, column = 1)
        canvas = Canvas(frameP, width=400, height=400)
        canvas.grid(row=1,column=1)
        canvas_img = ImageTk.PhotoImage(image=PIL.Image.fromarray(imgtk))
        canvas.create_image(0,0,image=canvas_img)
    except Exception as e:
        print(f"Eroare: {e}")
    print(imgtk.shape)"""
    """plt.imshow(imgtk,cmap='gray')
    plt.show()"""

    def testare():
        caleT = r'C:\Users\Andreea\Desktop\python\Algoritmi Recunoastere Faciala\s3\5.pgm'
        if var2.get() == 1:
            caleT = alg.testare()
        if var2.get() == 2:
            caleT = alg.testare()
        if var2.get() == 3:
            caleT = e.testare()
        if var2.get() == 4:
            caleT = er.testare()
        if var2.get() == 5:
            caleT = l.testare()
        return caleT
    caleT = testare()

    imgT = cv2.imread(caleT,0)
    imT = Image.fromarray(imgT)
    imgtkT = ImageTk.PhotoImage(imT)
    label8 = Label(frameP, text="Poza ceruta").grid(row = 0, column = 0)
    label6 = Label(frameP, image = imgtkT).grid(row = 1, column = 0)

    button1 = Button(master, text = 'Seteaza', command = apelare_tot). grid(row = 15, column = 2)
    button2 = Button(master, text = 'Afiseaza', command=afisare_poza).grid(row = 15, column = 3)
    button3 = Button(master, text='statistici', command=deschide_fisier_csv).grid(row = 15, column = 4)
    button4 = Button(master, text='grafice', command=afiseaza_grafice).grid(row = 15, column = 5)

    label1.grid(row=0, column=0)
    labelSpatiu.grid(row=6,column=0)
    label2.grid(row=0, column=3)
    labelSpatiu.grid(row=14,column=0)
    label3.grid(row = 0, column = 4)
    master.mainloop()



if __name__ == "__main__":
    main()