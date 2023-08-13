class Solution:
	def __init__(self, filename):
		self.instructions = self.ReadInstructions(filename)
		self.signalStrengths = self.CalcSumOfSignalStrength()
		self.SumOfSignalStrengths = sum([signal[0]*signal[1] for signal in self.signalStrengths])

	def ReadInstructions(self, filename):
		instructions = []
		with open(filename, 'r') as f:
			for instruction in f:
				ins = instruction.split()
				if len(ins) != 1:
					cmd, val = ins
					instructions.append([cmd, int(val)])
				else:
					instructions.append([ins[0], 0])

		return instructions

	def print(self, cycle, register):
		print(f'Cycle: {cycle} >> Register: {register}')

	def CheckCycle(self, cycleNo):
		cycleChecks = [20,60,100,140,180,220]

		if cycleNo in cycleChecks:
			return True
		else:
			return False


	def CalcSumOfSignalStrength(self):
		signalStrengths = []
		register = [1]
		cycle = 0

		for ins in self.instructions:
			cmd, val = ins

			if cmd == 'addx':
				cycle += 1
				if self.CheckCycle(cycle):
					signalStrengths.append([cycle, sum(register)])
				cycle += 1
				if self.CheckCycle(cycle):
					signalStrengths.append([cycle, sum(register)])
				register.append(val)
			elif cmd == 'noop':
				cycle += 1
				if self.CheckCycle(cycle):
					signalStrengths.append([cycle, sum(register)])
			else:
				print(f'Didnt acount for this command >> {ins}')


		return signalStrengths





def main():
	#s = Solution('example.txt')
	s = Solution('input.txt')

	print(f'Part 1, list of signal strengths: {s.signalStrengths}')
	print(f'     Sum of signal strengths {s.SumOfSignalStrengths}')




if __name__ == '__main__': main()