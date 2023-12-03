import sys
data = """Game 1: 7 red, 14 blue; 2 blue, 3 red, 3 green; 4 green, 12 blue, 15 red; 3 green, 12 blue, 3 red; 11 red, 2 green
Game 2: 16 blue, 9 red, 5 green; 8 red; 8 blue, 5 green, 12 red; 11 blue, 8 green, 17 red
Game 3: 8 green, 1 blue, 7 red; 12 red, 6 blue, 9 green; 2 blue, 1 red, 14 green; 9 green, 4 red; 2 red, 1 blue, 8 green
Game 4: 1 blue, 3 green; 2 green, 1 blue, 1 red; 1 red, 3 green
Game 5: 6 red, 1 blue; 1 green; 5 red, 2 green; 1 red, 1 blue, 3 green
Game 6: 3 green, 4 red, 1 blue; 2 blue, 5 green, 2 red; 12 green, 3 blue, 2 red; 4 blue, 1 green, 4 red; 11 green, 6 red; 5 green, 10 red, 3 blue
Game 7: 2 blue, 3 green, 16 red; 1 blue, 3 red; 2 green, 13 red; 18 red, 2 blue, 1 green; 3 red, 1 blue
Game 8: 4 red, 3 blue, 8 green; 2 red, 16 green; 2 red, 1 blue"""
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
    
    @classmethod
    def is_possible(cls, draw: Draw) -> bool:
        return cls.red >= draw.red and cls.green >= draw.green and cls.blue >= draw.blue

def main():
    config = Configuration()
    ctr = 1
    sum = 0
    for game in sys.stdin:
        draws = game.split(": ")[-1].split(';')
        is_possible = True
        for draw in draws:
            d = Draw(draw.strip())
            if not config.is_possible(draw=d):
                is_possible = False
                break
        if is_possible:
            #print(ctr)
            sum = sum + ctr
        ctr = ctr + 1
    print(sum)
            
if __name__ == "__main__":
    main()