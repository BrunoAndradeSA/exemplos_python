# coding: windows-1252
import os
import cv2

# Importar arquivo XML
cv2path = os.path.dirname(cv2.__file__)
xml_name = 'haarcascade_frontalface_alt2.xml'
xml_path = os.path.join(os.path.join(cv2path, 'data'), xml_name)

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

        # Desenhar retangulo azul para deteção da face
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (500, 0, 0))

        # Visualizar
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) == ord('x'):
            break

# Desligar a webcam
cap.release()

#Fechar janela do vídeo
cv2.destroyAllWindows()