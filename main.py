import pyautogui
import keyboard
import threading

# Mapeamento das teclas para as coordenadas
teclas = {
    'w': (151, 834),  # Preencha com as coordenadas corretas para o movimento para frente
    's': (157, 1006),  # Preencha com as coordenadas corretas para o movimento para trás
    'd': (247, 927),  # Preencha com as coordenadas corretas para o movimento para a direita
    'a': (73, 920),  # Preencha com as coordenadas corretas para o movimento para a esquerda
}

def apertando(tecla):
    apertado = False
    while True:
        if keyboard.is_pressed(tecla):
            if not apertado:
                pyautogui.mouseDown(teclas[tecla])
                apertado = True 
        elif apertado:
            pyautogui.mouseUp()
            apertado = False

# Iniciar a verificação das teclas em threads separadas
threads = []
for direcao in ['w', 's', 'd', 'a']:
    thread = threading.Thread(target=apertando, args=(direcao,))
    threads.append(thread)
    thread.start()

# Aguardar as threads terminarem (isso vai manter o programa em execução)
for thread in threads:
    thread.join()
