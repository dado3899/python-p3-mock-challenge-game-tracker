class Game:
    def __init__(self, title):
        self.title = title

    def results(self):
        return_list = []
        for r in Result.all:
            if r.game is self:
                return_list.append(r)
        return return_list

    def players(self):
        # Loop through all the results for this game
        # Check if player is in a master list
        # If not add to that list
        # Return list
        pass

    def average_score(self, player):
        # Loop through all results of the player
        sum = 0
        count = 0
        for r in player.results():
            # Check if game is self 
            if r.game is self:
            # Calculate sum
                sum = sum + r.score 
                count += 1
            # Divide by amount of results
        return sum/len(player.results())
        # return sum/player.num_times_played(self)
        pass

    def get_title(self):
        return self._title
    def set_title(self, value):
        # print(value)
        if type(value) is str and 0<len(value) and not hasattr(self,"title"):
            self._title = value
        else:
            print("NOT VALID TITLE")
    title = property(get_title,set_title)

g1 = Game("BOTW")
class Player:
    def __init__(self, username):
        self.username = username

    def results(self):
        # [Result(),Result()]
        # Loop through every result in existance
        # print(Result.all)
        return_list = []
        for r in Result.all:
            if r.player is self:
                return_list.append(r)
        return return_list

        # Check if that user is this player
        # If so add it to a master list
        pass

    def games_played(self):
        return_list = []
        # Loop through all the results attatched to this player
        for my_r in self.results():
            #Check if game is in our list, if not add it
            if my_r.game not in return_list:
                return_list.append(my_r.game)
        return return_list
        # THIS IS TEMP, HARD CODED EXAMPLE
        # return [g1]
        pass
    def played_game(self, game):
        # Look at all of our games played
        our_played_games = self.games_played()
        # If the game we pass in is in that list return true
        if game in our_played_games:
            return True
        return False
        pass

    def num_times_played(self, game):
        # Look through all instances of times we played the game
        count = 0
        for r in self.results():
        # Count up whenever we see the game passed in
            if r.game is game:
                count+=1
        return count
        pass

    def get_username(self):
        return self._username
    def set_username(self, value):
        # if type(value) is str and 0<len(value) and not hasattr(self,"title"):
        if type(value) is str and 2<=len(value)<=16:
            self._username = value
        else:
            print("NOT VALID USERNAME")
    username = property(get_username,set_username)

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def get_score(self):
        return self._score
    def set_score(self, value):
        if type(value) is int and 1<=value<=5000 and not hasattr(self,"score"):
            self._score = value
        else:
            print("NOT VALID score")
    score = property(get_score,set_score)

    def get_player(self):
        return self._player
    def set_player(self, value):
        if type(value) is Player:
            self._player = value
        else:
            print("NOT VALID player")
    player = property(get_player,set_player)

    def get_game(self):
        return self._game
    def set_game(self, value):
        if type(value) is Game:
            self._game = value
        else:
            print("NOT VALID game")
    game = property(get_game,set_game)



p1 = Player("DD")
# print(type(g1)
g2 = Game("MAss Effect")
g3 = Game("God Of War")
# player, game, score
s1 = Result(p1,g1,1)
s1_2 = Result(p1,g1,300)
s1_3 = Result(p1,g2,1000)
# p1.results()
s2 = Result(Player("Bob"),Game("TOTK"), 90)
# print(p1.games_played()[0].title)
# print(p1.num_times_played(g3))
print(g1.average_score(p1))
# print(Result.all)
# print(s1.score)
# s1.score = 0
# print(p1.username)
# p1.username = "XXX_KILERMAN_XXX"
# print(p1.username)
# g1.title = "TOTK"
# print("49", g1.title)