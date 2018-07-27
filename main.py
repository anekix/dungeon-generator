# -*- coding: utf-8 -*-

from random import randint

W =60
H =60
MAX_ROOMS = 30
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

	room = {}
	room['x'] = randint(1,W-10);
	room['y'] = randint(1,H-10);
	room['w'] = randint(5,9);
	room['h'] = randint(5,7);
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


def find_closest_room(R, rooms):
	mid_point = { 'x': R['x']+(R['w']/2), 'y': R['y']+(R['h']/2) }
	closest_distance = 1000000
	closest_room = {}
	for i in rooms:
		if i == R:continue
		i_mid = { 'x': R['x']+(R['w']/2), 'y': R['y']+(R['h']/2) } 
		distance = abs(mid_point['x'] - i_mid['x']) + abs(mid_point['y'] - i_mid['y'])
		if distance < closest_distance:
			closest_distance = distance
			closest_room = i
	return closest_room
			 
		
 
def build_coridors(G, rooms):
	for i in rooms:
		roomA = i
		roomB = find_closest_room(roomA, rooms) 	
		
		# Find random points in the current room & closest room

		pointA = { 'x': randint(roomA['x'] , roomA['x'] + roomA['w']) , 'y': randint(roomA['y'] , roomA['y']+ roomA['h'])}
		pointB = { 'x': randint(roomB['x'] , roomB['x']+ roomB['w']) , 'y': randint(roomB['y'] ,  roomB['y'] + roomB['h'])}


		while (pointB['x'] != pointA['x']) or (pointB['y'] != pointA['y']) :         
			if pointB['x'] != pointA['x']:             
			    if pointB['x'] > pointA['x']:
				pointB['x'] -= 1
			    else:
				pointB['x'] += 1
			elif pointB['y'] != pointA['y']:
			    if pointB['y'] > pointA['y']:
				pointB['y'] -= 1
			    else:
	 			pointB['y'] +=1 
		
			print pointB['x'],pointB['y']
			G[pointB['x']][pointB['y']] = 'x'
		
	return G
		
def render(G,rooms):
	for i in rooms:
		x = i['x']
		y = i['y']
		w = i['w']
		h = i['h']
		for c in range(x,x+w):

			for d in range(y,y+h):
				G[c][d] = '▓'
	return G

G = grid()	

#print_map(G)

rooms = get_rooms()

print_map(render(G,rooms))

G  = build_coridors(G,rooms)
print_map(render(G,rooms))
