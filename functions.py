def av_moves (puzzle):
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

def update_puzzle(puzzle,selected_move):
    p1=0
    zero_pos=puzzle.index(0)
    if selected_move=='d':
        if zero_pos+1 <=8 and zero_pos+1>=0:
         p1=puzzle[zero_pos+1]
         puzzle[zero_pos+1]=0
         puzzle[zero_pos]=p1
    elif selected_move=='a':
        if zero_pos-1 <=8 and zero_pos-1>=0:
           p1=puzzle[zero_pos-1]
           puzzle[zero_pos-1]=0
           puzzle[zero_pos]=p1
    elif selected_move=='s':
        if zero_pos+3 <=8 and zero_pos+3>=0:
           p1=puzzle[zero_pos+3]
           puzzle[zero_pos+3]=0
           puzzle[zero_pos]=p1
    elif selected_move=='w':
        if zero_pos-3 <=8 and zero_pos-3>=0:
           p1=puzzle[zero_pos-3]
           puzzle[zero_pos-3]=0
           puzzle[zero_pos]=p1
    return puzzle



def win (puzzle):
    win_condition=[0,1,2,3,4,5,6,7,8]
    if puzzle==win_condition:
        return True
    else:
        return False   