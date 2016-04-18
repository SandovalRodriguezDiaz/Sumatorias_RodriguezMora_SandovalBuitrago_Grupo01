#Autores: Julain Guillermo Rodriguez y Luis Yesid Sandoval


#numpy solo para ajustar el volumen del nuevo archivo de audio
#NO SE UTILIZA PARA LA SUMA DE LOS ARREGLOS
import numpy as np

#Creacion de la clase
class Iteraciones:
    def __init__(self, arreglo1, arreglo2, arreglo3):
        self.audio1 = arreglo1
        self.audio2 = arreglo2
        self.audio3 = arreglo3

    #Funcion para reproducir los tres audios al tiempo
    def Rsimultanea(self):
        #Arreglo para el nuevo audio
        audiofinal=[]

        frames1=len(self.audio1)
        frames2=len(self.audio2)
        frames3=len(self.audio3)
        #Comparacion del tamano de los audios para las iteraciones
        if frames1 < frames2 and frames1 < frames3:
            #Primera iteracion, empieza en 0 y termina en el arreglo mas pequeno
            for i in range(0, frames1):
                #Suma de los datos de los arreglos uno por uno, NO SE USA NUMPY
                dato1=self.audio1[i][0]+self.audio2[i][0]+self.audio3[i][0]
                audiofinal.append(dato1)
            #Comparar que audio es el siguiente mas paqueno
            if frames2 < frames3:
                #Segunda iteracion, empiza donde termino la iteracion anterior y termina en el siguiente arreglo mas chico
                for i in range(frames1, frames2):
                    dato2=self.audio2[i][0]+self.audio3[i][0]
                    audiofinal.append(dato2)
                #Tercera iteracion acomada el resto del audio mas grande
                for i in range(frames2, frames3):
                    audiofinal.append(self.audio3[i][0])

            if frames3 < frames2:

                for i in range(frames1, frames3):
                    dato2=self.audio2[i][0]+self.audio3[i][0]
                    audiofinal.append(dato2)

                for i in range(frames3, frames2):
                    audiofinal.append(self.audio2[i][0])

        if frames2 < frames1 and frames2 < frames3:

            for i in range(0, frames2):

                dato1=self.audio1[i][0]+self.audio2[i][0]+self.audio3[i][0]
                audiofinal.append(dato1)

            if frames1 < frames3:

                for i in range(frames2, frames1):
                    dato2=self.audio1[i][0]+self.audio3[i][0]
                    audiofinal.append(dato2)
                for i in range(frames1,frames3):
                    audiofinal.append(self.audio3[i][0])


            if frames3 < frames1:

                for i in range(frames2, frames3):
                    dato2=self.audio1[i][0]+self.audio3[i][0]
                    audiofinal.append(dato2)
                for i in range(frames3,frames1):
                    audiofinal.append(self.audio1[i][0])

        if frames3 < frames1 and frames3 < frames2:

            for i in range(0, frames3):

                dato1=self.audio1[i][0]+self.audio2[i][0]+self.audio3[i][0]
                audiofinal.append(dato1)

            if frames1 < frames2:

                for i in range(frames3, frames1):
                    dato2=self.audio1[i][0]+self.audio2[i][0]
                    audiofinal.append(dato2)
                for i in range(frames1,frames2):
                    audiofinal.append(self.audio2[i][0])

            if frames2 < frames1:

                for i in range(frames3, frames2):
                    dato2=self.audio1[i][0]+self.audio2[i][0]
                    audiofinal.append(dato2)
                for i in range(frames2,frames1):
                    audiofinal.append(self.audio1[i][0])


        #SE COMBIERTE A NUMPY PARA EL AJUSTE DE VOLUMEN
        audioval=np.asanyarray(audiofinal)

        return audioval
    #Funcion para crear el arreglo que suena un audio despues del otro
    def Rcontinua(self):
        #Suma lineal del los tres arreglos
        audiofinal=self.audio1+self.audio2+self.audio3
        #SE COMBIERTE A NUMPY PARA EL AJUSTE DE VOLUMEN
        audioval=np.asanyarray(audiofinal)

        return audioval
    #Funccion que crea el audio que sonara a la izquierda
    def Resterio1(self):
    #Se realiza el mismo procedimiento que se uso para que los audios suenen al tiempo
        audiofinal1=[]
        frames1=len(self.audio1)
        frames3=len(self.audio3)

        if frames1<frames3:
            for i in range(0, frames1):
                dato=self.audio1[i][0]+self.audio3[i][0]
                audiofinal1.append(dato)
            for i in range(frames1, frames3):
                audiofinal1.append(self.audio3[i][0])

        if frames3<frames1:
            for i in range(0, frames3):
                dato2=self.audio1[i][0]+self.audio3[i][0]
                audiofinal1.append(dato2)

            for  i in range(frames3, frames1):
                audiofinal1.append(self.audio1[i][0])
        #SE COMBIERTE A NUMPY PARA EL AJUSTE DE VOLUMEN
        audioval=np.asanyarray(audiofinal1)
        return audioval
    #Funccion que crea el audio que sonara a la derecha
    def Resterio2(self):
        audiofinal2=[]
        frames2=len(self.audio2)
        frames3=len(self.audio3)

        if frames2<frames3:
            for i in range(0, frames2):
                dato=self.audio2[i][0]+self.audio3[i][0]
                audiofinal2.append(dato)
            for i in range(frames2, frames3):
                audiofinal2.append(self.audio3[i][0])

        if frames3<frames2:
            for  i in range(0, frames3):
                dato2=self.audio2[i][0]+self.audio3[i][0]
                audiofinal2.append(dato2)

            for  i in range(frames3, frames2):
                audiofinal2.append(self.audio2[i][0])
        #SE COMBIERTE A NUMPY PARA EL AJUSTE DE VOLUMEN
        audioval=np.asanyarray(audiofinal2)
        return audioval




    #Funcion que ajusta el volumen del audio nuevo
    #AQUI ES DONDE SE UTILIZAN LOS ARREGLOS NUMPY, NUMCA SE USO NUMPY PARA LA SUMA DE LOS ARREGLOS
    def niveldeaudio(self, nivel, info):
                VaP=max(abs(info))
                valornivel=(10**(nivel/20.0))*((2**16)/2)
                valorajustado=valornivel/float(VaP)
                infoajustada=info*valorajustado
                return infoajustada


