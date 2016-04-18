

import pyaudio
import wave


#Creacion de la clase que reproduce el audio nuevo
class play:
    def __init__(self, CHUNK):
        self.CHUNK = CHUNK

    def open(self, nombre):

        self.wf = wave.open(nombre+".wav", 'rb')
        sampwidth = self.wf.getsampwidth()
        channels = self.wf.getnchannels()
        rate = self.wf.getframerate()
        return (sampwidth, channels, rate, self.wf)

    def start(self, sampwidth, channels, framerate):
        self.p = pyaudio.PyAudio()
        self.stream=self.p.open(format=self.p.get_format_from_width(sampwidth),
                        channels=channels,
                        rate=framerate,
                        output=True)

    def play(self, archivodeaudio):
        data = archivodeaudio.readframes(self.CHUNK)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)

    def closed(self):

        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()