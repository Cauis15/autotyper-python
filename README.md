# autotyper-python
Automação desenvolvida para contornar a limitação de campos web que bloqueiam a função de colar texto.

O script roda em segundo plano e aguarda um atalho de teclado global para executar a automação:

1. Captura do Texto (pyperclip): Lê o conteúdo que está armazenado na área de transferência do sistema (o último texto que você copiou com (Ctrl + C).
2. Tempo de Preparação (time): Dá uma pausa de 3 segundos para que o usuário clique no campo de texto onde deseja inserir o conteúdo.
3. Simulação de Digitação (pyautogui): Simula a digitação caractere por caractere com um intervalo configurável (interval=0.01), contornando limitações de campos que não aceitam colar texto diretamente.
4. Disparo por Atalho (keyboard): Monitora o sistema até que o atalho "Ctrl + Alt + D" seja pressionado para iniciar o processo.

pyperclip — Manipulação da área de transferência (Clipboard).
pyautogui — Automação de comandos de mouse e teclado.
keyboard — Monitoramento de atalhos globais do teclado.
time — Controle de tempo e pausas na execução.

Limitações: Não escreve acentos ou caracteres especiais.
