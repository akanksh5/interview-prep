import random
from collections import deque

class Snake:
    def __init__(self,head: int,tail: int):
        if tail>= head:
            raise ValueError("The tail value cannot be an int.")
        self.head = head
        self.tail = tail

class Ladder:
    def __init__(self,top: int, bottom: int):
        if bottom >= top:
            raise ValueError("the bottom part of the ladder cannot be higher than the top")
        self.top = top
        self.bottom = bottom

class Player:
    def __init__(self,name :str,position :int):
        self.name = name
        self.position = position

class Board:
    def __init__(self,size :int, snakes : list[Snake], ladders: list[Ladder]):
        self.size = size
        self.snakes = {snake.head: snake.tail for snake in snakes}
        self.ladders = {ladder.bottom: ladder.top for ladder in ladders}
    
    def get_next_position(self,position: int):
        pos = position
        if position in self.snakes:
            pos = self.snakes[position]
        if position in self.ladders:
            pos = self.ladders[position]
        return pos

class Game:
    def __init__(self,players: list[Player],board: Board):
        self.players = deque(players)
        self.board = board
        self.winner = None
    
    def play_next_turn(self):
        player = self.players.popleft()
        position = random.randint(1,6)
        if player.position + position > self.board.size:
            print(f"Sorry! we can't go ahead of the board size.")
        pos = self.board.get_next_position(player.position+ position)
        if pos == self.board.size:
           self.winner = player
           print(f"We have a winner and that's player {player.name}!!")
        else:
            player.position = pos
            self.players.append(player)
    
    def start_game(self):
        print(f"The game has begun :D")
        while not self.winner:
            self.play_next_turn()

