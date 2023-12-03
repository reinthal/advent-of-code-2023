import sys

small_input = \
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def is_digit(c: chr) -> bool:
    return c in "0123456789"

def is_symbol(c: chr) -> bool:
    return c not in "0123456789."

class Schematic:

    part_numbers = []

    def __init__(self, matrix) -> None:
        self.max_j = len(matrix[0]) - 1
        self.max_i = len(matrix) - 1
        self.matrix = matrix

    
    def get_number(self, i: int, j: int) -> int:
        """get the number from the matrix @ pos i,j
        
        
        assuming that a number is a contiguos string of digits 0..9
        assume that a number cannot have stretch multiple rows
        
        """
        if self.matrix[i][j] not in "0123456789":
            return 0
        number = ""
        
        # Go fowards through the string
        ctr = 0
        while j + ctr < self.max_j and is_digit(self.matrix[i][j+ctr]):
            number = number + self.matrix[i][j+ctr]
            self.matrix[i][j+ctr] = "." # erase the digit to avoid double-counting
            ctr = ctr + 1
        
        # Go backwards through the string
        ctr = 1
        while j - ctr >= 0 and is_digit(self.matrix[i][j-ctr]):
            number = self.matrix[i][j-ctr] + number
            self.matrix[i][j-ctr] = "." # erase the digit to avoid double-counting
            ctr = ctr + 1
        return int(number)

    def get_adjecents(self, i,j):
        """get adjecent numbers of i,j
        
        a number can be adjecent in  8 ways
             \ ^ /  
            <- x ->
             / ~ \ 
        this corresponds to 

        1. i, j+1
        2. i+1, j+1
        3. i+1, j
        4. i+1, j-1
        5. i, j-1
        6. i-1, j-1
        7. i-1, j
        8. i-1, j+1

        in clockwise order.
        """
        cases = [
            (i, min(self.max_j, j+1)),
            (min(self.max_i, i+1), min(self.max_j,j+1)), 
            (min(self.max_i, i+1), j),
            (min(self.max_i, i+1), max(0, j-1)), 
            (i, max(0, j-1)), 
            (max(0, i-1), max(0, j-1)),
            (max(0, i-1), j), 
            (max(0, i-1), min(self.max_j,j+1))
        ]
        hits = []
        for case in cases:
            i_c, j_c = case
            if is_digit(self.matrix[i_c][j_c]):
                hits.append(case)
        return hits

    def traverse_schematic(self):
        """traverses the schematic and adds part numbers to schematic list
        
        algorithm looks like this

        sum = 0
        for each element e in matrix:
            if e is a symbol
                numbers = get_adjecent(e)
                remove numbers from matrix marking them with ...
        """
        sum = 0
        for i in range(0, self.max_i + 1):
            for j in range(0, self.max_j + 1):
                current_character = self.matrix[i][j]
                if is_symbol(current_character):
                    hits = self.get_adjecents(i, j)
                    for hit in hits:
                        n = self.get_number(*hit)
                        self.part_numbers.append(n)
                        sum = sum + n
        print(sum)

def main():
    schematic = []
    with open(sys.argv[1], 'r') as fp:
        for line in fp.readlines():
            schematic.append(list(line))
    engine = Schematic(schematic)
    engine.traverse_schematic()
    engine.part_numbers.sort()
    print(engine.part_numbers)

    
    


    pass

if __name__ == "__main__":
    main()