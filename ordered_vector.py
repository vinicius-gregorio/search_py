import numpy as np

class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=int)


    def printz(self):
            if self.last_position == -1:
                print('The vector is empty!')
            else:
                for i in range(self.last_position + 1):
                    print(f'Position {i}: {self.values[i]}')
        
    def insert(self, value):
            if self.last_position == self.capacity - 1:
                print('The vector is full!')
            else:
                position = 0
                while position <= self.last_position:
                    if self.values[position] > value:
                        break
                    position = position + 1
                for i in range(self.last_position, position - 1, -1):
                    self.values[i + 1] = self.values[i]
                self.values[position] = value
                self.last_position = self.last_position + 1
                    
                    
                    