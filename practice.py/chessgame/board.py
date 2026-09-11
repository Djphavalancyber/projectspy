import pygame

class Board:
    def __init__(self):
        pygame.init()
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.display = pygame.display.set_mode((900, 900))
        self.clock = pygame.time.Clock()
        self.setup_pieces()
        self.load_images()
        self.selected = None

    def draw_board(self):
            for i in range(8):
                for j in range(8):
                    colour = (255,255,255) if (i+j)%2==0 else (255,150,80)
                    rect = pygame.Rect(j*111, i*111, 111, 111)
                    pygame.draw.rect(self.display, colour, rect)  
                    if self.selected == (i,j):
                        pygame.draw.rect(self.display, (0, 255, 255), rect, 5)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click(event.pos)           
            self.draw_board() 
            self.draw_pieces()        
            pygame.display.update()  
            self.clock.tick(60)
           
    def setup_pieces(self):
        self.board[7] = ['wr','wn','wb','wq','wk','wb','wn','wr']
        self.board[6] = ['wp','wp','wp','wp','wp','wp','wp','wp']
        self.board[1] = ['bp','bp','bp','bp','bp','bp','bp','bp']
        self.board[0] = ['br','bn','bb','bq','bk','bb','bn','br']
    def load_images(self):
        self.images = {}
        pieces = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk', 'bp', 'br', 'bn', 'bb', 'bq', 'bk']
        for piece in pieces: 
                    path = 'C:/Users/admin/Downloads/Category_PNG chess pieces_Standard transparent - Wikimedia Commons_files/'
                    self.images[piece] = pygame.image.load(path + piece + '.png')    
                    self.images[piece] = pygame.transform.scale(self.images[piece], (90, 90))  
    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]                     
                if piece and piece in self.images:   
                    self.display.blit(self.images[piece], (j * 111+15, i * 111+15, 111, 111))
    selected_piece=None 
    running = True
    def on_click(self,pos):
        col = pos[0] // 111
        row = pos[1] // 111
        piece = self.board[row][col]
        if self.selected is None:
           if piece:
            self.selected=(row,col) 
        else:
           from_row , from_col = self.selected
           self.board[row][col]=self.board[from_row][from_col]
           self.board[from_row][from_col]=None
           self.selected = None

game = Board()
game.run()   

