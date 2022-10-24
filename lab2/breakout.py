# File: Breakout.py
# Names: Issa Mohamed, Marco Caba-Acevedo
# Professor: Aaron Bauer
# Date: 10/6/21
# Class: CS 111

"""
This program (once you have finished it) implements the Breakout game.
"""
from connect4_pgl import GWindow, GOval, GRect, GTimer
import random
from dataclasses import dataclass

# Constants

GWINDOW_WIDTH = 360               # Width of the graphics window
GWINDOW_HEIGHT = 600              # Height of the graphics window
N_ROWS = 5                        # Number of brick rows
N_COLS = 10                       # Number of brick columns
BRICK_ASPECT_RATIO = 4 / 1        # Width to height ratio of a brick
BRICK_TO_BALL_RATIO = 3 / 2       # Ratio of brick width to ball size
BRICK_TO_PADDLE_RATIO = 2 / 3     # Ratio of brick to paddle width
BRICK_SEP = 4                     # Separation between bricks
TOP_FRACTION = 0.2                # Fraction of window above bricks
BOTTOM_FRACTION = 0.05            # Fraction of window below paddle
N_BALLS = 3                       # Number of balls in a game
TIME_STEP = 10                    # Time step in milliseconds
INITIAL_Y_VELOCITY = 3.0          # Starting y velocity downward
MIN_X_VELOCITY = 1.0              # Minimum random x velocity
MAX_X_VELOCITY = 3.0              # Maximum random x velocity
BRICK_COLORS = ["Red", "Orange",  # List of the colors for rows of bricks from
                "Green", "Cyan",  # top to bottom
                "Blue"]

# Derived constants

BRICK_WIDTH = (GWINDOW_WIDTH - (N_COLS + 1) * BRICK_SEP) / N_COLS
BRICK_HEIGHT = BRICK_WIDTH / BRICK_ASPECT_RATIO
PADDLE_WIDTH = BRICK_WIDTH / BRICK_TO_PADDLE_RATIO
PADDLE_HEIGHT = BRICK_HEIGHT / BRICK_TO_PADDLE_RATIO
PADDLE_Y = (1 - BOTTOM_FRACTION) * GWINDOW_HEIGHT - PADDLE_HEIGHT
BALL_SIZE = BRICK_WIDTH / BRICK_TO_BALL_RATIO

@dataclass()
class GameState:
    num_bricks: int = 0
    balls_left: int = 0
    ball_x_vel: float = 0
    ball_y_vel: float = 0
    update_timer: GTimer = None

def start_round(gw, game_state, update_fn):
    """initialize the round to start called update_fn once the user clicks the mouse"""
    if game_state.update_timer:
        game_state.update_timer.stop()
    def onclick(e):
        game_state.update_timer = gw.setInterval(update_fn, TIME_STEP)
        gw.eventManager.clickListeners.pop()
    gw.addEventListener("click", onclick)

def end_game(game_state):
    if game_state.update_timer:
        game_state.update_timer.stop()

