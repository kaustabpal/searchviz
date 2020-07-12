import pygame
import time
from video import make_video

class searchviz:
    pygame.init()
    clock = pygame.time.Clock()
    block_size=10
    w=block_size*50
    h=block_size*50
    gameDisplay = pygame.display.set_mode((w,h))
    save_screen = make_video(gameDisplay)

    def __init__(self,title):
        pygame.display.set_caption(title)
        self.unvisited = (255,255,255)
        self.black=(0,0,0)
        self.visited = (5, 43, 104)
        self.alive = (255,255,0)
        self.current = (30, 196, 15)
        self.dead = (2, 49, 56)
        self.textcol = (2, 49, 56)
        self.done = False
        self.start_x=4
        self.start_y=4
        self.x=self.start_x
        self.y=self.start_y
        self.nodes=[]
        self.nodes.append([self.x,self.y])

    def update(self):
        pygame.display.update()
        # next(self.save_screen)
        # next(self.save_screen)
        # next(self.save_screen)

    def color(self, row=0, col=0,clr=(30, 196, 15)):
        start_x=row*self.block_size
        start_y=col*self.block_size
        self.gameDisplay.fill(clr, (start_x,start_y,self.block_size, self.block_size))

    def up(self):
        self.x=self.x
        if(self.y == 0):
            self.y=self.y
        else:
            self.y=self.y-1

    def down(self):
        self.x=self.x
        if(self.y == 9):
            self.y=self.y
        else:
            self.y=self.y+1

    def left(self):
        self.y=self.y
        if(self.x == 0):
            self.x=self.x
        else:
            self.x=self.x-1

    def right(self):
        self.y=self.y
        if(self.x == 9):
            self.x=self.x
        else:
            self.x=self.x+1

    def draw_grids(self):
        for y in range(0,self.h,self.block_size):
          for x in range(self.w):
            self.gameDisplay.fill(self.textcol, (x,y,1,1)) ## Horizontal lines for grids
        for x in range(0,self.w,self.block_size):
          for y in range(0, self.h):
            self.gameDisplay.fill(self.textcol, (x,y,1,1)) ## vertical lines for grids

    def color_visited(self):
        for i in range(len(self.visited)):
                self.color(self.visited[i][0],self.visited[i][1],(175,222,243))

    def color_dead(self):
        for i in range(len(self.dead)):
                self.color(self.dead[i][0],self.dead[i][1],(0,0,0))


    def capture_keyboard(self):
        ###### capturing keystrokes
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_q:
                self.done=True
            if(event.type == pygame.QUIT):
              self.done=True

    def paint_background(self,w=1028,h=600):
        self.gameDisplay.fill(self.unvisited, (0,0,w,h))

    def set_fps(self,rate=30):
        self.clock.tick(30)

    def step(self):
        self.set_fps(30)
        self.capture_keyboard()
        self.paint_background(self.w,self.h)
        self.color_visited()
        self.color_dead()
        self.color(self.x, self.y, clr=self.current)
        #self.draw_grids()
        self.update()
        if(self.done==True):
            pygame.quit()
        return self.done
