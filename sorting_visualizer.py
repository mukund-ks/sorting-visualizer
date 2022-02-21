import pygame
import random
pygame.init()

class Drawing:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = 178,223,238
    
    GRADIENT = [(159,121,238),(137,104,205),(93,71,139)]
    
    SIDE_PADDING = 100
    TOP_PADDING = 150
        
    def __init__(self, width, height, li):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption('Sorting Visualizer')
        self.set_list(li)
    
    def set_list(self, li):
        self.li = li
        self.min_vl = min(li)
        self.max_vl = max(li)
        
        self.blk_width = (self.width - self.SIDE_PADDING) // len(li)
        self.blk_height = (self.height - self.TOP_PADDING) // (self.max_vl - self.min_vl)
        self.start_x = self.SIDE_PADDING // 2

def draw(draw_win):
    draw_win.window.fill(draw_win.BACKGROUND_COLOR)
    draw_list(draw_win)
    pygame.display.update()

def draw_list(draw_win):
    li = draw_win.li
    
    for i,vl in enumerate(li):
        x = draw_win.start_x + i * draw_win.blk_width
        y = draw_win.height - (vl - draw_win.min_vl) * draw_win.blk_height
        
        color = draw_win.GRADIENT[i%3]
        
        pygame.draw.rect(draw_win.window, color, (x,y, draw_win.blk_width, draw_win.height))

def gen_starting_li(n, min_vl, max_vl):
    li = []
    
    for i in range(n):
        vl = random.randint(min_vl,max_vl)
        li.append(vl)
        
    return li

def main():
    run = True
    clock = pygame.time.Clock()
    
    n = 50
    min_vl = 0
    max_vl = 100
    
    li = gen_starting_li(n, min_vl, max_vl)
    
    draw_win = Drawing(800,600,li)
    
    while run:
        clock.tick(60)
        
        draw(draw_win)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
if __name__=='__main__':
    main()