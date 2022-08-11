# Tetris

Tetris is a minimalistic, text-based version of the classic Tetris game implemented in Python. This project is designed to run in the terminal and provides a basic gameplay experience, featuring the essential mechanics of Tetris, including piece movement and rotation.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/tetris.git
```

2. Navigate to the cloned repository:

```
cd tetris
```

3. Create and activate a virtual environment:

```
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies using pip and the requirements.txt file:

```
pip install -r requirements.txt
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

You'll be prompted to enter the dimensions of the Tetris board. After that, control the falling Tetris pieces with the following commands:

- `piece`: Enter a new piece into the game. You'll need to input the type of piece after this command.
- `down`, `right`, `left`: Move the piece down, right, or left, respectively.
- `rotate`: Rotate the piece.
- `exit`: Exit the game.

To execute a command, simply type it and press Enter.

Example:

```
10 20
piece
O
down
right
rotate
```

## License

This project is licensed under the [MIT License](LICENSE.txt).
