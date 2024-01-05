import keyboard

def tecla_pressionada(tecla):
    return keyboard.is_pressed(tecla)

def monitorar_tecla(tecla):
    tecla_apertada = False

    while True:
        if tecla_pressionada(tecla):
            tecla_apertada = True
        elif tecla_apertada:
            print(f"A tecla '{tecla}' foi solta")
            tecla_apertada = False

# Exemplo de uso:
tecla_monitorada = 'a'  # Substitua 'a' pela tecla que você deseja monitorar

monitorar_tecla(tecla_monitorada)
