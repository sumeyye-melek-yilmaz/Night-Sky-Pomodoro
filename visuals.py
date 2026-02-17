import pygame
import random
from settings import WIDTH, HEIGHT, GOLD, WHITE

class Star:
    def __init__(self):
        self.x = random.randint(10, WIDTH - 10)
        self.y = random.randint(10, HEIGHT - 200)
        self.size = random.randint(1, 3)

    def draw(self, screen):
        current_size = self.size + random.randint(-1, 1)
        pygame.draw.circle(screen, GOLD, (self.x, self.y), max(1, current_size))

def draw_ui(screen, time_str, star_count):
    font = pygame.font.SysFont("Verdana", 90)
    small_font = pygame.font.SysFont("Verdana", 20)
    
    # Zamanlayıcı
    text_surf = font.render(time_str, True, WHITE)
    screen.blit(text_surf, (WIDTH//2 - 120, HEIGHT//2 - 60))
    
    # Alt Bilgi
    info_surf = small_font.render(f"Kazanılan Yıldızlar: {'*' * star_count}", True, GOLD)
    screen.blit(info_surf, (30, HEIGHT - 50))