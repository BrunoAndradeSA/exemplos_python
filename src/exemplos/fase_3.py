# coding: windows-1252
import os
import speech_recognition as sr
import time
from gtts import gTTS

def logar(texto):
    with open('historico.log', mode='a', encoding='windows-1252') as arquivo:
        arquivo.write(texto + '\n')

def falar(texto, idioma):
    if texto:
        logar('InfoxBot: {}'.format(texto))

        # Criar um objeto, que contém a sintexe do texto digitado, no idioma selecionado
        fala = gTTS(text=texto, lang=idioma, slow=False)

        # Nome do arquivo a ser salvo a partir do timestamp de execução
        nome_mp3 = str(time.time()).replace('.','')

        # Salvar a saída em um mp3 temporário
        fala.save("{}.mp3".format(nome_mp3))

        # Executar o mp3 que contém a sintetização da fala
        os.system("mpg123 {}.mp3".format(nome_mp3)) 

        # Remover o mp3 após a execução
        os.system("rm {}.mp3".format(nome_mp3))

def ouvir(idioma):
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        # Função para redução de ruído do microfone
        microfone.adjust_for_ambient_noise(source)

        microfone.dynamic_energy_threshold = False
        
        # Ouvir o microfone e armazenar na variável
        print("Fale agora...")
        audio = microfone.listen(source)

    try:
        # Tenta reconhecer a frase a partir do audio armazenado
        frase = microfone.recognize_google(audio, language=idioma)
    except:
        # Caso não consiga reconher uma frase, retornar uma frase informando
        frase = 'Desculpe, não consegui entender o que você falou.'

    logar('Usuário: {}'.format(frase))

    return frase


# Executar um loop infinito
executar = True

while executar:
    # Define o idioma a ser utiizado para sintetizar a fala
    idioma = 'pt-br'

    # Bot se apresenta e pergunta o nome do usuário
    falar('Olá! Eu me chamo InfoxBot! Qual o seu nome?', idioma)

    nome = ouvir(idioma)

    # Bot dá boas-vindas ao usuário, caso tenha entendido o nome
    if nome != 'Desculpe, não consegui entender o que você falou.':
        falar('Seja bem-vindo {}! Caso deseje encerrar a conversa, basta dizer sair, ou senão, continuar'.format(nome), idioma)
    

        resposta = ouvir(idioma)

        if resposta == 'sair':
            # Bot se despede do usuário e encerra o programa
            falar('Até mais {}'.format(nome), idioma)
            break
        else:
            # o Bot repetirá o que for dito
            while True:
                falar('{}, diga algo que eu irei tentar repetir.'.format(nome), idioma)

                fala = ouvir(idioma)

                if fala == 'sair':
                    falar('Até mais {}'.format(nome), idioma)
                    executar = False
                    break
                else:
                    falar('{}, você falou: {}'.format(nome, fala), idioma)
    else:
        continue