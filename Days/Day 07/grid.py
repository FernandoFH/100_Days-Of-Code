from array import Array

class Grid:
    def __init__(self, rows, columns, fillValue = None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fillValue)

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += str(self.data[row][col]) + " "
            result += "\n"

        return str(result)

