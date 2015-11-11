from random import randint

class RandomPlayer():
    """Player that chooses a move randomly."""
    def move(self, game, legal_moves, time_left):
        if not legal_moves: return (-1,-1)
        return legal_moves[randint(0,len(legal_moves)-1)]


class HumanPlayer():
    """Player that chooses a move according to
    user's input."""
    def move(self, game, legal_moves, time_left):
        print('\t'.join(['[%d] %s'%(i,str(move)) for i,move in enumerate(legal_moves)] ))
        
        valid_choice = False
        while not valid_choice:
            try:
                index = int(raw_input('Select move index:'))
                valid_choice = 0 <= index < len(legal_moves)

                if not valid_choice:
                    print('Illegal move! Try again.')
            
            except ValueError:
                print('Invalid index! Try again.')
        return legal_moves[index]


class OpenMoveEvalFn():
    
    def score(self, game):
        # TODO: finish this function!
        eval_func = len(game.get_legal_moves())
        return eval_func


class CustomEvalFn():

    def score(self, game):
        eval_func = len(game.get_legal_moves())
        return eval_func



class CustomPlayer():
    # TODO: finish this class!
    def __init__(self, search_depth=3, eval_fn=OpenMoveEvalFn()):
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, legal_moves, time_left):

        #best_move, utility = self.minimax(game, depth=self.search_depth)
        best_move, utility = self.alphabeta(game, depth=self.search_depth)
        # you will eventually replace minimax with alpha-beta
        return best_move

    def myutility(self, game):
        
        if game.is_winner(self):
            return float("inf")

        if game.is_opponent_winner(self):
            return float("-inf")

        return self.eval_fn.score(game)

    def minimax(self, game, depth=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if depth == 0 or game.is_winner(self) or game.is_opponent_winner(self):
            return (-1,-1),self.myutility(game)
        if maximizing_player:
        	best_val = float('-inf')
        	best_move = None
        	for move in game.get_legal_moves():
        		newgame = game.forecast_move(move)
        		dummymove,val = self.minimax(newgame,depth-1,False)
        		if val>best_val:
        			best_val = val
        			best_move = move
        	return best_move, best_val
        else:
        	best_val = float('inf')
        	best_move = None
        	for move in game.get_legal_moves():
        		newgame = game.forecast_move(move)
        		dummymove,val = self.minimax(newgame,depth-1,True)
        		if val<best_val:
        			best_val = val 
        			best_move = move
        	return best_move, best_val

    def alphabeta(self,game, depth=float("inf"), alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        # TODO: finish this function!
        if depth == 0 or game.is_winner(self) or game.is_opponent_winner(self) :
            return (-1,-1),self.myutility(game)
        if maximizing_player:
            best_val = float('-inf')
            best_move = (-1,-1)
            for move in game.get_legal_moves():
                newgame = game.forecast_move(move)
                dummymove,val = self.alphabeta(newgame,depth-1,alpha,beta,False)
                if val>best_val:
                    best_val = val
                    best_move = move
                if best_val>alpha:
                    alpha = best_val
                if beta <= alpha:
                    break
            return best_move, best_val
        else:
            best_val = float('inf')
            best_move = (-1,-1)
            for move in game.get_legal_moves():
                newgame = game.forecast_move(move)
                dummymove,val = self.alphabeta(newgame,depth-1,alpha,beta,True)
                if val<best_val:
                    best_val = val
                    best_move = move
                if best_val<beta:
                    beta = best_val
                if beta <= alpha:
                    break
            return best_move, best_val
        #return best_move, best_val



"""Example test you can run
to make sure your AI does better
than random."""
from isolation import Board

if __name__ == "__main__":
    r = RandomPlayer()
    h = CustomPlayer()
    game = Board(h,r)
    game.play_isolation()