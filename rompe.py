import pygame
import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
pygame.init()

WIDTH, HEIGTH = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Juego de Romper Bloques")
running = True

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence = 0.5,
                    min_tracking_confidence = 0.5,
                    max_num_hands = 1) as hands:
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Titulo CV2', frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()