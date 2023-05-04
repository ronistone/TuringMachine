

## Requirements

- Python 3


## Execution

Use `python3 main.py`

## Machine Configuration

 - In file `machine-definition.json` is the state, letters and transitions used by the machine.

### 1. States
  The states are defined by a list of:
  ```
"states": [{
    "name": "q0",
    "isAcception": false,
    "isInitial": false
}]
  ```
Where name is the state name, isAcception define if the machine ends up in this state the word should be accepted, and isInitial tells the machine to start processing the word from this state.
#### Restrictions

  1. Only one state must have 'isInitial' equal to true
  2. The machine accepts multiple states with 'isAcception' equal to true

### 2. Letter

The letters define the alphabet used, it's just a list of char:

```
"letters": [
        "a",
        "b",
        "N",
        "R",
        "#"
]
```

### 3. Transitions

The transitions define the action that should be executed when determinate letter is found in the head and when the machine is in a determinate state. So if the state is 'q0' and the machine finds the letter 'a', then the machine will write X and move the head 'R' (Right), and change the machine to nextState

```
{
    "state": "q0",
    "nextState": "q1",
    "letter": "a",
    "result": "X",
    "move": "R"
}
```
   - 'state' indicate the state from
   - 'nextState' indicate the state to move
   - 'letter' indicate the letter that to be found
   - 'result' indicate the letter that should be write in the word
   - 'move' indicate the moviment in the word that the machine should have.

#### Restrictions
  1. 'state' and 'nextState' must be in the [states](#1-states) list
  2. 'letter' and 'result' must be in the [letters](#2-letter) list
  3. 'move' must be 'R' (right) or 'L' (left)