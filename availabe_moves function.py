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