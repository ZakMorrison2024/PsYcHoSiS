# system
import pygame
import asyncio
import sys
import os
# feature
import random
import time

# Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

# classes
class player(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","spr_player.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y

   def update(self):
           mx,my = pygame.mouse.get_pos()
           if mx > 470 :
                self.image = pygame.transform.flip(self.img_org,True,False)
           elif mx < 470:
                 self.image = self.img_org   
     
           #if self.rect.collidepoint(player.rect.centerx,player.rect.centery):

# light
class light(pygame.sprite.Sprite): 
   def __init__(self, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","spr_torch.png")))
      self.image = self.img_org # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y

   def update(self):
           mx,my = pygame.mouse.get_pos()
           if mx < 470 :
                self.image = pygame.transform.flip(self.img_org,1,0)
           elif mx > 470:
                 self.image = self.img_org
     
 
# people
class character_1(pygame.sprite.Sprite): 
   def __init__(self, startx, x, y, *groups): # Intialisation
      super().__init__(*groups) 
      self.img_org = [pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","spr_character1_1.png"))),
                      pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","spr_character1_2.png")))]
      self.img_monster = pygame.image.load(os.path.abspath(os.getcwd()+os.path.join("/imgs","spr_delusion.png")))
      self.image = self.img_org[0] # Set Default image
      self.rect = self.image.get_rect() # Set Colision Rectangle
      self.rect.x = x # Rect X
      self.rect.y = y # Rect Y
      self.index = 0

      self.sx = startx

      self.animation_time = 0.3
      self.current_time = 0

      self.animation_frames = 2
      self.current_frame = 1

   def update(self,dt):
                  
       mx,my = pygame.mouse.get_pos()

       self.current_time += dt
       if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.img_org)

       if self.rect.x < 470:
            if mx < 470:
                 self.image = self.img_org[self.index]
            elif mx > 470:
                 self.image = self.img_monster
       elif self.rect.x > 470:
             if mx > 470:
                 self.image = self.img_org[self.index]
             elif mx < 470:
                 self.image = self.img_monster
     
       if self.sx < 470:
            self.rect.x += 3
            self.image= pygame.transform.flip(self.image,True,False)

            if self.rect.x > 420:
                 if mx > 470:
                      kill = True # add loose function

            if self.rect.x > 960:
                 self.kill()

       elif self.sx > 470:
            self.rect.x -= 3

            if self.rect.x < 420:
                 if mx < 470:
                      kill = True # add loose function

            if self.rect.x < 0:
                 self.kill()  
                   

# set screen
size = (960, 540)
screen = pygame.display.set_mode(size)#, pygame.FULLSCREEN)

# caption
pygame.display.set_caption("PsYcHoSiS")

# Loop until the user clicks the close button.
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()#catch the jumping men

# Define objects

user = pygame.sprite.Group()
characters = pygame.sprite.Group()

item = light(0,60,user)
protagontist = player(435,440,user)
npc = character_1(0,0,440,characters)


# main program
async def main():
     while True:
# -------- Main Program Loop -----------
    # --- Main event loop
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      pygame.quit()
                      sys.exit()


# Drawing

           screen.fill(BLACK)
           user.draw(screen)
           characters.draw(screen)

           
           
# DT and Clock tick
           dt = clock.tick(60)/1000
# update
           user.update()
           characters.update(dt)
           

 
# Close the window and quit.

         
           pygame.display.flip()

           await asyncio.sleep(0)  # Very important, and keep it 0
 

asyncio.run(main())