def breakout():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    game_state = GameState()
    game_state.balls_left = N_BALLS - 1 # subtract off the first turn


    # CREATE THE PADDLE HERE (STEP 1)
    paddle = GRect(0, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle.setFilled(True)
    paddle.setColor("Black")
    gw.add(paddle)
    # remember to use the relevant constants compute above (PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def update_paddle(e):
        """function to update the paddle's location based on the mouse position"""
        # fill in the updated x and y locations of the paddle in the setLocation call below
        # the parameter e represents the mouse movement that triggered this update
        # you can use e.getX() to get the mouse's current x coordinate
        # FINISH THIS FUNCTION
        mouse_x_postion = e.getX()
        cutoff_point_of_window = GWINDOW_WIDTH - PADDLE_WIDTH
        if (cutoff_point_of_window > mouse_x_postion):
            paddle.setLocation(mouse_x_postion, PADDLE_Y)


    
    # make it so that update_paddle is called whenever the user moves the mouse
    gw.addEventListener("mousemove", update_paddle) 


    # CREATE THE BALL HERE (STEP 2)
    ball = GOval(GWINDOW_WIDTH / 2 ,GWINDOW_HEIGHT / 2, BALL_SIZE, BALL_SIZE)
    ball.setFilled(True)
    ball.setColor("Black")
    gw.add(ball) 
    game_state.ball_x_vel = random.uniform(MIN_X_VELOCITY, MAX_X_VELOCITY)
    #making the x vel 50/50 to left or right
    game_state.ball_x_vel = random.choice([1, -1]) * game_state.ball_x_vel
    game_state.ball_y_vel = INITIAL_Y_VELOCITY

    #set game_state.ball_x_vel and game_state.ball_y_vel


    # CREATE THE BRICKS HERE (STEP 4)
    # remember to update game_state.num_bricks appropriately
    # caluclating the Y-Coordinate of first brick row 
    brick_y_coordinate = (GWINDOW_HEIGHT / 2) - (N_ROWS * BRICK_SEP * BRICK_HEIGHT) 
    for row in range(N_ROWS):
        current_brick_color = BRICK_COLORS[row]
        brick_x_coordinate = BRICK_SEP
        for col in range(N_COLS):
            #creating the brick
            brick = GRect(brick_x_coordinate, brick_y_coordinate, BRICK_WIDTH, BRICK_HEIGHT)
            brick.setFilled(True)
            brick.setColor(current_brick_color)
            gw.add(brick)
            game_state.num_bricks = game_state.num_bricks + 1 
            
            brick_x_coordinate = brick_x_coordinate + BRICK_SEP + BRICK_WIDTH
        #updating the Y-Coordinate for the next row 
        brick_y_coordinate = brick_y_coordinate + BRICK_HEIGHT + BRICK_SEP

    


    # FILL IN THE CODE FOR THIS FUNCTION ACCORDING TO THE STEPS OUTLINED IN THE COMMENTS (STEPS 3 and 5)
    def update_ball():
        x_position = ball.getX()
        y_position = ball.getY()
        # condition 1: its gonna hit top or condtion 2: its gonna hit bottom
        if((y_position <= 0)):
            game_state.ball_y_vel = -game_state.ball_y_vel
        elif((y_position >= PADDLE_Y)):
            print(game_state.balls_left)
            game_state.balls_left = game_state.balls_left - 1
            if( game_state.balls_left == -1):
                end_game(game_state)
            else:
                ball.setLocation(GWINDOW_WIDTH / 2 ,GWINDOW_HEIGHT / 2)
             
             
        #condition 3: it hits left or condtion 4: it hits right
        if((x_position <= 0) or (x_position >= GWINDOW_WIDTH)): 
            game_state.ball_x_vel = -game_state.ball_x_vel
        ball.move(game_state.ball_x_vel,game_state.ball_y_vel)

        """
        function to update the ball's position and handle any collisions 
        with walls, paddle or bricks
        """
        
        # move the ball according to game_state.ball_x_vel and game_state.ball_y_vel

        # check if the ball has hit one of the side walls
        # if so, reverse the x velocity

        # check if the ball has hit the top (y is 0 at the top of the game window)
        # if so, reverse the y velocity

        # check if the ball has hit the bottom (y is GWINDOW_HEIGHT at the bottom of the game window)
        # if so
        #     if there are balls left
        #         decrease game_state.balls_left
        #         reset the ball to its starting location
        #         reset game_state.ball_x_vel and game_state.ball_y_vel
        #         call start_round with arguments gw, game_state, and update_ball
        #     else
        #         end the game by calling end_game(game_state)
        #         

        collider = check_collision(ball.getX(), ball.getY())
        if( collider != "None"):
            # Checking if equal to paddle
            if( collider == paddle):
                game_state.ball_y_vel = -game_state.ball_y_vel
            else:
                game_state.ball_y_vel = -game_state.ball_y_vel
                gw.remove(collider)
                game_state.num_bricks = game_state.num_bricks - 1 
                
                if( game_state.num_bricks == 0 ):
                    end_game(game_state)

                
        # if collider is not None, then the ball is colliding with the paddle or bricks
        #     if collider is the paddle, reverse the y velocity
        #     otherwise, the ball has hit a brick, remove it (gw.remove(collider)) and decrease the number of bricks

        # if there are no more bricks, end_game(game_state)


    # FINISH THIS FUNCTION (STEP 5)
    def check_collision(x, y):
        """
        use gw.getElementAt to check for collisions with the ball
        return the colliding element or None if there is no collision
        x, y are the coordinates of the ball's upper left corner
        """
        radius_of_ball_point = BALL_SIZE / 2
        # check the upper left corner
        elem = gw.getElementAt(x, y)
        if elem != None:
            return elem

        # check the upper right corner
        elem = gw.getElementAt(x+ (radius_of_ball_point * 2), y)
        if elem != None:
            return elem

        # check the lower left corner
        elem = gw.getElementAt(x, y + (2 * radius_of_ball_point))
        if elem != None:
            return elem

        # check the lower right corner
        elem = gw.getElementAt(x +(2 * radius_of_ball_point),(2 * radius_of_ball_point) + y)
        if elem != None:
            return elem
        return ("None")

    start_round(gw, game_state, update_ball)

if __name__ == "__main__":
    breakout()