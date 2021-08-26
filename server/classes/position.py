from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return o.x == self.x and o.y == self.y

        return (self.x, self.y) == o


print(Position(1, 2) == (1, 2))
