class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __str__(self):
        return f'({self.__x}, {self.__y})'
