class Solution:
	def __init__(self, filename):
		self.headCoords = [0,0]
		self.tailCoords = [0,0]
		self.movements = self.GetMovements(filename)
		self.tailVisitedCoords = self.TrackTailMovement()


	def GetMovements(self, filename):
		movements = []
		with open(filename, 'r') as f:
			for line in f:
				direction, length = line.split()
				movements.append([direction, int(length)])

		return movements

	def GetDistance(self):
		xt, yt = self.tailCoords
		xh, yh = self.headCoords
		vertDist, horzDist = abs(yh - yt), abs(xh - xt)

		if vertDist >= 2 or horzDist >= 2:
			return True
		else:
			return False


	def TrackTailMovement(self):
		tailVisitedCoords = []

		for move in self.movements:
			print(move)
			direction, length = move
			for i in range(length):
				if direction == 'U':
					self.headCoords[1] += 1
				elif direction == 'D':
					self.headCoords[1] -= 1
				elif direction == 'L':
					self.headCoords[0] -= 1
				elif direction == 'R':
					self.headCoords[0] += 1

				if self.GetDistance():
					xt, yt = self.tailCoords
					xh, yh = self.headCoords
					vertDist, horzDist = yh - yt, xh - xt

					
					if vertDist == 2 and horzDist == 0:
						self.tailCoords[1] += 1
					elif (vertDist == 2 and horzDist == 1) or (vertDist == 1 and horzDist == 2):
						self.tailCoords = [x+1 for x in self.tailCoords]
					elif vertDist == 0 and horzDist == 2:
						self.tailCoords[0] += 1
				
					elif vertDist == -2 and horzDist == 0:
						self.tailCoords[1] -= 1
					elif (vertDist == -1 and horzDist == 2) or (vertDist == -2 and horzDist == 1):
						self.tailCoords[0] += 1
						self.tailCoords[1] -= 1
					elif (vertDist == -2 and horzDist == -1) or (vertDist == -1 and horzDist == -2):
						self.tailCoords = [a-1 for a in self.tailCoords]
				
					elif vertDist == 0 and horzDist == -2:
						self.tailCoords[0] -= 1
					elif (vertDist == 1 and horzDist == -2) or (vertDist == 2 and horzDist == -1):
						self.tailCoords[0] -= 1
						self.tailCoords[1] += 1
					else:
						print('Didnt acount for this type of move')

				print(f'Tail >> {self.tailCoords}, Head >> {self.headCoords}')
				tailVisitedCoords.append(self.tailCoords[:])

		return [(x,y) for x, y in tailVisitedCoords]






def main():
	s = Solution('input.txt')
	#s = Solution('example.txt')
	print(f'Part 1: How many tiles have the tail visited? {len(set(s.tailVisitedCoords))}')

if __name__ == '__main__': main()