from dataclasses import dataclass

from .position import Position


@dataclass
class Player:
    name    : str
    impostor: bool
    position: Position
