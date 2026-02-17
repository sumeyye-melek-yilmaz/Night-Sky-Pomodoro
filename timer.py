# timer.py
import pygame
from settings import POMODORO_MINUTES

class PomodoroTimer:
    def __init__(self):
        self.total_seconds = POMODORO_MINUTES * 60
        self.passed_seconds = 0
        self.paused = True
        self.last_tick = pygame.time.get_ticks()

    def update(self):
        if not self.paused:
            now = pygame.time.get_ticks()
            if now - self.last_tick >= 1000:
                self.passed_seconds += 1
                self.last_tick = now
        else:
            self.last_tick = pygame.time.get_ticks()

    def get_remaining_str(self):
        remaining = max(0, self.total_seconds - self.passed_seconds)
        mins = remaining // 60
        secs = remaining % 60
        return f"{mins:02}:{secs:02}"

    def toggle_pause(self):
        self.paused = not self.paused