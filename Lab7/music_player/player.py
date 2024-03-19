import pygame
import os

pygame.init()

scr = pygame.display.set_mode((400, 300))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

music_dir = '"C:\Users\Timur\Downloads"'
tracks = [os.path.join(music_dir, track) for track in os.listdir(music_dir) if track.endswith('.mp3')]
current_track = 0

button_width = 80
button_height = 40
buttons_start_x = 100
buttons_y = 250
button_gap = 100

def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def draw_buttons():
    pygame.draw.rect(scr, GREEN, (buttons_start_x, buttons_y, button_width, button_height))  # Play/Pause 
    pygame.draw.rect(scr, RED, (buttons_start_x + button_gap, buttons_y, button_width, button_height))  # Stop 
    pygame.draw.rect(scr, BLUE, (buttons_start_x + 2*button_gap, buttons_y, button_width, button_height))  # Next 
    pygame.draw.rect(scr, BLUE, (buttons_start_x - button_gap, buttons_y, button_width, button_height))  # Previous

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                play_music(tracks[current_track])
            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(tracks)
                play_music(tracks[current_track])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if buttons_start_x <= x <= buttons_start_x + button_width and buttons_y <= y <= buttons_y + button_height:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif buttons_start_x + button_gap <= x <= buttons_start_x + button_gap + button_width and buttons_y <= y <= buttons_y + button_height:
                stop_music()
            elif buttons_start_x + 2 * button_gap <= x <= buttons_start_x + 2 * button_gap + button_width and buttons_y <= y <= buttons_y + button_height:
                current_track = (current_track + 1) % len(tracks)
                play_music(tracks[current_track])
            elif buttons_start_x - button_gap <= x <= buttons_start_x - button_gap + button_width and buttons_y <= y <= buttons_y + button_height:
                current_track = (current_track - 1) % len(tracks)
                play_music(tracks[current_track])

    scr.fill((30, 30, 30))
    draw_buttons()
    pygame.display.flip()