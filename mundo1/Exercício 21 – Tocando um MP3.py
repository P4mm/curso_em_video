import pygame

# Inicializa o pygame
pygame.init()

# Carrega o arquivo MP3
pygame.mixer.music.load(r"C:\Users\User\Desktop\python_estudos\curso_em_video\mundo_1\smithsnroses-will-shock-me-alone-ac-dc-mp3.mp3")

# Reproduz o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa em execução até que a música termine
while pygame.mixer.music.get_busy():
    continue
