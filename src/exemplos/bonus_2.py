# coding: windows-1252
import os
import cv2

# Busca dos arquivos XML de detecção do OpenCV
def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            print("O diretorio/arquivo {} encontra-se em: {}".format(name, root))
            return os.path.join(root, name)
    
    # Caso não encontre realizar busca recursiva
    return find(name, os.path.dirname(path))

# Importar arquivo XML
cv2path = os.path.dirname(cv2.__file__)
haar_path = find('haarcascades', cv2path)
xml_name = 'haarcascade_frontalface_alt2.xml'
xml_path = os.path.join(haar_path, xml_name)

# Inicializar o classificador
clf = cv2.CascadeClassifier(xml_path)

# Inicialiar a Webcam
cap = cv2.VideoCapture(0)

# Loop para leitura do conteúdo
while(not cv2.waitKey(20) & 0xFF == ord('q')):
        # Capturar proximo frame
        ret, frame = cap.read()

        # Converter para tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Classificar
        faces = clf.detectMultiScale(gray)

        # Desenhar retangulo
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))

        # Visualizar
        cv2.imshow('frame',frame)

# Desligar a webcam
cap.release()

#Fechar janela do vídeo
cv2.destroyAllWindows()