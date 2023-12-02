import sys

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

    red = 12
    green = 13
    blue = 14

    def is_possible(self, draw: Draw) -> bool:
        return self.red >= draw.red and self.green >= draw.green and self.blue >= draw.blue

def main():
    config = Configuration
    ctr = 1
    sum = 0
    for game in sys.stdin:
        draws = game.split(';')
        for draw in draws:
            d = Draw(draw)
            if config.is_possible(d):
                sum = sum + ctr
        ctr = ctr + 1
            
            