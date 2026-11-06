import time
import keyboard
import pyautogui
import pyperclip


def digitar_texto_copiado():
    # 1. Pega o texto que está atualmente na área de transferência (Clipboard)
    texto = pyperclip.paste()

    if not texto:
        print("Nenhum texto encontrado na área de transferência!")
        return

    print("Texto detectado! Prepare o cursor onde deseja digitar...")
    print("Você tem 3 segundos para clicar no local correto.")

    # 2. Dá um tempo pequeno para o usuário clicar na caixa de texto desejada
    time.sleep(3)

    print("Digitando...")
    # 3. Simula a digitação do texto de forma automatizada
    pyautogui.write(texto, interval=0.01)
    print("Digitação concluída!")


# Define o atalho de teclado (Exemplo: Ctrl + Alt + D) para disparar a função
keyboard.add_hotkey("ctrl+alt+d", digitar_texto_copiado)

print("Programa rodando... Selecione um texto, copie (Ctrl+C),")
print("e depois pressione 'Ctrl + Alt + D' para começar o processo.")

# Mantém o programa rodando em segundo plano
keyboard.wait()
