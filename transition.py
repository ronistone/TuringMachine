from word import Word
# from state import State

class Transition(object):
    def __init__(self, nextState, letter, result, move) -> None:
        self.__nextState = nextState
        self.__letter = ord(letter[0])
        self.__result = ord(result[0])
        self.__move = move
    
    @property
    def letter(self):
        return self.__letter
    

    def apply(self, word: Word, position: int) -> tuple[object, Word, int]:
        word.define(position, self.__result)

        if self.__move == 'L':
            position -= 1
        elif self.__move == 'R':
            position += 1
        
        return (self.__nextState, word, position)
    
    def __str__(self) -> str:
        return "({0}, {1}, {2}, {3})".format(self.__nextState, chr(self.letter), chr(self.__result), self.__move)
    
    def __repr__(self) -> str:
        return "({0}, {1}, {2}, {3})".format(self.__nextState, chr(self.letter), chr(self.__result), self.__move)