# CS 111 FINAL PROJECT: CONNECT FOUR
# Orignal code from Breakout Lab by Aaron Bauer
# Modified and adapted for "Connect Four" Final Project by Issa Mohamed and Markus Gunadi 
import tkinter as tk
from tkinter import XView
from tkinter.constants import TRUE
from connect4_pgl import GWindow, GOval, GRect, GTimer
import random
from dataclasses import dataclass

class GameState:
    # Input Lists
    player_moves = [] 
    bot_moves = []
    open_spots = []
    is_game_active = [True]

def connectfour():
     # Making the Window and Grid
    gw = GWindow(600, 700)
    game_state = GameState()
    for row in range(6):
        for column in range(7):
            rect = GRect(column * 50 +100, row * 50 + 100, 50, 50)
            gw.add(rect)
            game_state.open_spots.append(rect)


    #Player Functions
    def click_action(e):
        if game_state.is_game_active[0] == True:
            gobj = gw.getElementAt(e.getX(), e.getY())
            if gobj: 
                if gobj.getColor() != "#FF0000" and gobj.getColor() != "#0000FF":
                    gobj_x_value = gobj.getX()
                    gobj_y_value = gobj.getY()
                    lowest_spot = gobj
                    for spot in game_state.open_spots:
                        current_spot_x_value = spot.getX()
                        current_spot_y_value = spot.getY()
                        if current_spot_x_value == lowest_spot.getX():
                            if current_spot_y_value > lowest_spot.getY():
                                lowest_spot = spot
                    gobj = lowest_spot
                    game_state.player_moves.append(gobj)
                    game_state.open_spots.remove(gobj)
                    gobj.setColor("#FF0000")
                    # Making the Player's Piece
                    player_piece = GOval(gobj.getX(), gobj.getY(), 50, 50)
                    player_piece.setFilled(True)
                    player_piece.setColor("#FF0000")
                    gw.add(player_piece)
                    print("Turn", len(game_state.player_moves))
                    print("player has", 21 - len(game_state.player_moves), "pieces left.")
                    if check_connect4(game_state.player_moves) == True:
                        game_state.is_game_active[0]= False
                        endgame("Player", "")
                    elif 21 - len(game_state.player_moves) < 0: 
                        game_state.is_game_active[0] = False
                        endgame("", "Bot")
                    else:
                        bot_action(gobj)
                    
                else:
                    print("This Spot Has Already Been Selected. Please Choose Another Spot.")
            else:
                print("Click Inside The Board!")

    # Checking Win Conditions:
    def check_connect4(list_of_moves):
        if len(list_of_moves) < 4:
            return False
        else:
            for piece in list_of_moves:
                # 3 to the left 
                piece_y_val = piece.getY()
                piece_x_val = piece.getX()
                piece_color = piece.getColor()
                left_one_x_val = piece_x_val - 50
                left_two_x_val = piece_x_val - 100
                left_three_x_val = piece_x_val - 150
                left_one_obj = gw.getElementAt(left_one_x_val,piece_y_val)
                left_two_obj = gw.getElementAt(left_two_x_val,piece_y_val)
                left_three_obj = gw.getElementAt(left_three_x_val,piece_y_val)
                if (left_one_obj and left_two_obj and left_three_obj):
                    if ( (left_one_obj.getColor() == piece_color) and (left_two_obj.getColor() == piece_color) and (left_three_obj.getColor() == piece_color)):
                                return True
                # 3 to the right
                right_one_x_val = piece_x_val + 50
                right_two_x_val = piece_x_val + 100
                right_three_x_val = piece_x_val + 150
                right_one_obj = gw.getElementAt(right_one_x_val,piece_y_val)
                right_two_obj = gw.getElementAt(right_two_x_val,piece_y_val)
                right_three_obj = gw.getElementAt(right_three_x_val,piece_y_val)
                if (right_one_obj and right_two_obj and right_three_obj):
                    if ( (right_one_obj.getColor() == piece_color) and (right_two_obj.getColor() == piece_color) and (right_three_obj.getColor() == piece_color)):
                                return True
                    # 3 above
                above_one_y_val = piece_y_val - 50
                above_two_y_val = piece_y_val - 100
                above_three_y_val = piece_y_val - 150
                above_one_obj = gw.getElementAt(piece_x_val,above_one_y_val)
                above_two_obj = gw.getElementAt(piece_x_val,above_two_y_val)
                above_three_obj = gw.getElementAt(piece_x_val,above_three_y_val)
                if (above_one_obj and above_two_obj and above_three_obj):
                    if ( (above_one_obj.getColor() == piece_color) and (above_two_obj.getColor() == piece_color) and (above_three_obj.getColor() == piece_color)):
                                return True
                    
                # 3 below
                below_one_y_val = piece_y_val + 50
                below_two_y_val = piece_y_val + 100
                below_three_y_val = piece_y_val + 150
                below_one_obj = gw.getElementAt(piece_x_val,below_one_y_val)
                below_two_obj = gw.getElementAt(piece_x_val,below_two_y_val)
                below_three_obj = gw.getElementAt(piece_x_val,below_three_y_val)
                if (below_one_obj and below_two_obj and below_three_obj):
                    if ( (below_one_obj.getColor() == piece_color) and (below_two_obj.getColor() == piece_color) and (below_three_obj.getColor() == piece_color)):
                                return True
                # 3 right diagonal down
                right_diag_one_obj = gw.getElementAt(right_one_x_val, below_one_y_val)
                right_diag_two_obj = gw.getElementAt(right_two_x_val, below_two_y_val)
                right_diag_three_obj = gw.getElementAt(right_three_x_val, below_three_y_val)
                if (right_diag_one_obj and right_diag_two_obj and right_diag_three_obj):
                    if ( (right_diag_one_obj.getColor() == piece_color) and (right_diag_two_obj.getColor() == piece_color) and (right_diag_three_obj.getColor() == piece_color)):
                                return True
                # 3 left diagonal down
                left_diag_one_obj = gw.getElementAt(left_one_x_val, below_one_y_val)
                left_diag_two_obj = gw.getElementAt(left_two_x_val, below_two_y_val)
                left_diag_three_obj = gw.getElementAt(left_three_x_val, below_three_y_val)
                if (left_diag_one_obj and left_diag_two_obj and left_diag_three_obj):
                    if ( (left_diag_one_obj.getColor() == piece_color) and (left_diag_two_obj.getColor() == piece_color) and (left_diag_three_obj.getColor() == piece_color)):
                                return True
        return False
    # How the game stops after a win or player runs out of pieces 
    def endgame(who_won, who_ran_out):
        print("Game Over.")
        if who_won == "Player":
            print('You Win!')
        elif who_won == "Bot":
            print( 'You Lose. Better Luck Next Time.')
        else:
            if who_ran_out == "Player":
                print("Player Has Run Out of Pieces.")
            elif who_ran_out == "Bot":
                print("Bot Has Run Out of Pieces.")


    # Bot's Turn   
    def bot_action(last_move):
        last_move_x_value = last_move.getX()
        intelligent_moves = {}
        intelligent_moves["middle_move"] = ""
        intelligent_moves["top_move"] = ""
        intelligent_moves["side_move"] = ""

        on_top_x_value = last_move_x_value
        on_left_x_value = last_move_x_value - 50
        on_right_x_value = last_move_x_value + 50
        on_middle_x_value = 250

        for spot in game_state.open_spots:
            current_spot_x_value = spot.getX()
            # first strategy: bot places a piece into the middle column 
            if current_spot_x_value == on_middle_x_value:
                intelligent_moves["middle_move"] = spot
            # second strategy: bot places a piece on top of the player's last piece to block in response to possibly block their vertical strategy 
            if current_spot_x_value == on_top_x_value:
                intelligent_moves["top_move"] = spot
            # third strategy: bot places a piece to the player's piece's side to block their possible horizontal strategy      
            if current_spot_x_value == on_left_x_value or current_spot_x_value == on_right_x_value:
                intelligent_moves["side_move"] = spot
        bot_move_options = []
        if intelligent_moves["middle_move"] != "":
            bot_move_options.append(intelligent_moves["middle_move"])
        if intelligent_moves["top_move"] != "":
            bot_move_options.append(intelligent_moves["top_move"])
        if intelligent_moves["side_move"] != "":
            bot_move_options.append(intelligent_moves["side_move"])
        if len(bot_move_options) > 0:
            gobj = random.choice(bot_move_options)
        else:
            # default Strategy: bot randomly picks a column with an open spot   
            gobj = random.choice(game_state.open_spots)


    # Based on what colum was picked, finding the lowest open spot in the column 
        lowest_spot = gobj
        for spot in game_state.open_spots:
            current_spot_x_value = spot.getX()
            current_spot_y_value = spot.getY()
            if current_spot_x_value == lowest_spot.getX():
                if current_spot_y_value > lowest_spot.getY():
                    lowest_spot = spot
        gobj = lowest_spot
        # Making the Bot's piece
        gobj.setColor("#0000FF")
        bot_piece = GOval(gobj.getX(), gobj.getY(), 50, 50)
        bot_piece.setFilled(True)
        bot_piece.setColor("#0000FF")
        gw.add(bot_piece)
        game_state.bot_moves.append(gobj)
        game_state.open_spots.remove(gobj)
        print("bot has", 21 - len(game_state.bot_moves) , "pieces left.")
        if check_connect4(game_state.bot_moves) == True:
            game_state.is_game_active[0]= False
            endgame("Bot","")
        if 21 - len(game_state.bot_moves) < 0: 
            game_state.is_game_active[0] = False
            endgame("", "Player")

        
        return None
    gw.addEventListener("click", click_action)
if __name__ == "__main__":
    connectfour()