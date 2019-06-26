# coding: windows-1252
import os
from gtts import gTTS

# Executar um loop infinito
while True:

    # Obter uma entrada de texto do terminal
    fala = input('Digite algo ou [X] para sair:')

    # Caso digitado X, sai do loop e encerra o programa
    if fala == 'X':
        break

    # Define o idioma a ser utiizado para sintetizar a fala
    idioma = 'pt-br'

    # Criar um objeto, que contém a sintexe do texto digitado, no idioma selecionado
    objeto_fala = gTTS(text=fala, lang=idioma, slow=False)

    # Salvar a saída em um mp3 temporário
    objeto_fala.save("fase_2.mp3")

    # Executar o mp3 que contém a sintetização da fala
    os.system("mpg123 fase_2.mp3") 

    # Remover o mp3 após a execução
    os.system("rm fase_2.mp3")