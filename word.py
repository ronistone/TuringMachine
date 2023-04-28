class Word:

    def __init__(self, word) -> None:
        self.__word = bytearray(word.encode())
        self.__negative_word = bytearray('#'.encode())
    

    def get(self, position):
        if position >= 0 and position < len(self.__word):
            return self.__word[position]
        elif position < 0 and -position < len(self.__negative_word):
            return self.__negative_word[-position]
        else:
            self.define(position, ord('#'))
            return ord('#')
    
    def define(self, position, value):
        if position >= 0:
            self.__define_positive(position, value)
        else:
            self.__define_negative(-position, value)

    def __define_negative(self, position, value):
        if position < len(self.__negative_word):
            self.__negative_word[position] = value
        else:
            self.__negative_word = self.__negative_word + ('#'.encode() * (position - len(self.__negative_word) + 1))

    def __define_positive(self, position, value):
        if position < len(self.__word):
            self.__word[position] = value
        else:
            self.__word = self.__word + ('#'.encode() * (position - len(self.__word) + 1))

    def getWordWithPosition(self, position):
        word = self.__str__()
        normalizedPosition = -position if position < 0 else (position + len(self.__negative_word)-1)
        if normalizedPosition == len(word) - 1:
            return word[:normalizedPosition] + '[' + word[normalizedPosition] + ']'
        return word[:normalizedPosition] + '[' + word[normalizedPosition] + ']' + word[normalizedPosition+1:]

    def __str__(self) -> str:
        return "{0}".format(self.__negative_word[1:].decode() + self.__word.decode())

    def __repr__(self) -> str:
        return "{0}".format(self.__negative_word[1:].decode() + self.__word.decode())