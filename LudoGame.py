# Author: Andrew Niman
# GitHub username: drewniman
# Date: 8/2/22
# Description: Ludo board game simulator, a game can be simulated by creating a LudoGame object with a players list and turns list.

class Player():
    """Represents the player who plays the game at a certain position. Used by LudoGame class."""
    def __init__(self, position):
        """
        Purpose: Initializes private data members for Player class, including:
        the position the player choose (A, B, C or D)
        start and end space for this player
        current position of the player’s two tokens: in the home yard, ready to go, somewhere on the board, or has finished.
        the current state of the player: whether the player has won and finished the game, or is still playing
        Parameters: position (A, B, C, or D)
        Return: none
        """
        self._position = position
        self._start = None                  #didn't end up using, this is established in the conditional dictionary
        self._end = "E"
        self._cur_pos_p = None              #in the home yard, ready to go, somewhere on the board, or has finished
        self._cur_pos_q = None              #in the home yard, ready to go, somewhere on the board, or has finished
        self._cur_state = "STILL_PLAYING"   #can be either "FINISHED" or "STILL_PLAYING"
        self._token_p_step_count = -1       #corresponds to home yard
        self._token_q_step_count = -1
        self._stacking_state = "NOT_STACKED"   #can be set to "STACKED"

        # set dictionary linking step count to position on the board, depending on start position
        if position == "A":
            keys = [i for i in range(-1, 58)]
            values = ["H", "R"] + [str(i) for i in range(1, 51)] + ["A1", "A2", "A3", "A4", "A5", "A6", "E"]
            self._steps_to_pos = dict(zip(keys, values))
        elif position == "B":
            keys = [i for i in range(-1, 58)]
            values = ["H", "R"] + [str(i) for i in range(15, 57)] + [str(i) for i in range(1, 9)] + ["B1", "B2", "B3", "B4", "B5", "B6", "E"]
            self._steps_to_pos = dict(zip(keys, values))
        elif position == "C":
            keys = [i for i in range(-1, 58)]
            values = ["H", "R"] + [str(i) for i in range(29, 57)] + [str(i) for i in range(1, 23)] + ["C1", "C2", "C3", "C4", "C5", "C6", "E"]
            self._steps_to_pos = dict(zip(keys, values))
        elif position == "D":
            keys = [i for i in range(-1, 58)]
            values = ["H", "R"] + [str(i) for i in range(43, 57)] + [str(i) for i in range(1, 37)] + ["C1", "C2", "C3", "C4", "C5", "C6", "E"]
            self._steps_to_pos = dict(zip(keys, values))

    def get_completed(self):
        """
        Purpose: check if the player has finished the game or not
        Parameters: none
        Return: True if player has finished, False if player has not finished
        """
        """
        1. Check _token_p_step_count
            a. If "E", check _token_q_step_count
                i. If "E", return True
        
        1. If _cur_state is "FINISHED"
            a. return True
        2. Otherwise, return False
        """

        if self._cur_state == "FINISHED":   #check the cur_state data member
            return True
        else:
            return False

    def set_completed(self):
        """If both tokens have reached the end of the board, updates cur_position to "FINISHED".
        Should be called each time a token is moved"""
        """
        1. Check _token_p_step_count
            a. If "E", check _token_q_step_count
                i. If "E", set _cur_state to "FINISHED"
        """
        if self._token_p_step_count == 57:  #check if token p has reached the finish
            if self._token_q_step_count == 57:  #check if token q has reached the finish
                self._cur_state = "FINISHED"



    def get_token_p_step_count(self):
        """
        Purpose: Check how many steps the Players token P has taken on the board.
        Parameters: none
        Return: # of steps token P has taken on the board
        """
        return self._token_p_step_count

    def set_token_p_step_count(self, steps):
        """
        Purpose: Set how many steps the Player's token P has taken on the board. If step count goes over 57, bounces back down (58 becomes 56, etc)
        Parameters: steps (int)
        Return: none
        """
        """
        1. # of steps received from move_token method
        2. Update _token_p_step_count
        """
        self._token_p_step_count = steps


    def get_token_q_step_count(self):
        """
        Purpose: Check how many steps the Players token Q has taken on the board.
        Parameters: none
        Return: # of steps token Q has taken on the board
        """
        return self._token_q_step_count

    def set_token_q_step_count(self, steps):
        """
        Purpose: Set how many steps the Player's token Q has taken on the board. If step count goes over 57, bounces back down (58 becomes 56, etc)
        Parameters: steps (int)
        Return: none
        """
        """
        1. # of steps received from move_token method
        2. Update _token_q_step_count
        """
        self._token_q_step_count = steps

    def get_p_pos(self):
        """Based on position-dependent dictionary and token_p_step_count, returns the token position on the board"""
        return self._steps_to_pos[self._token_p_step_count]

    def set_p_pos(self, steps):
        """Sets the player's P token position based on step count"""
        self._cur_pos_p = self._steps_to_pos[steps]

    def get_q_pos(self):
        """Based on position-dependent dictionary and token_q_step_count, returns the token position on the board"""
        return self._steps_to_pos[self._token_q_step_count]

    def set_q_pos(self, steps):
        """Sets the player's Q token position based on step count"""
        self._cur_pos_q = self._steps_to_pos[steps]

    def get_space_name(self, steps):
        """
        Purpose: Given the step count, returns the name of the space the token has landed on the board as a string. Returns home yard position ("H") and ready to go position (‘R’) as well
        Parameters: steps - represents how many steps the token has taken on the board
        Return: Name of space as a string
        """
        """
        1. Look at the corresponding space name for the given # of steps
            a. This will be found in a dictionary specific to that Player's position
        2. Return space name as a string
        """
        return self._steps_to_pos[steps]    #same as get_p/q_pos, but with # of steps passed as a parameter

    def get_stacking_state(self):
        """Returns the stacking state of the Player's tokens"""
        return self._stacking_state

    def set_stacking_state(self, stacking_state):
        """Updates the stacking state of the Player's tokens"""
        self._stacking_state = stacking_state



