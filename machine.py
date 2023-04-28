from state import State
from word import Word

class Machine(object):

    def __init__(self, states: dict, letters) -> None:
        self.__states = states
        self.__letters = letters
        self.__acceptionStates = list(map(lambda tupleState: tupleState[1], filter(lambda s: s[1].isAcception, states.items())))
        self.__initialState = list(map(lambda tupleState: tupleState[1], filter(lambda s: s[1].isInital, states.items())))[0]

    def process(self, word: Word) -> bool:
        return self.__iterate(self.__initialState, word)


    def __iterate(self, state: State, word: Word, position=0, iterations=0):
        if iterations > 10000:
            return False, word
        transition = state.getTransition(word.get(position))
        if not transition:
            return state.isAcception, word
        
        print(transition, word.getWordWithPosition(position))
        nextState, word, position = transition.apply(word, position)

        return self.__iterate(self.__states[nextState], word, position, iterations + 1)
    
        
    def __str__(self) -> str:
        return "machine([{0}], {1})".format(list(self.__states.values()), self.__initialState)
    
    def __repr__(self) -> str:
        return "machine([{0}], {1})".format(list(self.__states.values()), self.__initialState)