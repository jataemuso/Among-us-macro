import keyboard
import threading

teclas_monitoradas = {}  # Dicionário para rastrear as teclas sendo monitoradas

def tecla_pressionada(tecla):
    return keyboard.is_pressed(tecla)

def monitorar_tecla(tecla, callback):
    tecla_apertada = tecla_pressionada(tecla)  # Verifica se a tecla está pressionada inicialmente

    while True:
        if tecla_apertada and not tecla_pressionada(tecla):
            callback(True)  # Chamada ao callback quando a tecla é solta
            tecla_apertada = False
        elif not tecla_apertada and tecla_pressionada(tecla):
            tecla_apertada = True

def quando_soltar(tecla_monitorada):
    def on_release(is_released):
        if is_released:
            print(f"A tecla '{tecla_monitorada}' foi solta")

    # Verifica se a tecla já está sendo monitorada
    if tecla_monitorada not in teclas_monitoradas:
        teclas_monitoradas[tecla_monitorada] = threading.Thread(target=monitorar_tecla, args=(tecla_monitorada, on_release))
        teclas_monitoradas[tecla_monitorada].start()


