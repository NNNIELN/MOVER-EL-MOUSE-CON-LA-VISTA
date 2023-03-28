#importamos nuestras librerias
import cv2
import mediapipe as mp
import pyautogui

#instalacion de la camara
camara = cv2.VideoCapture(0)
#colocacion de la malla
malla = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
pat_w, pat_h = pyautogui.size()
while True:
    _, frame = camara.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    elaboracion = malla.process(rgb_frame)
    puntos = elaboracion.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if puntos:
        #vamos referencias los puntos
        puntosreferencias = puntos[0].landmark
        for identificacion, referencia in enumerate(puntosreferencias[474:478]):
            x = int(referencia.x * frame_w)
            y = int(referencia.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0,0,255))
            if identificacion == 1:
                patalla_x = pat_w / frame_w * x
                patalla_y = pat_h / frame_h * y
                pyautogui.moveTo(patalla_x, patalla_y)
        izquierda = [puntosreferencias[145], puntosreferencias[159]]
        for referencia in izquierda:
            x = int(referencia.x * frame_w)
            y = int(referencia.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
        if (izquierda[0].y - izquierda[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(2)
    cv2.imshow('CONTROL DE MOUSE', frame)
    if cv2.waitKey(3) & 0xFF == ord('a'):
        break
