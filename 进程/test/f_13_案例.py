class Game:
    top_score = 0
    def __init__(self, play_name):
        self.play_name = play_name
    @staticmethod
    def show_help():
        print("游戏提示:玩就行")

    @classmethod
    def show_top_score(cls):
        print("历史最高分%d" % cls.top_score)

    def start_game(self):
        print("开始游戏:%s" % self.play_name)

Game.show_help()
Game.show_top_score()
game = Game("张三")
game.start_game()