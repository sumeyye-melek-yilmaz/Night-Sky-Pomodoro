# main.py
import pygame
import sys
from settings import *
from timer import PomodoroTimer
from visuals import Star, draw_ui

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Professional Night Sky Pomodoro")
    clock = pygame.time.Clock()
    
    timer = PomodoroTimer()
    stars = []

    while True:
        screen.fill(DEEP_BLUE)
        
        # Olay Kontrolü
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    timer.toggle_pause()

        # Güncelleme
        timer.update()
        
        # Yıldız Mantığı: Her STAR_INTERVAL_SECONDS saniyede bir yıldız ekle
        needed_stars = timer.passed_seconds // STAR_INTERVAL_SECONDS
        while len(stars) < needed_stars:
            stars.append(Star())

        # Çizim
        for star in stars:
            star.draw(screen)
            
        draw_ui(screen, timer.get_remaining_str(), len(stars))
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()