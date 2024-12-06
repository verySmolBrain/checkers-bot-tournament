from checkers_bot_tournament.bots.base_bot import Bot
from checkers_bot_tournament.move import Move
from checkers_bot_tournament.board import Board


class FirstMover(Bot):
    """
    Just picks the first move :D
    """
    def play_move(self, board: Board, colour: str, move_list: list[Move]) -> int:
        return 0
    
    def get_name(self) -> str:
        return "FirstMover"