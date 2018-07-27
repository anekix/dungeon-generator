W =60
H =60
MAX_ROOMS = 12
def grid():
	g = []
	r = []
	for i in range(H):
		g.append( ['.']*W)
	return g

def print_map(G):
	for i in G: print ' '.join(i)

def check_collides(room, rooms):
	## explanation: http://codesam.blogspot.com/2011/02/check-if-two-rectangles-intersect.html
	collides = False
	for i in rooms:
		if( 
		room['x']+room['w'] < i['x'] 
		or room['y']+room['h'] < i['y']
		or room['y'] > i['y'] + i['h']
		or room['x']  > i['x'] + i['w']
		):
		
			print 'does not collides'
		
		else:
			collides = True
			print 'collides'
	return collides	

	


def room():
	from random import randint
	room = {}
	room['x'] = randint(1,W-10);
	room['y'] = randint(1,H-10);
	room['w'] = randint(9,13);
	room['h'] = randint(9,13);
	return room

def get_rooms():
	rooms = []
	room_count = 0
	while room_count < (MAX_ROOMS):
		R = room()
		collides = check_collides(R,rooms)
		print '(',collides,')'
		if not collides:
			rooms.append(R)
			room_count += 1
		else:
			print "FOUND COLLISION, TRYING ANOTHER PLACEMENT"

		
		

	return rooms

def render(G,rooms):
	for i in rooms:
		x = i['x']
		y = i['y']
		w = i['w']
		h = i['h']
		for c in range(x,x+w):

			for d in range(y,y+h):
				G[c][d] = '#'
	return G

G = grid()	

#print_map(G)

rooms = get_rooms()

print_map(render(G,rooms))
