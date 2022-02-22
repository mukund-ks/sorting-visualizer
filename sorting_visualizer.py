import pygame
import random
pygame.init()

class Drawing:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = 178,223,238
    FONT = pygame.font.SysFont('arial', 20)
    LARGE_FONT = pygame.font.SysFont('arial', 40)
    
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

def draw(draw_win, sorting_algo_name, ascending):
    draw_win.window.fill(draw_win.BACKGROUND_COLOR)
    
    title = draw_win.LARGE_FONT.render(f"{sorting_algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_win.BLACK)
    draw_win.window.blit(title, (draw_win.width/2 - title.get_width()/2, 5))
    
    controls = draw_win.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_win.BLACK)
    draw_win.window.blit(controls, (draw_win.width/2 - controls.get_width()/2, 55))
    
    sorting = draw_win.FONT.render("I - Insertion Sort | B - Bubble Sort ", 1, draw_win.BLACK)
    draw_win.window.blit(sorting, (draw_win.width/2 - sorting.get_width()/2, 85))
    
    draw_list(draw_win)
    pygame.display.update()

def draw_list(draw_win, color_positions={}, clear_background=False):
    li = draw_win.li
    
    if clear_background:
        clear_rect = (draw_win.SIDE_PADDING//2, draw_win.TOP_PADDING, draw_win.width - draw_win.SIDE_PADDING, draw_win.height - draw_win.TOP_PADDING)
        
        pygame.draw.rect(draw_win.window, draw_win.BACKGROUND_COLOR, clear_rect)
    
    for i,vl in enumerate(li):
        x = draw_win.start_x + i * draw_win.blk_width
        y = draw_win.height - (vl - draw_win.min_vl) * draw_win.blk_height
        
        color = draw_win.GRADIENT[i%3]
        
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_win.window, color, (x,y, draw_win.blk_width, draw_win.height))
    
    if clear_background:
        pygame.display.update()

def gen_starting_li(n, min_vl, max_vl):
    li = []
    
    for i in range(n):
        vl = random.randint(min_vl,max_vl)
        li.append(vl)
        
    return li

def bubble_sort(draw_win, ascending=True):
    li = draw_win.li
    
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            num1 = li[j]
            num2 = li[j+1]
            
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                li[j], li[j+1] = li[j+1], li[j]
                draw_list(draw_win,{j: draw_win.GREEN, j+1: draw_win.RED}, True)
                yield True
    return li

def main():
    run = True
    clock = pygame.time.Clock()
    
    n = 50
    min_vl = 0
    max_vl = 100
    
    li = gen_starting_li(n, min_vl, max_vl)
    sorting = False
    ascending = bool()
    
    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_gen = None
    
    draw_win = Drawing(800,600,li)
    
    while run:
        clock.tick(240) # increase this number to have the algorithm function at a higher speed.
        
        if sorting:
            try:
                next(sorting_algo_gen)
            except StopIteration:
                sorting = False
        else:
            draw(draw_win, sorting_algo_name, ascending)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                li = gen_starting_li(n, min_vl, max_vl)
                draw_win.set_list(li)
                sorting = False
                
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algo_gen = sorting_algo(draw_win, ascending)
            
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()
    
if __name__=='__main__':
    main()