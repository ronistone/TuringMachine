from transition import Transition

class State:

    def __init__(self, state, transitions, isInitial=False, isAcception=False) -> None:
        self.__state = state
        self.__transitions = transitions
        self.__isAcception = isAcception
        self.__isInitial = isInitial
    

    @property
    def isAcception(self):
        return self.__isAcception
    
    @property
    def isInital(self):
        return self.__isInitial
    
    @property
    def name(self):
        return self.__state
    
    def getTransition(self, letter) -> Transition:
        for t in self.__transitions:
            if t.letter == letter:
                return t
        return None

    def __str__(self) -> str:
        return "{0}(isAcception={1}, isInitial={2}, {3})".format(self.__state, self.__isAcception, self.__isInitial, self.__transitions)

    def __repr__(self) -> str:
        return "{0}(isAcception={1}, isInitial={2}, {3})".format(self.__state, self.__isAcception, self.__isInitial, self.__transitions)