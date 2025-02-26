import glob, random
import cv2 as cv
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import swirl
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import PhotoImage
def main():

    fileS = rf'C:\Users\Andreea\Desktop\python\Filtre de Poze\poze'

    master = Tk()
    master.title("Procesare de imagini")
    var1 = IntVar()

    comboBox = ttk.Combobox(master, values=["1","2","3","4","5","6"],width=15)
    comboBox.grid(row=0,column=0)
    comboBox.set("Alege o poza")



    def selected():
        select = comboBox.get()
        if select == "Alege o poza" or not select.isdigit():
            return 1
        return int(select)

    def poza():
        file = r'C:\Users\Andreea\Desktop\python\Filtre de Poze\poze\1.jpg'
        if selected() == 1:
            file = fileS + r"\1.jpg"
        elif selected() == 2:
            file = fileS + r"\2.jpg"
        elif selected() == 3:
            file = fileS + r"\3.jpg"
        elif selected() == 4:
            file = fileS + r"\4.jpg"
        elif selected() == 5:
            file = fileS + r"\5.jpg"
        elif selected() == 6:
            file = fileS + r"\6.jpg"
        return file

    file = poza()
    img = Image.open(file)
    imgTk = ImageTk.PhotoImage(img)

    def actualizare(event=None):
        try:
            file = poza()
            img = Image.open(file)
            img = img.resize((400,300))
            imgTk = ImageTk.PhotoImage(img)
            label.config(image=imgTk)
            label.image = imgTk
        except Exception as e:
            print(f"Eroare la încărcarea imaginii: {e}")
            return

    comboBox.bind("<<ComboboxSelected>>", actualizare)
    label = Label(master, image=imgTk)
    label.grid(row=0, column=6, rowspan=10, sticky = "n")


    actualizare()


    def afisare_filtru(cvImg,lb):
        try:
            cvImgRGB = cv.cvtColor(cvImg,cv.COLOR_BGR2RGB)
            img_pil = Image.fromarray(cvImgRGB)
            img_pil = img_pil.resize((400, 300))
            imgTkk = ImageTk.PhotoImage(img_pil)
            lb.config(image=imgTkk)
            lb.image = imgTkk
        except Exception as e:
            print(f"Eroare la actualizarea imaginii procesate: {e}")

    def afiseaza_videoclip(video_path, lb):
        cap = cv.VideoCapture(video_path)
        if not cap.isOpened():
            print("Eroare la deschiderea videoclipului.")
            return

        def redare_cadru():
            ret, frame = cap.read()
            if ret :
                fram = cv.resize(frame,(400,300))
                frame_rgb = cv.cvtColor(fram, cv.COLOR_BGR2RGB)
                img_pil = Image.fromarray(frame_rgb)
                imgTkk = ImageTk.PhotoImage(img_pil)

                lb.config(image=imgTkk)
                lb.image = imgTkk

                lb.after(40, redare_cadru)
            else:
                cap.release()
        redare_cadru()


    label_filtru1 = Label(master)
    label_filtru1.grid(row=10, column=6,rowspan=10)

    label_filtru3 = Label(master,width=400,height=300,bg="light gray")
    label_filtru3.grid(row=10, column=6,rowspan=10)
    label_filtru3.grid_remove()

    label_filtru2 = Label(master)
    label_filtru2.grid(row=40, column=6,rowspan=10,sticky="s")

    def blurring():
        file = poza()

        value = 3

        slider.grid(row = 17,column = 0)
        value = slider.get()
        if value % 2 == 0:
            value = value + 1


        img = cv.imread(file)
        #cv.imshow('Original', img)

        blur = cv.GaussianBlur(img, (value,value),cv.BORDER_DEFAULT)
        #cv.imshow("Blur", blur)
        afisare_filtru(blur,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        cv.waitKey(0)

    def histograma_color():
        file = poza()
        image = cv.imread(file)
        #cv.imshow("Original", image)
        plt.figure("Histograma Color")
        plt.xlabel("Bins")
        plt.ylabel("Numar pixeli")
        culori = ('b', 'g', 'r')
        for i,col in enumerate(culori):
            color_his = cv.calcHist([image],[i],None,[256],[0,256])
            plt.plot(color_his,color=col)
            plt.xlim([0,256])
        #plt.show()
        plt.savefig("grafic")
        fileG = r'C:\Users\Andreea\Desktop\python\grafic.png'
        image = cv.imread(fileG)
        afisare_filtru(image,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()
        cv.waitKey(0)

    def colorSpace():
        file = poza()
        img = cv.imread(file)
        #cv.imshow("Original", img)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        #cv.imshow("Gray", gray)
        afisare_filtru(gray,label_filtru1)
        rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        afisare_filtru(rgb,label_filtru2)
        #cv.imshow("Rgb", rgb)
        label_filtru2.grid(row=40, column=6,rowspan=10,sticky="s")
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()
        cv.waitKey(0)

    def mirror():
        gray_scale = True
        file = poza()
        img = cv.imread(file)
        #cv.imshow("Original", img)
        mir = np.fliplr(img)
        #cv.imshow("Oglindita", mir)
        afisare_filtru(mir,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()
        cv.waitKey(0)

    def conturare():
        file = poza()
        img = cv.imread(file)
        #cv.imshow("Original", img)
        conturat = cv.Canny(img, 125, 170)
        #cv.imshow("Conturare", conturat)
        afisare_filtru(conturat,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()
        cv.waitKey(0)

    def swirll():
        file = poza()
        img = cv.imread(file)
        #cv.imshow('Original', img)
        h,w = img.shape[:2]
        cx = w // 2
        cy = h // 2
        max_amount = 20
        dist = min(h,w)/2
        angle = 0
        num_frames = 100
        delay = 50
        frames = []
        video_path = "swirl_effect.mp4"
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        fps = 25
        out = cv.VideoWriter(video_path,fourcc,fps,(w,h))
        for i in range(0,num_frames):
            amount = i*max_amount/num_frames
            result = swirl(img,center=(cx,cy),rotation=angle,strength=amount, radius=dist, preserve_range=True).astype(np.uint8)
            out.write(result)
        for i in range(0,num_frames):
            amount = (num_frames-i)*max_amount/num_frames
            result = swirl(img,center=(cx,cy),rotation=angle,strength=amount, radius=dist, preserve_range=True).astype(np.uint8)
            out.write(result)
        out.release()
        afiseaza_videoclip(video_path,label_filtru3)
        label_filtru2.grid_remove()
        label_filtru3.grid(row=10, column=6, rowspan=10)
        label_filtru1.grid_remove()
        slider.grid_remove()

    def heart():
        file = poza()
        """images = glob.glob(random.choice(file))
        random_image = random.choice(images)

        def coord(event,x,y,flags,param):
            if event == cv.EVENT_RBUTTONDOWN:
                print(f"Coord: x={x}, y={y}")
        # Original
        img = cv.imread(random_image)
        pts = np.array([[550,850],[248,530],[833,552]])
        pts.reshape((-1,1,2))
        img = cv.circle(img,(700,400),100,(0,0,255),200)
        img = cv.circle(img,(400,400),100,(0,0,255),200)
        img = cv.circle(img,(554,536),10,(0,0,255),20)
        img = cv.fillPoly(img,[pts],(0,0,255))
        cv.imshow("Inima", img)
        cv.setMouseCallback("Inima", coord)
        cv.waitKey(0)"""
        img = cv.imread(file)
        drawnig = False
        last_point = None
        def coord(event,x,y,flags,param):
            nonlocal drawnig,last_point
            if event == cv.EVENT_LBUTTONDOWN:
                drawing = True
                last_point = (x,y)
            elif event == cv.EVENT_MOUSEMOVE:
                if drawnig:
                    cv.line(img, last_point,(x,y),(0,0,255),2)
                    last_point = (x,y)
            elif event == cv.EVENT_LBUTTONUP:
                drawing = False
        cv.setMouseCallback("Desen", coord)
        afisare_filtru(img, label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def cartoon():
        file = poza()

        # Original
        img = cv.imread(file)
        #cv.imshow('Original', img)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        smooth = cv.medianBlur(gray,5)
        edge = cv.adaptiveThreshold(smooth,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9 ,9)
        color = cv.bilateralFilter(img,9,300,300)
        cartoonImg = cv.bitwise_and(color,color,mask = edge)
        #cv.imshow("Cartoon",cartoonImg)
        afisare_filtru(cartoonImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()
        cv.waitKey(0)

    def motion():
        file = poza()
        slider.grid(row=17, column=0)
        # Original
        img = cv.imread(file)
        #cv.imshow('Original', img)
        kernel_size = slider.get()
        kernel_h = np.zeros((kernel_size, kernel_size))
        kernel_h[int((kernel_size-1)/2),:] = np.ones(kernel_size)
        kernel_h /= kernel_size
        horizontal = cv.filter2D(img, -1,kernel_h)
        #cv.imshow("Motion", horizontal)
        afisare_filtru(horizontal,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)


    def crayon():
        file = poza()
        slider.grid_remove()
        # Original
        img = cv.imread(file)
        #cv.imshow('Original', img)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        inv_gray = 255-gray
        blurImg = cv.GaussianBlur(inv_gray,(101,101),0)
        inv_blur = 255-blurImg
        sketch = cv.divide(gray,inv_blur,scale=255.0)
        #cv.imshow("Crayon", sketch)
        afisare_filtru(sketch,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def glitch():
        file = poza()
        img = cv.imread(file)
        h,w = img.shape[:2]
        scale = 0.1
        small = cv.resize(img,(int(w*scale), int(h*scale)), interpolation=cv.INTER_LINEAR)
        pixelated = cv.resize(small,(w,h),interpolation=cv.INTER_NEAREST)
        afisare_filtru(pixelated,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()

    def ripple():
        file = poza()
        value = 10
        slider.grid(row=17,column=0)
        value = slider.get()
        img = cv.imread(file)
        rows,cols,_ = img.shape
        map_x = np.zeros_like(img[:, :, 0],dtype=np.float32)
        map_y = np.zeros_like(img[:, :, 0],dtype=np.float32)
        for i in range(rows):
            for j in range(cols):
                map_x[i,j] = j+value*np.sin(2*np.pi*i/100)
                map_y[i,j] = i+value*np.sin(2*np.pi*j/100)
        rippleImg = cv.remap(img,map_x,map_y,interpolation=cv.INTER_LINEAR)
        afisare_filtru(rippleImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def heatmap():
        file = poza()
        img = cv.imread(file)
        heatmapImg = cv.applyColorMap(img,cv.COLORMAP_JET)
        afisare_filtru(heatmapImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def sphere():
        file = poza()
        img = cv.imread(file)
        rows,cols,_ = img.shape
        map_x = np.zeros_like(img[:, :, 0],dtype=np.float32)
        map_y = np.zeros_like(img[:, :, 0],dtype=np.float32)
        center_x, center_y = cols / 2, rows / 2
        radius = min(center_x,center_y)
        for i in range(rows):
            for j in range(cols):
                dx, dy = j - center_x, i - center_y
                distance = np.sqrt(dx**2+dy**2)
                if distance < radius:
                    r = distance/radius
                    theta = np.arctan2(dy,dx)
                    map_x[i,j] = center_x + r * radius * np.cos(theta)
                    map_y[i,j] = center_y + r * radius * np.sin(theta)
                else:
                    map_x[i,j],map_y[i,j] = j, i
        sphereImg = cv.remap(img,map_x,map_y,interpolation=cv.INTER_LINEAR)
        afisare_filtru(sphereImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def inverted():
        file = poza()
        img = cv.imread(file)
        invertedImg = cv.bitwise_not(img)
        afisare_filtru(invertedImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)
        slider.grid_remove()


    def emboss():
        slider.grid_remove()
        file = poza()
        img = cv.imread(file)
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        embossed = cv.filter2D(img,-1,kernel)
        afisare_filtru(embossed,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)

    def pixelSorting():
        slider.grid_remove()
        file = poza()
        img = cv.imread(file)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        sortedImg = np.copy(img)
        for i in range(gray.shape[0]):
            sortedImg[i, :, 0] = np.sort(img[i, :, 0]) # sortez canalul albastru
            sortedImg[i, :, 1] = np.sort(img[i, :, 1]) # sortez canalul verde
            sortedImg[i, :, 2] = np.sort(img[i, :, 2]) # sortez canalul rosu
        afisare_filtru(sortedImg,label_filtru1)
        label_filtru2.grid_remove()
        label_filtru3.grid_remove()
        label_filtru1.grid(row=10, column=6, rowspan=10)


    slider = Scale(master, variable = var1, from_ = 1, to = 100, orient=HORIZONTAL)
    slider.grid(row = 17,column = 0)
    slider.grid_remove()

    button1 = Button(master, text="Blur",width=15, command=blurring).grid(row=1,column=0)
    button2 = Button(master, text="Histograma Color",width=15, command=histograma_color).grid(row=2,column=0)
    button3 = Button(master, text="Color Space",width=15, command=colorSpace).grid(row=3,column=0)
    button4 = Button(master, text="Mirror",width=15, command=mirror).grid(row=4,column=0)
    button5 = Button(master, text="Conturare",width=15, command=conturare).grid(row=5,column=0)
    button6 = Button(master, text="Swirl",width=15, command=swirll).grid(row=6,column=0)
    #button7 = Button(master, text="Inima",width=15, command=heart).grid(row=7,column=0)
    button8 = Button(master, text="Cartoon",width=15, command=cartoon).grid(row=7,column=0)
    button9 = Button(master, text="Motion",width=15, command=motion).grid(row=8,column=0)
    button10 = Button(master, text="Crayon",width=15, command=crayon).grid(row=9,column=0)
    button11 = Button(master, text="Glitch",width=15, command=glitch).grid(row=10,column=0)
    button12 = Button(master, text="Ripple",width=15, command=ripple).grid(row=11,column=0)
    button13 = Button(master, text="HeatMap",width=15, command=heatmap).grid(row=12,column=0)
    button14 = Button(master, text="Inverted",width=15, command=inverted).grid(row=13,column=0)
    button15 = Button(master, text="Saturation",width=15, command=emboss).grid(row=14,column=0)
    button16 = Button(master, text="Pixel Sorting",width=15, command=pixelSorting).grid(row=15,column=0)


    master.mainloop()

if __name__=="__main__":
    main()
