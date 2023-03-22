from tkinter import *

import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

pygame.init() #iniciamos modulo de pygame
#Funcion boton abrir cancion
def abrirArchivo():
    cancion=filedialog.askopenfilename() #Guardar el nombre de la cancion
    print (cancion)
    pygame.mixer.music.load(cancion)
 


def playSong():
    pygame.mixer.music.play()
 

def stopSong():
    pygame.mixer.music.stop()

def pauseSong():
    pygame.mixer.music.pause()

def resumeSong():
    pygame.mixer.music.unpause()

def volumenUp():
    volumenLevel=pygame.mixer.music.get_volume()+0.5
    print(volumenLevel)
    pygame.mixer_music.set_volume
    (volumenLevel)

def volumenDown():
    volumenLevel=pygame.mixer.music.get_volume()-0.5
    print(volumenLevel)
    pygame.mixer_music.set_volume
    (volumenLevel)




raiz=Tk()
raiz.title("Reproductor MP3-GUI")
raiz.iconbitmap("pop.ico")
#flaticon.com PNG A ICO


raiz.geometry("800x500")
raiz.resizable(0,0)

#Crear Frame
framePrincipal=Frame (raiz, bg="#D4AADD")
framePrincipal.pack(fill="both", expand=1)

#Titulo reproductor 
tituloReproductor=Label(framePrincipal, text="Reproductor MP3-GUI",  font=("ROBOTO", 30, "bold"), bg="#D4AADD", fg="#fbfbfb")
tituloReproductor.place(relx=0.25, rely=0.4)

#BotonOpenSong 
botonOpenSong =Button(framePrincipal, text="Open  Song", fg="#000000", bg="#CD853F", font=("Roboto", 12, "bold"), width=10, height=2, command=abrirArchivo)
botonOpenSong.place(relx=0.1, rely=0.6)

#BotonPlay 
botonPlaySong =Button(framePrincipal, text="Play", fg="#000000", bg="#FA8072", font=("Roboto", 12, "bold"), width=10, height=2, command=playSong)
botonPlaySong.place(relx=0.25, rely=0.6)

#Botonstop
botonStopSong =Button(framePrincipal, text="Stop", fg="#000000", bg="#800000", font=("Roboto", 12, "bold"), width=10, height=2, command=stopSong)
botonStopSong.place(relx=0.4, rely=0.6)

#BotonResumeSong 
botonResumeSong =Button(framePrincipal, text="Resume", fg="#000000", bg="#2E8B57", font=("Roboto", 12, "bold"), width=10, height=2, command=resumeSong)
botonResumeSong.place(relx=0.55, rely=0.6)

#BotonPauseSong 
botonPauseSong =Button(framePrincipal, text="Pause", fg="#000000", bg="#F5FFFA", font=("Roboto", 12, "bold"), width=10, height=2, command=pauseSong)
botonPauseSong.place(relx=0.7, rely=0.6)

#BotonVolumenmasSong 
botonvolumenMas =Button(framePrincipal, text="Volumen +", fg="#000000", bg="#FF4500", font=("Roboto", 12, "bold"), width=10, height=2, command=resumeSong)
botonvolumenMas.place(relx=0.55, rely=0.8)

#VolumenmenosSong
botonvolumenMenos =Button(framePrincipal, text="Volumen -", fg="#000000", bg="#8B008B", font=("Roboto", 12, "bold"), width=10, height=2, command=pauseSong)
botonvolumenMenos.place(relx=0.25, rely=0.8)







raiz.mainloop()