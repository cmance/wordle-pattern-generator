# Wordle Pattern Generator

A Python tool that finds valid Wordle words that match specific color patterns when compared to a target word.

![Wordle Example](images/wordle-example.png)

*Ever wondered what words would create this exact pattern? This tool finds them for you!*

## What it does

This tool helps you find words that would produce specific Wordle color patterns (green, yellow, gray) when guessed against a known target word. This is useful for:
- Creating custom Wordle puzzles
- Analyzing Wordle strategies
- Finding words that produce specific feedback patterns

## How it works

The program takes:
1. **Today's word** - The target word (5 letters)
2. **Pattern array** - A 6-row pattern representing the color feedback for each guess

And returns valid Wordle words that would produce each specified pattern when guessed.

## Pattern Format

Each pattern is represented as an array of 6 rows, where each row contains 5 integers:

- `0` = Gray (letter not in the target word)
- `1` = Yellow (letter in target word but wrong position)  
- `2` = Green (letter in target word and correct position)

### Example Pattern
```python
[
    [1, 0, 0, 0, 0],  # Row 1: First letter yellow, rest gray
    [0, 1, 0, 0, 0],  # Row 2: Second letter yellow, rest gray
    [0, 0, 1, 0, 0],  # Row 3: Third letter yellow, rest gray
    [0, 0, 0, 1, 0],  # Row 4: Fourth letter yellow, rest gray
    [0, 0, 0, 0, 1],  # Row 5: Fifth letter yellow, rest gray
    [2, 2, 2, 2, 2]   # Row 6: All letters green (correct word)
]
```

## Usage

### Command Line Usage

The tool now supports command-line arguments for easy use:

```bash
python main.py [target_word] [pattern1] [pattern2] [pattern3] [pattern4] [pattern5] [pattern6]
```

Each pattern should be 5 comma-separated integers (0, 1, or 2).

**Example:**
```bash
python main.py "crane" "1,0,0,0,0" "0,1,0,0,0" "0,0,1,0,0" "0,0,0,1,0" "0,0,0,0,1" "2,2,2,2,2"
```

**Get help and examples:**
```bash
python main.py --example
```

### Quick Start

1. **Install Python** (3.6 or higher)
2. **Clone or download** this repository
3. **Ensure the word list file** `valid-wordle-words.txt` is in the same directory
4. **Run with command-line arguments**:

```bash
python main.py "crane" "1,0,0,0,0" "0,1,0,0,0" "0,0,1,0,0" "0,0,0,1,0" "0,0,0,0,1" "2,2,2,2,2"
```

### Example Output

```
Loaded 14855 valid Wordle words
Row 1: abbot
Row 2: babby
Row 3: bhels
Row 4: bibes
Row 5: bidon
Row 6: crane
```

### More Examples

**Progressive discovery pattern:**
```bash
python main.py "snake" "0,0,0,0,0" "1,0,0,0,0" "1,1,0,0,0" "2,1,0,0,0" "2,2,1,0,0" "2,2,2,2,2"
```

## File Structure

```
wordle-pattern-generator/
├── main.py                    # Main program file
├── valid-wordle-words.txt     # List of valid Wordle words (one per line)
├── README.md                  # This file
└── LICENSE                    # License file
```

## Customizing Patterns

### Command Line Examples

**Progressive Discovery:**
```bash
python main.py "snake" "0,0,0,0,0" "1,0,0,0,0" "1,1,0,0,0" "2,1,0,0,0" "2,2,1,0,0" "2,2,2,2,2"
```

### Code Examples

If you prefer to edit the code directly, think about what feedback each guess should produce:

### Example 1: Progressive Discovery
```python
main("SNAKE", [
    [0, 0, 0, 0, 0],  # All gray - no letters match
    [1, 0, 0, 0, 0],  # First letter yellow (S in wrong position)
    [1, 1, 0, 0, 0],  # Two letters yellow
    [2, 1, 0, 0, 0],  # First green, second yellow
    [2, 2, 1, 0, 0],  # More progress
    [2, 2, 2, 2, 2]   # Perfect match
])
```

## Requirements

- Python 3.6+
- `valid-wordle-words.txt` file containing valid Wordle words (included)

## How the Algorithm Works

1. **Load Word List**: Reads all valid Wordle words from the text file
2. **Pattern Matching**: For each pattern row, checks every valid word to see if it would produce that exact color pattern when compared to the target word
3. **Validation**: Ensures all patterns are valid (5 elements each, values 0-2 only)
4. **Output**: Returns the first matching word for each pattern row

## Contributing

Feel free to submit issues or pull requests to improve the tool.

## License

See LICENSE file for details.