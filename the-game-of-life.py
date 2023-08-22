import numpy as np
import random
import pygame

#dimensiones maximas ancho: 104, alto: 47

tablero = []
col = 500
fil = 500
cantidad = 0
generacion = 0
lista_personas = []


def crearTablero():
    global tablero
    global col
    global fil
  
    col = int(col/2)
    fil = int(fil/2)
    

    tablero = np.array([[" "] * col] * fil, dtype=object)
    
    


def ponerFichas(tot):
    global tablero
    global ficha
    for i in range(tot):
        i = random.randrange(0,len(tablero),1)
        a = random.randrange(0,len(tablero[0]),1)
        tablero[i][a] = ficha


        
        
def modificarPosiciones():
    global tablero
    global ficha
    fichas = ["+","·"]
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            celdas = 0
            if a > 0 and i > 0 and a < len(tablero[0])-1 and i < len(tablero)-1:
                if tablero[i][a-1] in fichas:
                    celdas += 1
            
               
                if tablero[i][a+1] in fichas:
                    celdas += 1
                
     
                if tablero[i+1][a] in fichas:
                    celdas += 1
                if tablero[i+1][a+1] in fichas:
                    celdas += 1
            
                if tablero[i+1][a-1] in fichas:
                    celdas += 1
                        
                if tablero[i-1][a] in fichas:
                    celdas += 1
    
                if tablero[i-1][a+1] in fichas:
                    celdas += 1
            
                if tablero[i-1][a-1] in fichas:
                    celdas += 1
          
            if tablero[i][a] == ficha:
                if celdas == 2 or celdas == 3:
                    tablero[i][a] = ficha
                else:
                    tablero[i][a] = "·"
           
            elif celdas == 3:
                    tablero[i][a] = "-"
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            if tablero[i][a] == "-":
                
                tablero[i][a] = ficha
            if tablero[i][a] == "·":
                tablero[i][a] = " "
#Nacimientos: cada celda muerta adyacente a exactamente tres vecinos vivos se convertirá en vivo en la próxima generación.
#Muerte por aislamiento: cada célula viva con uno o menos vecinos vivos morirá en la próxima generación.
#Muerte por hacinamiento: cada celda viva con cuatro o más vecinos vivos morirá en la próxima generación.
#Supervivencia: cada célula viva con dos o tres vecinos vivos permanecerá viva durante la próxima generación.

ficha = "+"
crearTablero()
#cantidad = int(input("Cuantas personas quieres en la simulacion?: "))
cantidad = int((col*fil)/2)
ponerFichas(cantidad)

continuar = True


pygame.init()
font = pygame.font.Font(None, int(col/5))  # Puedes elegir la fuente que desees

generacion_text = font.render(f"Gen: {generacion}", True, (0, 255, 0))
generacion_rect = generacion_text.get_rect()
generacion_rect.left = 0
generacion_rect.top = 0


personas = 0

personas_text = font.render(f"Vivos: {personas}", True, (0, 255, 0))
personas_rect = personas_text.get_rect()
personas_rect.left = 0
personas_rect.top = int(col/5)

pygame.display.set_caption("Juego de la vida")

NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
BLANCO = (255,255,255)
ROJO = (255, 0, 0)

#Pantalla = pygame.display.set_mode((1366,768))
Pantalla = pygame.display.set_mode((600,600))

def dibujarPuntos(matriz,color):
    desplazamientoPuntosX = Pantalla.get_width()/col
    desplazamientoPuntosY = Pantalla.get_height()/fil
  
    for i in range(len(matriz)):
        for a in range(len(matriz[i])):
            if matriz[i][a] == "+":
                pygame.draw.rect(Pantalla, color, (desplazamientoPuntosX*a,desplazamientoPuntosY*i,int(Pantalla.get_height()/col),int(Pantalla.get_height()/col)))
                #pygame.draw.circle(Pantalla, color, (desplazamientoPuntosX*a,desplazamientoPuntosY*i), 1)

Terminar = False
#Se define para poder gestionar cada cuando se ejecuta un fotograma
numeroNuevo = ""
numeroNuevo_text = font.render(f"Vivos: {numeroNuevo}", True, (0, 255, 0))
numeroNuevo_rect = numeroNuevo_text.get_rect()
numeroNuevo_rect.left = 0
numeroNuevo_rect.top = int(col/2.5)
continuar = True

listaVivos = []
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
        if Evento.type == pygame.QUIT:
            Terminar = True
        if Evento.type == pygame.KEYDOWN:
            if Evento.key == pygame.K_SPACE:
                continuar = True
                numeroNuevo = ""
                personas = 0
                generacion = 0
                lista_personas = []
                listaVivos = []
                #cantidad = int(input("Cuantas personas quieres en la simulacion?: "))
                cantidad = int((col*fil)/2)
                ponerFichas(cantidad)
            if Evento.key >= 48 and Evento.key <= 57:
                numeroNuevo += chr(Evento.key)
            if Evento.key == 8:
                numeroNuevo = numeroNuevo[:len(numeroNuevo)-1]
            if Evento.key == 13:
                continuar = True
                personas = 0
                generacion = 0
                cantidad = 0
                lista_personas = []
                col = int(numeroNuevo)
                fil = int(numeroNuevo)
                crearTablero()
                listaVivos = []
                #cantidad = int(input("Cuantas personas quieres en la simulacion?: "))
                cantidad = int((col*fil)/2)
                ponerFichas(cantidad)
                numeroNuevo = ""
               



    #---La lógica del juego
    
    if numeroNuevo == "" and continuar == True:
        modificarPosiciones()
        generacion += 1

    #time.sleep(0.1)
    #---Código de dibujo----
    Pantalla.fill(NEGRO)
    dibujarPuntos(tablero,ROJO)
    generacion_text = font.render(f"Gen: {generacion}", True, (0, 255, 0))

    personas = 0
    for i in range(len(tablero)):
        for a in range(len(tablero[i])):
            if tablero[i][a] == "+":
                personas += 1
    listaVivos.append(personas)
    if len(listaVivos) > 10:
        listaVivos.pop(0)
    if len(listaVivos) > 0 and listaVivos.count(listaVivos[0]) >= 5:
        continuar = False
    
    personas_text = font.render(f"Vivos: {personas}", True, (0, 255, 0))
    numeroNuevo_text = font.render(numeroNuevo, True, (0, 255, 0))
    Pantalla.blit(generacion_text,generacion_rect)
    Pantalla.blit(personas_text,personas_rect)
    Pantalla.blit(numeroNuevo_text,numeroNuevo_rect)
    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()

pygame.quit()

    

    
    
    
    
