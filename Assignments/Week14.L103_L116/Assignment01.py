# # التكليف 01

#     قم بكتابة محتويات ال Class لتظهر النتيجة كما في المثال

# class Game:
#   # Write Class Content

# game_one = Game("Ys", "Falcom", 2010, 50)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# # Needed Output
# # "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
# ===========================================================

class Game:

  # Write Class Content

    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self):
        return self.price * 15.6


game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()} Egyptian Pounds", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