class LudoGame():
    """Represents Ludo game, played by up to four players"""
    def __init__(self):
        """
        Purpose: Initialize private data members for LudoGame class, including:
        dictionary of positions (values) and Players (keys)
        end space (E) = 57 steps
        Parameters: none
        Return: none
        """
        self._players = {}
        self._end_space = 57
        self._valid_positions = ["A", "B", "C", "D"]

    def get_player_by_position(self, position):
        """
        Purpose: Create a new player with a given position. If invalid string parameter,
        Parameters: position (A, B, C, or D)
        Return: Valid parameter - Player object with specified position
                Invalid parameter - 'Player not found!'
        """

        """
        1. Check if string parameter is valid ("A, B, C, D")
            a. If parameter is invalid, return "Player not found!"
            b. If parameter is valid, return Player object with given starting position
        """
        if position in self._players:
            return self._players[position]
        else:
            return "Player not found!"


    def move_token(self, player, token, steps):
        """
        Purpose: Moves one of the tokens (p or q), (or both if the tokens are stacked) a given number of steps on the board, updates token's total steps. If token lands on an opponent's token, kicks out other token to home yard. Used by play_game.
        Parameters: player (Player object)
                    token ('p' or 'q')
                    steps (int)
        Return: none
        """

        """
        1. Check if the token steps will exceed 57
            a. Bounce token back once it hits 57
        2. Update token's step count
        3. Update token's current position (on the board)
        4. Check if any other Players have a token at the same position
            a. If another Player has a token at that position, kick it back to their Home Yard (steps = -1)
                i. If the other Player had stacked tokens there, kick them both back and set that Player's stacking_state to "NOT_STACKED"
            b, If the same Player has a token at that position, set Player's stacking_state to "STACKED"
        """
        if player.get_completed():    #if the player has finished the game, don't move any more tokens
            return

        if player.get_stacking_state() == "STACKED":
            new_steps = player.get_token_p_step_count() + steps
            if new_steps > 57:
                new_steps = 57 - (new_steps - 57)       #bounces token back from 57
            player.set_token_p_step_count(new_steps)    #update token p step count
            player.set_p_pos(new_steps)                 #update token position on board
            player.set_token_q_step_count(new_steps)    # update token q step count
            player.set_q_pos(new_steps)                 # update token position on board

        elif token == "p":
            if player.get_token_p_step_count() == -1:
                new_steps = 0
                player.set_token_p_step_count(new_steps)
                player.set_p_pos(new_steps)
            else:
                new_steps = player.get_token_p_step_count() + steps
                if new_steps > 57:
                    new_steps = 57 - (new_steps - 57)       #bounces token back from 57
                player.set_token_p_step_count(new_steps)    #update token step count
                player.set_p_pos(new_steps)                 #update token position on board

                if player.get_p_pos() == player.get_q_pos():    #check if token just landed on that Player's other token
                    player.set_stacking_state("STACKED")

        elif token == "q":
            if player.get_token_q_step_count() == -1:
                new_steps = 0
                player.set_token_q_step_count(new_steps)
                player.set_q_pos(new_steps)
            else:
                new_steps = player.get_token_q_step_count() + steps
                if new_steps > 57:
                    new_steps = 57 - (new_steps - 57)       #bounces token back from 57
                player.set_token_q_step_count(new_steps)    # update token step count
                player.set_q_pos(new_steps)                 # update token position on board

                if player.get_q_pos() == player.get_p_pos():    #check if token just landed on that Player's other token
                    player.set_stacking_state("STACKED")

        board_pos = player.get_space_name(new_steps)    #position of newly moved token
        players = self._players.values()                #create a list of just Player objects
        for other_player in players:
            if other_player is player:                  #don't apply these rules to the Player's own tokens
                continue
            if other_player.get_p_pos() == board_pos and board_pos != "R":         #if either token got landed on, except for R position
                other_player.set_token_p_step_count(-1)       #send it back to home yard
                other_player.set_p_pos(-1)
                if other_player.get_stacking_state() == "STACKED": #tokens are unstacked when they are kicked back to home yard
                    other_player.set_stacking_state("NOT_STACKED")
            if other_player.get_q_pos() == board_pos and board_pos != "R":
                other_player.set_token_q_step_count(-1)
                other_player.set_q_pos(-1)
                if other_player.get_stacking_state() == "STACKED":
                    other_player.set_stacking_state("NOT_STACKED")








    def play_game(self, players, turns):
        """
        Purpose: Initiates the gameplay of LudoGame. Creates the player list, then moves tokens according to the turns list following the priority rules and updates token positions and player's game state.
        Parameters: players (list of positions ['A', 'C'])
                    turns (list of tuples where each tuple is a roll for one player [('A', 6), ('A', 4), ('C', 5)] means player A rolls 6, then rolls 4, and player C rolls 5
        Return: List of strings representing the current spaces of all tokens for each player after executing all turns.
        """

        """
        
        3. Return list of strings of all current spaces of all tokens for each player
        """
        """For player in players list
            a. Create a Player object with the given position"""
        #for position in players:
         #   new_player = self.get_player_by_position(position)  #create a new player with the given position
          #  self._players[position] = new_player                #add new player to the player dictionary

        #can no longer use get_player_by_position to initialize new Player
        for position in players:
            self._players[position] = Player(position)  #initialize new Player with given position, and add to the dictionary of players

        player_list = self._players.values()

        """2. For each tuple in turns list
            a. Use priority rules to determine which token should be moved (calls priority_rules)
            b. Update token's position
            """
        for turn in turns:
            current_game_board = []
            player_pos = turn[0]
            player_obj = self._players[player_pos]
            steps = turn[1]
            p_pos = player_obj.get_p_pos()
            q_pos = player_obj.get_q_pos()
            player_obj.set_completed()
            token = self.priority_rules(player_obj, p_pos, q_pos, steps)    #this will return which token should be moved
            self.move_token(player_obj, token, steps)
            for player in player_list:
                current_game_board.append(player.get_p_pos())
                current_game_board.append(player.get_q_pos())
                player.set_completed()


        """c. Update player's game state"""

        #for player in player_list:
              #works whether they have finished or not

        """return a list of strings representing the current spaces of all of the tokens for each player in the list after moving the tokens following the rules described above"""
        current_game_board = []
        for player in player_list:
            current_game_board.append(player.get_p_pos())
            current_game_board.append(player.get_q_pos())

        return current_game_board

    def priority_rules(self, player, p_pos, q_pos, steps):
        """
        Purpose: Determines which token should be moved, p or q, given the priority rules
        Parameters: player (Player object)
                    token p current position
                    token q current position
                    number of steps rolled
        Return: 'p' or 'q'
        """

        """
        

        3. If one token can kick out an opponent token
            a. Return that token
        4. Return whichever token has a lower step count
        """

        """1. If roll is a 6
            a. If p in home yard, return p
            b. If q in home yard, return q"""
        if player.get_completed():  #check if the player is done
            return "p"

        if player.get_p_pos() != "H" and player.get_q_pos() == "H": #check if only p can be moved
            if steps != 6:
                return "p"

        if player.get_q_pos() != "H" and player.get_p_pos() == "H": #check if only p can be moved
            if steps != 6:
                return "q"

        if steps == 6:
            if player.get_p_pos() == "H":
                return "p"
            elif player.get_q_pos() == "H":
                return "q"

        """2. If one token is in a home square
            a. If step count + steps = 57, return that token"""
        if player.get_p_pos()[0] in "ABCD":   #check if token p is in a home square
            if player.get_token_p_step_count() + steps == 57:
                return "p"
        elif player.get_q_pos()[0] in "ABCD":
            if player.get_token_q_step_count() + steps == 57:
                return "q"

        """3. If one token can kick out an opponent token
            a. Return that token
            
            possibilities:
            player.get_p_step_count().get_space_name()
            player.get_q_step_count().get_space_name()
            """
        if player.get_token_p_step_count() + steps <= 57:
            move_p = player.get_space_name(player.get_token_p_step_count() + steps)
        else:
            move_p = None
        if player.get_token_p_step_count() + steps <= 57:
            move_q = player.get_space_name(player.get_token_q_step_count() + steps)
        else:
            move_q = None
        can_kick = []
        players = self._players.values()

        for other_player in players:
            if other_player is player:  # don't apply these rules to the Player's own tokens
                continue
            if other_player.get_p_pos() == move_p or other_player.get_q_pos() == move_p:  #check if moving token p can kick either of their tokens out
                can_kick.append("p")
            if other_player.get_p_pos() == move_q or other_player.get_q_pos() == move_q:    #check if moving token q can kick either of their tokens out
                can_kick.append("q")

        if "p" in can_kick and "q" not in can_kick: #check if only token p can kick out a token
            return "p"
        if "q" in can_kick and "p" not in can_kick: #check if only token q can kick out a token
            return "q"
        #if neither or both tokens can kick out another token, move on to next priority rule

        #return whichever token is further behind
        if player.get_token_p_step_count() <= player.get_token_q_step_count():  #check if token p is behind token q. If tokens are stacked, this will return token p
            return "p"
        else:
            return "q"
