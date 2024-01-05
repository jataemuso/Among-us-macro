import pyautogui
import time
import keyboard

# Mapeamento das teclas para as coordenadas
teclas = {
    'w': (151, 834),  # Preencha com as coordenadas corretas para o movimento para frente
    's': (157, 1006),  # Preencha com as coordenadas corretas para o movimento para trás
    'd': (247, 927),  # Preencha com as coordenadas corretas para o movimento para a direita
    'a': (73, 920),  # Preencha com as coordenadas corretas para o movimento para a esquerda
    'wd': (213, 846),  # Coordenadas para frente direita
    'sd': (214, 986),  # Coordenadas para baixo direita
    'sa': (89, 989),  # Coordenadas para baixo esquerda
    'aw': (84, 863),  # Coordenadas para cima esquerda
}

# Dicionário para rastrear o estado das teclas
teclas_press = {tecla: False for tecla in teclas}

def segura_tecla(tecla):
    global teclas_press
    coordenadas = teclas.get(tecla)
    
    # Verifica se é uma tecla composta
    if tecla == 'w':
        if teclas_press['d']:
            coordenadas = teclas.get('wd')
            teclas_press['s'] = False
        elif teclas_press['a']:
            coordenadas = teclas.get('aw')
            teclas_press['s'] = False
        else:
            teclas_press['s'] = True
            teclas_press['d'] = False
            teclas_press['a'] = False
            
    # Se for uma tecla composta, desliga as teclas simples
    if len(tecla) > 1:
        for key in teclas_press:
            if len(key) == 1 and key != tecla:
                solta_tecla(key)
    
    if coordenadas and not teclas_press[tecla]:
        teclas_press[tecla] = True
        pyautogui.mouseDown(*coordenadas)

def solta_tecla(tecla):
    global teclas_press
    coordenadas = teclas.get(tecla)
    
    # Verifica se é uma tecla composta
    if tecla == 'w':
        if teclas_press['d']:
            coordenadas = teclas.get('wd')
            teclas_press['s'] = False
        elif teclas_press['a']:
            coordenadas = teclas.get('aw')
            teclas_press['s'] = False
        else:
            teclas_press['s'] = False
            
    if len(tecla) > 1:
        teclas_press[tecla] = False
    elif coordenadas:
        teclas_press[tecla] = False
        pyautogui.mouseUp(*coordenadas)

for tecla in teclas:
    keyboard.on_press_key(tecla, lambda event, key=tecla: segura_tecla(key))
    keyboard.on_release_key(tecla, lambda event, key=tecla: solta_tecla(key))

keyboard.wait('esc')  # Espera até pressionar a tecla 'esc' para sair do loop
