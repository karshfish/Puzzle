"""
Puzzle8 Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from functions import *

def print_puzzle(puzzle):
	p=''
	for i in puzzle:
		if i==0: p+=' '
		else: p+=str(i)
	print (
		'-'*13 + '\n' +
		'| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
		'-'*13 + '\n' +
		'| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
		'-'*13
		)
def Moves (puzzle):
	position= puzzle.index(0)
	moves={'0':['d''s'],
	'1':['d','s','a'],
	'2':['a','s'],
	'3':['d','s','w'],
	'4':['d','s','a','w'],
	'5':['w','s','a'],
	'6':['d','w'],
	'7':['d','w','a'],
	'8':['w','a']}
	available_moves=moves[str(position)]
	return available_moves
	
								

def function2(puzzle,slected_move):
    kdmnffgjfgf
def function3(puzzle):
    kbdfkbfsdbhl    


def human_play(puzzle):
	while (True):
		print_puzzle(puzzle)
		available_moves=function1(puzzle) # returns the possible actions in the current state of the puzzle
		print('available moves: ',available_moves)
		selected_move=input('select a move: ')
		if selected_move not in available_moves:
			print('Game Over'); break
		puzzle=function2(puzzle,selected_move) # apply the action to the current state and returns the new state of the puzzle
		if function3(puzzle): # returns True only if the state of the puzzle satisfy the goal condition
			print_puzzle(puzzle); print("You win"); break

if __name__ == '__main__':
	puzzle=[
	3,1,2,
	4,0,5,
	6,7,8
	]
	human_play(puzzle)
