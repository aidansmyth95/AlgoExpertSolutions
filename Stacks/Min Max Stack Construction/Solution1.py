'''
Stacks are LIFO.
MinMaxStack: We can access max and min values in stack at any time.
All these action must be constant time and space - O(1)
Stack is just a LIFO stack.
minMaxStack keeps track of min/max values.
I implemented the indexing in this much cleaner than example.
'''

# All methods O(1) ST

class MinMaxStack:
	
	def __init__(self):
		self.minMaxStack = []
		self.stack = []
	
    def peek(self):
        return self.stack[-1]

    def pop(self):
		# remove tracked min max instance
        self.minMaxStack.pop()
		# remove and return actual value from stack
		return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
		newMinMax = {"min": number, "max": number}
		if len(self.minMaxStack):
			lastMinMax = self.minMaxStack[-1]
			newMinMax["min"] = min(lastMinMax["min"], newMinMax["min"])
			newMinMax["max"] = max(lastMinMax["max"], newMinMax["max"])
		self.minMaxStack.append(newMinMax)
				
    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]
