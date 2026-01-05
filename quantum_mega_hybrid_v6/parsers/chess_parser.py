"""Chess variant parser proxy"""

import chess
import chess.variant

def load_variant(variant: str = "standard"):
    if variant == "crazyhouse":
        return chess.variant.CrazyhouseBoard()
    return chess.Board()
