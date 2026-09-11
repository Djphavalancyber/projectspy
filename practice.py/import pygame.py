import pygame

class ChessGame:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()

    def display_board(self):
        self.screen.fill((255, 255, 255))  # Fill the screen with white
        for i in range(8):
            for j in range(8):
                color = (240, 217, 181) if (i + j) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(self.screen, color, pygame.Rect(j * 100, i * 100, 100, 100))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.display_board()
            self.clock.tick(60)
        pygame.quit()

# Example usage
game = ChessGame()
game.run()