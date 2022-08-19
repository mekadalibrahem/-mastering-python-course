# التكليف 04

# قم بكتابة محتويات ال Class لتظهر النتيجة كما في المثال
# إذا كتب الشخص إسم لعبة واحدة يظهر المثال كما في السطر الأول
# إذا كتب الشخص قائمة ألعاب في قائمة تظهر رسالة كما في المثال وتحتها قائمة الالعاب
# إذا كتب الشخص رقم تتغير الرسالة كما في المثال لتحسب عدد الألعاب فقط
# class Games:
# Write Class Content

# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()
# # Ouput
# # I Have One Game Called "Shadow Of Mordor"

# my_games_names.show_games()
# # Ouput
# # I Have Many Games:
# # -- Ys II
# # -- Ys Oath In Felghana
# # -- YS Origin

# my_games_count.show_games()
# # Output
# # I Have 80 Game.
# =========================================================

class Games:
    def __init__(self, games):
        self.games = games

    def show_games(self):
        if type(self.games) == int:
            print(f"I Have {self.games} Game.")
        elif type(self.games) == str:
            print(f"I Have One Game Called  \"{self.games}\" .")
        elif type(self.games) == list:
            print("I Have Many Games:")
            for game in self.games:
                print(f"-- {game}")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# v
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.
