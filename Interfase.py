#Autores: Julian Guillermo Rodriguez, y Luis Yesid Sandival



from Tkinter import *
from Tkinter import Tk
from tkFileDialog import askopenfilename
import struct
import tkMessageBox
from Sumatorias import Iteraciones
from Archivar import file
import wave
from reproductor import play

def main():


    #Creacion de la ventana
    interfaz=Tk()

    interfaz.title("Reproductor de Audio")

    frame1 = Frame(interfaz)
    frame1.pack(side=TOP)
    frame2 = Frame(interfaz)
    frame2.pack(side=TOP)
    frame3 = Frame(interfaz)
    frame3.pack(side=TOP)
    frame4=Frame(interfaz)
    frame4.pack(side=TOP)
    frame5=Frame(interfaz)
    frame5.pack(side=TOP)


    #Arreglos para los archivos de audio
    global file1, file2, file3

    file1= []
    file2= []
    file3= []
    #Cargar achivo1
    def open1():

        global file1
        #Obtencion de la direccion del archivo
        direccion1= askopenfilename()
        #Abrir el archivo y obtencion del numero de frames
        archivo1=wave.open(direccion1, "rb")
        arreglo1=int(archivo1.getnframes())
        ##Combersion de binario a flotante
        for i in range(0, arreglo1):
            datos=archivo1.readframes(1)
            packed_value = struct.unpack('<h', datos)
            file1.append(packed_value)


    #Cargar archivo2
    def open2():

        global file2

        direccion2= askopenfilename()

        archivo2=wave.open(direccion2, "rb")
        arreglo2=int(archivo2.getnframes())

        for i in range(0, arreglo2):
            datos=archivo2.readframes(1)
            packed_value = struct.unpack('<h', datos)
            file2.append(packed_value)
    #Cargar archivo3
    def open3():

        global file3

        direccion3= askopenfilename()

        archivo3=wave.open(direccion3, "rb")
        arreglo3=int(archivo3.getnframes())



        for i in range(0, arreglo3):
            datos=archivo3.readframes(1)
            j = struct.unpack('<h', datos)
            file3.append(j)



    #Funsion pra cada tipo de reproduccion
    def sumatoria():
        #llamar a los arreglos de los tres archivos
        global file1, file2, file3
        #Seleccion de reproduccion monofonica
        if sel.get() == 1:


            #Vericar si se subieron los archivos e ingreso nombre
            if len(file1)==0 or len(file2)==0 or len(file3)==0 or Nombre.get()=='':
                tkMessageBox._show('Error', 'No ingreso todos los datos.\nCarge de nuevo los audios,\ne ingrese el nombre del archivo nuevo.')
                sel.set(0)

            else:
                #Verificar que cada archivo es de diferente tamano
                if len(file1)==len(file2) or len(file1)== len(file3) or len(file3)==len(file2):
                    tkMessageBox._show('Error','Los audios no pueden ser de igual duracion.\nCarge de nuevo los audios')
                else:
                    #Llamar a la clase Iteraciones
                    audio=Iteraciones(file1, file2, file3)
                    #llamar a la funcion Rsimultanea para que suenen los tres audios al tiempo
                    Naudio=audio.Rsimultanea()
                    #ajuste de volumen con la funcion niveldeaudio
                    val=audio.niveldeaudio(Volumen.get(), Naudio)
                    #archivar el nuevo audio
                    Narchivo=file(44100,16,Nombre.get())
                    Narchivo.archive(val)
        #Seleccion de reproducir una despues de otro
        if sel.get() == 2:


            if len(file1)==0 or len(file2)==0 or len(file3)==0 or Nombre.get()=='':
                tkMessageBox._show('Error', 'No ingreso todos los datos\nCarge de nuevo los audios,\ne ingrese el nombre del archivo nuevo.')
                sel.set(0)

            else:
                if len(file1)==len(file2) or len(file1)== len(file3) or len(file3)==len(file2):
                    tkMessageBox._show('Error','Los audios no pueden ser de igual duracion.\nCarge de nuevo los audios')
                else:

                    audio=Iteraciones(file1, file2, file3)
                    #llamar a la funcion Rcontinua para que suenen los tres audios uno despues de otro
                    Naudio=audio.Rcontinua()
                    val=audio.niveldeaudio(Volumen.get(), Naudio)
                    Narchivo=file(44100,16,Nombre.get())
                    Narchivo.archive(val)

        #Seleccion de reproduccion estereo
        if sel.get() == 3:


            if len(file1)==0 or len(file2)==0 or len(file3)==0 or Nombre.get()=='':
                tkMessageBox._show('Error', 'No ingreso todos los datos.\nCarge de nuevo los audios,\ne ingrese el nombre del archivo nuevo.')
                sel.set(0)

            else:
                if len(file1)==len(file2) or len(file1)== len(file3) or len(file3)==len(file2):
                    tkMessageBox._show('Error','Los audios no pueden ser de igual duracion.\nCarge de nuevo los audios')
                else:
                    #arreglo del audio final
                    Audiofinal=[]
                    audio=Iteraciones(file1, file2, file3)
                    #Llamar a la funcion Resterio1 para sumar el audio1 con el audio3
                    Naudio1=audio.Resterio1()
                    #Llamar a la funcion Resterio2 para sumar el audio2 con el audio3
                    Naudio2=audio.Resterio2()
                    val1=audio.niveldeaudio(Volumen.get(), Naudio1)
                    val2=audio.niveldeaudio(Volumen.get(), Naudio2)


                    out=wave.open(Nombre.get()+".wav", 'w')
                    out.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

                    a=len(val1)
                    b=len(val2)
                    #Comparar el tamano de los dos arreglos nuevos para el orden de las iteraciones
                    if a<b:
                        #Iteracion que reparte los dos nuevos audios entre derecha e izquierda
                        for i in range(0,a):
                            l = struct.pack('<h', val1[i])
                            r= struct.pack('<h', val2[i])
                            Audiofinal.append(l)
                            Audiofinal.append(r)
                        #Iteracion que acomoda el resto del audio restante
                        for i in range(a,b):
                            l = struct.pack('<h', 0)
                            r= struct.pack('<h', val2[i])
                            Audiofinal.append(l)
                            Audiofinal.append(r)
                    if b<a:
                        for i in range(0,b):
                            l = struct.pack('<h', val1[i])
                            r= struct.pack('<h', val2[i])
                            Audiofinal.append(l)
                            Audiofinal.append(r)
                        for i in range(b,a):
                            l= struct.pack('<h', val1[i])
                            r= struct.pack('<h', 0)
                            Audiofinal.append(l)
                            Audiofinal.append(r)

                    value_str=''.join(Audiofinal)
                    out.writeframes(value_str)
                    out.close()



    #Funcion para reproducir el audio nuevo
    def reproducir():
        #Verificar si selecciono un tipo de reproduccion
        if sel.get()==0:
            tkMessageBox._show('Error','No seleciono un tipo de reproduccion.\n Ingrese de nuevo todos los datos')
        else:
            #Llamar a la clase play que reproduce el audio
            sonido=play(1024)
            Datos=sonido.open(Nombre.get())
            sonido.start(Datos[0],Datos[1],Datos[2])
            sonido.play(Datos[3])
            sonido.closed()

    #Creacion de botones
    cuadro= Label(frame1, fg="black", padx=15, pady=10, text="Ingrese el nombre del archivo nuevo:")
    cuadro.pack(side=LEFT)

    sel=IntVar()

    Atiempo=Radiobutton(frame4,text='Reproduccion Monofonica',value=1,variable=sel,command=sumatoria)
    Atiempo.pack(side=LEFT)

    Serie=Radiobutton(frame4,text='Reproducir uno despues del otro',value=2,variable=sel,command=sumatoria)
    Serie.pack(side=LEFT)

    Estereo=Radiobutton(frame4,text='Reproduccion Estereofonica',value=3,variable=sel,command=sumatoria)
    Estereo.pack(side=LEFT)

    Nombre = Entry(frame1, bd=5, insertwidth=1)
    Nombre.pack(side=LEFT, padx=15, pady=10)


    Archivo1=Button(frame2, padx=30, pady=2,text="Cargar archivo 1",command=open1)
    Archivo1.pack(side=LEFT)

    Archivo2=Button(frame2, padx=30, pady=2,text="Cargar archivo 2",command=open2)
    Archivo2.pack(side=LEFT)

    Archivo3=Button(frame2, padx=30, pady=2,text="Cargar archivo 3",command=open3)
    Archivo3.pack(side=LEFT)

    Volumen= Scale(frame3, label='Volumen', orient=HORIZONTAL,width=10, length=250,from_=0,to=-20)
    Volumen.pack(side=TOP, padx=1,pady=1)

    Reproducir=Button(frame5,padx=30, pady=2,text="Reproducir",command=reproducir)
    Reproducir.pack(side=LEFT)



    interfaz.mainloop()

if __name__ == "__main__":
    main()