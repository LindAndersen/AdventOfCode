class Solution:
	def __init__(self, filename, numberOfKnots):
		self.knotsCoords = [[0,0] for x in range(numberOfKnots)]
		self.movements = self.GetMovements(filename)
		self.tailVisitedCoords = self.TrackTailMovement()


	def GetMovements(self, filename):
		movements = []
		with open(filename, 'r') as f:
			for line in f:
				direction, length = line.split()
				movements.append([direction, int(length)])

		return movements

	def GetDistance(self, knotIndex):
		xt, yt = self.knotsCoords[knotIndex-1]
		xh, yh = self.knotsCoords[knotIndex]
		vertDist, horzDist = abs(yh - yt), abs(xh - xt)

		if vertDist >= 2 or horzDist >= 2:
			return True
		else:
			return False

	def ChangeHeadCoords(self, direction):
		if direction == 'U':
			self.knotsCoords[-1][1] += 1
		elif direction == 'D':
			self.knotsCoords[-1][1] -= 1
		elif direction == 'L':
			self.knotsCoords[-1][0] -= 1
		elif direction == 'R':
			self.knotsCoords[-1][0] += 1


	def TrackTailMovement(self):
		tailVisitedCoords = []

		for move in self.movements:
			print(move)
			direction, length = move

			for i in range(length):
				for i in reversed(range(1, len(self.knotsCoords))):
					if i == len(self.knotsCoords)-1:
						self.ChangeHeadCoords(direction)

					if self.GetDistance(i):
						xt, yt = self.knotsCoords[i-1]
						xh, yh = self.knotsCoords[i]
						vertDist, horzDist = yh - yt, xh - xt

						
						if vertDist == 2 and horzDist == 0:
							self.knotsCoords[i-1][1] += 1
						elif (vertDist == 2 and horzDist == 1) or (vertDist == 1 and horzDist == 2):
							self.knotsCoords[i-1] = [x+1 for x in self.knotsCoords[i-1]]
						elif vertDist == 0 and horzDist == 2:
							self.knotsCoords[i-1][0] += 1
					
						elif vertDist == -2 and horzDist == 0:
							self.knotsCoords[i-1][1] -= 1
						elif (vertDist == -1 and horzDist == 2) or (vertDist == -2 and horzDist == 1):
							self.knotsCoords[i-1][0] += 1
							self.knotsCoords[i-1][1] -= 1
						elif (vertDist == -2 and horzDist == -1) or (vertDist == -1 and horzDist == -2):
							self.knotsCoords[i-1] = [a-1 for a in self.knotsCoords[i-1]]
					
						elif vertDist == 0 and horzDist == -2:
							self.knotsCoords[i-1][0] -= 1
						elif (vertDist == 1 and horzDist == -2) or (vertDist == 2 and horzDist == -1):
							self.knotsCoords[i-1][0] -= 1
							self.knotsCoords[i-1][1] += 1
						#Handling abs(2,2) diagonals
						elif vertDist == 2 and horzDist == 2:
							self.knotsCoords[i-1] = [x+1 for x in self.knotsCoords[i-1]]
						elif vertDist == -2 and horzDist == 2:
							self.knotsCoords[i-1][0] += 1
							self.knotsCoords[i-1][1] -= 1
						elif vertDist == -2 and horzDist == -2:
							self.knotsCoords[i-1] = [x-1 for x in self.knotsCoords[i-1]]
						elif vertDist == 2 and horzDist == -2:
							self.knotsCoords[i-1][0] -= 1
							self.knotsCoords[i-1][1] += 1

						else:
							print(f'Didnt acount for this type of move. vertDist: {vertDist}, horzDist: {horzDist}')

					#print(f'Tail >> {self.tailCoords}, Head >> {self.headCoords}')
					print(self.knotsCoords[0])
					if self.knotsCoords[0] not in tailVisitedCoords:
						tailVisitedCoords.append((self.knotsCoords[0]).copy())
						#tailVisitedCoords.append(self.knotsCoords[0][:])

		return tailVisitedCoords






def main():
	s = Solution('input.txt', 10)
	#s = Solution('example.txt', 10)
	#s = Solution('largerexample.txt', 10)
	#print(s.tailVisitedCoords)
	print(f'Part 2: How many tiles have the tail visited? {len(s.tailVisitedCoords)}')


if __name__ == '__main__': main()