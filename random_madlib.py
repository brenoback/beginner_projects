from madlibs import avengers, champions, futebol, harry_potter
import random

if __name__ == "__main__":
    m = random.choice([avengers, champions, futebol, harry_potter])
    m.madlib()
