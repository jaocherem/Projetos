import face_recognition as fr
import cv2
import os
import numpy as np

"""
Olha todas as fotos da pasta e retorna os rostos que conseguir encontrar
"""

def getEncodedFaces():
    encoded = {}

    for dirpath, dirnames, filenames in os.walk("Face Recognition/faces"):
        for f in filenames:
            if f.endswith(".jpg"):
                face = fr.load_image_file("Face Recognition/faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    
    return encoded

faces = getEncodedFaces()
facesEncoded = list(faces.values())
knownFaceNames = list(faces.keys())

capture = cv2.VideoCapture(0)

while True:

    ret, frame = capture.read()

    """
    Procura por rostos pela webcam
    """

    faceLocations = fr.face_locations(frame)
    unknownFaceEncodings = fr.face_encodings(frame, faceLocations)
    faceNames = []

    """
    Compara os rostos que encontrou na webcam com os rostos da pasta
    """

    for face in unknownFaceEncodings:
        matches = fr.compare_faces(facesEncoded, face)
        name = "Desconhecido"

        faceDistances = fr.face_distance(facesEncoded, face)
        bestMatchIndex = np.argmin(faceDistances)

        if matches[bestMatchIndex]:
            name = knownFaceNames[bestMatchIndex]

        faceNames.append(name)

        """
        Desenha um retângulo no rosto que aparece na webcam e escreve o nome ou coloca como desconhecido
        """

        for (top, right, bottom, left), name in zip(faceLocations, faceNames):
            cv2.rectangle(frame, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
            cv2.putText(frame, name, (left - 10, bottom + 12), font, 0.65, (255, 255, 255), 2)

    cv2.imshow('Video', frame)

    """
    Clique 'x' para fechar o programa
    """

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

capture.release()
cv2.destroyAllWindows()

print(faceNames)