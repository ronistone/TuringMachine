import json
from transition import Transition
from state import State
from machine import Machine
from word import Word

def createTransition(transition):
    return ( transition['state'],
        Transition(
            transition['nextState'],
            transition['letter'],
            transition['result'],
            transition['move']
        )
    )

with open('machine-definition.json', 'r') as d:
    definition = json.loads(d.read())

transitions = {}

for t in definition['transitions']:
    state, transition = createTransition(t)
    if state in transitions:
        transitions[state].append(transition)
    else:
        transitions[state] = [transition]

state = {}
for s in definition['states']:
    name = s['name']
    state[name] = State(name, transitions[name] if name in transitions else [] , s['isInitial'], s["isAcception"])


machine = Machine(state, definition['letters'])

word = input("Insert the word to test: ")

isAccepted,finalWord = machine.process(Word(word))

print("{word} {result} accepted! -> Final Word {finalWord}".format(word=word, result='is' if isAccepted else 'not is', finalWord=finalWord))


