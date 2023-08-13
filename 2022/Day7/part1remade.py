class Directory:
	def __init__(self, name, size: int = 0, parent=None, isDir=False):
		self.name = name
		self.size = size
		self.parent = parent
		self.contains = []
		self.isDir = isDir

	def GetNameRepr(self, depth):
		space = ' '
		string = f'{depth*space*2}- {self.name}, size={self.size}' + '\n'
		return string

	def AddDirectory(self, dir):
		self.contains.append(dir)
		self.size += dir.size

		p = self.parent

		while p != None:
			p.size += dir.size
			p = p.parent

class Solution():
	root = None
	depth = 0

	def __init__(self, filename):
		self.inp = self.GetData(filename)
		self.DataHandler()

	def ReprHelper(self, dir, depth, string=''):
		depth += 1
		for d in dir.contains:
			string += d.GetNameRepr(depth)
			if len(d.contains) != 0:
				string = self.ReprHelper(d, depth, string)

		return string


	def __repr__(self):
		string = self.root.GetNameRepr(0)
		string += self.ReprHelper(self.root, 0)

		return string


	def GetData(self, filename):
		with open(filename,'r') as f:
			inp = [line.split() for line in f]

		return inp

	def DataHandler(self):
		currentDir = None
		for line in self.inp:
			#print(line)
			if line[0] == '$' and line[1] == 'cd':
				if line[2] == '/': #for root, initializes pathfinding currentDir
					self.root = Directory(line[2], isDir = True)
					currentDir = self.root
				elif line[2] == '..': #Escape 1 depth
					currentDir = currentDir.parent
				else: #Moving in 1 depth
					newDir = Directory(line[2],parent=currentDir, isDir=True)
					currentDir.AddDirectory(newDir)
					currentDir = newDir
			elif line[0] == 'dir' or line[1] == 'ls':
				pass
			else: # for files with size
				currentDir.AddDirectory(Directory(line[1],int(line[0]),currentDir))

	def MoreDirs(self, dir, size):
		sumOfDirs = 0
		for d in dir.contains:
			if d.size <= size and d.isDir == True:
				sumOfDirs += d.size
				sumOfDirs += self.MoreDirs(d, size)
			else:
				sumOfDirs += self.MoreDirs(d, size)

		return sumOfDirs

	def NumberOfDirsWithSizeLessThan(self, size):
		sumOfDirs = 0
		for d in self.root.contains:
			if d.size <= size and d.isDir == True:
				sumOfDirs += d.size
				sumOfDirs += self.MoreDirs(d, size)
			else:
				sumOfDirs += self.MoreDirs(d, size)

		return sumOfDirs

	def FindMoreDirs(self, dir, minSize, possibleSizes):
		for d in dir.contains:
			if d.size >= minSize and d.isDir == True:
				possibleSizes.append(d.size)
				possibleSizes + self.FindMoreDirs(d, minSize, possibleSizes)


		return possibleSizes


	def SizeOfSmallets(self, minSize):
		possibleSizes = []

		for d in self.root.contains:
			if d.size >= minSize:
				if d.isDir == True:
					possibleSizes.append(d.size)
					possibleSizes + self.FindMoreDirs(d, minSize, possibleSizes)

		return min(possibleSizes)

def main():
	s = Solution('input.txt')
	print(s)
	sumOfDirs = s.NumberOfDirsWithSizeLessThan(100000)

	availSpace = 70000000 - s.root.size
	minSize = 30000000 - availSpace
	sizeOfSmallets = s.SizeOfSmallets(minSize)


	print(f'Sum of size of files that make up less than 100.000: {sumOfDirs}')
	print(f'Size of smallest file to make room for update of size {minSize}: {sizeOfSmallets}')



if __name__ == '__main__': main()