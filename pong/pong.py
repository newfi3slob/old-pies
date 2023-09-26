# Pong Project - recreates the game of Pong using classes and user-defined funcs.

import pygame

# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong Rough')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 
   
# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initializes a Game.
      # self is the game
      # surface is the window on which the game is displayed

      # === not game specific
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.font_size = 100
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.x_dim, self.y_dim = self.surface.get_size()  # gets window dimensions
      self.center = [(self.x_dim/2),(self.y_dim/2)]  # gets center of display
    
      # === game specific OBJECTS
      self.ball_speed = [4,1]
      self.y_dim = 0.425 * self.y_dim
      self.paddle_increment = 10
      self.max_score = 11
      self.left_count = 0
      self.right_count = 0  
      self.default_color = 'white'
      self.ball = Ball(self.default_color, 7,self.center, self.ball_speed,self.surface)
      self.leftpaddle = Paddle(0.2*self.x_dim,self.y_dim,10,50,self.default_color,self.surface)
      self.rightpaddle = Paddle(0.8*self.x_dim,self.y_dim,10,50,self.default_color,self.surface)
      self.left_rect = self.leftpaddle.get_rect()
      self.right_rect = self.rightpaddle.get_rect()
      self.ball_center = self.ball.get_center()
      self.ball_velocity = self.ball.get_velocity()
      self.ball_radius = self.ball.get_radius()
                    
   def play(self):
      # Play the game until the player presses the close box.
      while not self.close_clicked:
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
            self.game_Clock.tick(self.FPS)
            if self.left_count == self.max_score or self.right_count == self.max_score:
               self.continue_game = False  # freezes game when score target is met
         
   def scoreboard(self):
      # renders the scoreboard (text) to screen 
      
      #right_corner = 
      left_str = str(self.left_count)
      right_str = str(self.right_count)
      text_font = pygame.font.SysFont('', self.font_size)
      left_img = text_font.render(left_str, True, self.default_color)
      right_img = text_font.render(right_str, True, self.default_color)
      left_score = self.surface.blit(left_img, (0,0))
      right_score = self.surface.blit(right_img, (420,0))
      
   def scoreboard_update(self):
      # updates the scoreboards 'score' counts
      if self.ball_center[0] + self.ball_radius > self.surface.get_width():
         self.left_count += 1  # right edge
      elif self.ball_center[0] < self.ball_radius:
         self.right_count += 1  # left edge
      
   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         elif event.type == pygame.KEYDOWN:
            self.handle_key_down(event)
         elif event.type == pygame.KEYUP:
            self.handle_key_up(event)
            
   def handle_key_down(self,event):
      # response to KEYDOWN event
      if event.key == pygame.K_q:
         self.leftpaddle.set_vertical_velocity(-self.paddle_increment)
      elif event.key == pygame.K_a:
         self.leftpaddle.set_vertical_velocity(self.paddle_increment)
         
      if event.key == pygame.K_p:
         self.rightpaddle.set_vertical_velocity(-self.paddle_increment)
      elif event.key == pygame.K_l:
         self.rightpaddle.set_vertical_velocity(self.paddle_increment)      
   
   def handle_key_up(self,event):
      # response to KEYUP event
      if event.key == pygame.K_q:
         self.leftpaddle.set_vertical_velocity(0)  # stops paddle movement
      elif event.key == pygame.K_a:
         self.leftpaddle.set_vertical_velocity(0)
         
      if event.key == pygame.K_p:
         self.rightpaddle.set_vertical_velocity(0)
      elif event.key == pygame.K_l:
         self.rightpaddle.set_vertical_velocity(0)       

   def draw(self):
      # Draw all game objects.
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      self.leftpaddle.draw()
      self.rightpaddle.draw()      
      self.scoreboard()
      pygame.display.update() # make the updated surface appear on the display
      
   def collision_manager(self):
      # manages object collisions (paddle and ball)
      if self.left_rect.collidepoint(self.ball_center): 
         if self.ball_center[0] >= 100 and self.ball_velocity[0] < 0:
            self.ball_velocity[0] = -self.ball_velocity[0]
      elif self.right_rect.collidepoint(self.ball_center):
         if self.ball_center[0] >= 400 and self.ball_velocity[0] > 0:
            self.ball_velocity[0] = -self.ball_velocity[0]
      
   def update(self):
      # Update the game objects for the next frame (including collisions)
      self.ball.move()
      self.leftpaddle.move()
      self.rightpaddle.move()
      self.scoreboard_update()
      self.collision_manager()

   def decide_continue(self):
      # Check and remember if the game should continue
      pass
   
class Paddle:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the height of the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color(color)
      self.surface = surface
      self.vertical_velocity = 0  # paddle is not moving at the start
      
   def get_rect(self):  # GETS the rect dimensions of a paddle
      return self.rect

   def set_rect(self, new_rect):  # SETS the rect dimensions of a paddle
      self.rect = new_rect
      
   def draw(self):
      # -self is the Paddle object to draw
      pygame.draw.rect(self.surface,self.color,self.rect)
      
   def set_vertical_velocity(self,vertical_distance):
      # set the vertical velocity of the Paddle object
      # -self is the Paddle object
      # -vertical_distance is the int increment by which the paddle moves vertically
      self.vertical_velocity = vertical_distance
      
   def move(self):
      # moves the paddle such that paddle does not move outside the window
      # - self is the Paddle object
      self.rect.move_ip(0,self.vertical_velocity)
      if self.rect.bottom >= self.surface.get_height():   # change to bottom
         self.rect.bottom = self.surface.get_height()
      elif self.rect.top  <= 0:   # change to top
         self.rect.top = 0   
               
class Ball:
   # an object in this class represents a moving ball
   
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
      # initializes attributes of a ball
      
      self.color = pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
      
   def edge_manager(self):
      # manages the balls edge bounces (window edges)
      
      if self.center[0] + self.radius > self.surface.get_width():  # right
         self.velocity[0] = -self.velocity[0]   
      elif self.center[1] + self.radius > self.surface.get_height():  # bottom
         self.velocity[1] = -self.velocity[1]
      elif self.center[0] < self.radius:  # left
         self.velocity[0] = -self.velocity[0]
      elif self.center[1] < self.radius:  # top
         self.velocity[1] = -self.velocity[1]  
         
   def move(self):
       # Change the location of the ball by adding the corresponding 
       # speed values to the x and y coordinate of its center
      
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])  
      self.edge_manager()
      
   def get_center(self):  # used the get and set method to create
      return self.center  # the collision_manager for Game class
   
   def set_center(self,new_center):
      self.center = new_center
      
   def get_velocity(self):
      return self.velocity
   
   def return_velocity(self, new_velocity):
      self.velocity = new_velocity
      
   def get_radius(self):
      return self.radius
   
   def set_radius(self, new_radius):
      self.radius = new_radius
              
   def draw(self):
      # draws the ball on the surface
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)   

main()