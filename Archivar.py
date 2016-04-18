

import wave
import struct
#Creacion de la clase que archiva el audio nuevo
class file:
    def __init__(self, frecuency, bits, nombre):
        self.frecuency = frecuency
        self.bits = bits
        self.nombre = nombre

    def archive(self, datos):
        out = wave.open(self.nombre+".wav", 'w')
        bytes = self.bits/8
        out.setparams((1, bytes, self.frecuency, 0, 'NONE', 'not compressed'))

        valor = []
        for i in range(0, len(datos)):
            packed_value = struct.pack('<h', datos[i])
            valor.append(packed_value)

        value_str = ''.join(valor)
        out.writeframes(value_str)
        out.close()