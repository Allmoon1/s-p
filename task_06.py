class WrongNumberOfPlayersError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'WrongNumberOfPlayersError, {0} '.format(self.message)
        else:
            return 'WrongNumberOfPlayersError has been raised'

class NoSuchStrategyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'NoSuchStrategyError, {0} '.format(self.message)
        else:
            return 'NoSuchStrategyError has been raised'


def rps_game_winner(array):
    game_rule_lst = {'R':'P', 'P':'S', 'S':'R'}
    if (len(array) > 2):
        raise WrongNumberOfPlayersError()
    if (array[0][1] not in game_rule_lst) or (array[1][1] not in game_rule_lst):
        raise NoSuchStrategyError()
    elif array[0][1] == array[1][1]:
        return array[0]
    elif (game_rule_lst[array[0][1]] in game_rule_lst) and (game_rule_lst[array[1][1]] == game_rule_lst[game_rule_lst[array[0][1]]]):
        return array[1]
    elif (game_rule_lst[array[1][1]] in game_rule_lst) and (game_rule_lst[array[0][1]] == game_rule_lst[game_rule_lst[array[1][1]]]):
        return array[0]
    else:
        raise ValueError("SomethingWentWrong")

print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) #=> WrongNumberOfPlayersError
#print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) #=> NoSuchStrategyError
#print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) #=> 'player2 S'
#print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'
#print(rps_game_winner([['player1', 'R'], ['player2', 'P']])) #=> 'player2 P'
#print(rps_game_winner([['player1', 'R'], ['player2', 'S']])) #=> 'player1 R'