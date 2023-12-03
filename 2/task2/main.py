import sys
data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
class Draw:
    red = 0
    green = 0
    blue = 0
    def __init__(self, draw) -> None:
        colors = draw.split(', ')
        for c in colors:
            number = int(c.split(" ")[0])
            color = c.split(" ")[1]
            if color == "green":
                self.green = number
            elif color == "red":
                self.red = number
            else:
                self.blue = number

class Configuration:

    red = 0
    green = 0
    blue = 0
    
    def __init__(self) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0
    
    def update_minimal(self, draw: Draw) -> bool:
        self.red = max(self.red, draw.red)
        self.green = max(self.green, draw.green)
        self.blue = max(self.blue, draw.blue)
    
    def pow(self) -> int:
        return self.red * self.green * self.blue

def main():
    sum = 0
    for game in sys.stdin:
        min_config = Configuration()
        draws = game.split(": ")[-1].split(';')
        for draw in draws:
            d = Draw(draw.strip())
            min_config.update_minimal(d)
        sum = sum + min_config.pow()
    print(sum)
            
if __name__ == "__main__":
    main()