
import argparse

def loadValidWords(filename="valid-wordle-words.txt"):
    """Load valid Wordle words from a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = [line.strip().lower() for line in file if line.strip()]
        print(f"Loaded {len(words)} valid Wordle words")

        return words
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find the word list file: {filename}")
    except Exception as e:
        raise Exception(f"Error reading word list file: {e}")


def getWordlePattern(guess, target):
    """
    Generate the Wordle pattern for a guess against a target word.
    Returns a list of 5 integers: 0=gray, 1=yellow, 2=green
    """
    pattern = [0] * 5
    targetChars = list(target)
    
    # First pass: mark all green (correct position) matches
    for i in range(5):
        if guess[i] == target[i]:
            pattern[i] = 2
            targetChars[i] = None  # Mark as used
    
    # Second pass: mark yellow (wrong position) matches
    for i in range(5):
        if pattern[i] == 0:  # Not green
            if guess[i] in targetChars:
                pattern[i] = 1
                # Remove one instance of this letter from available chars
                targetChars[targetChars.index(guess[i])] = None
    
    return pattern

def matchPattern(todaysWord, pattern, validWords):
    '''
    Should match the pattern against the valid words
    Returns an array for each row in the pattern
    '''
    wordMatches = []
    
    for element in pattern:
        if len(element) != 5:
            raise ValueError("Each pattern element must be 5 elements long")
        if not all(isinstance(x, int) and x in [0, 1, 2] for x in element):
            raise ValueError("Pattern elements must contain only integers 0, 1, or 2")

        matchingWords = []
        for word in validWords:
            if len(word) != 5:
                continue
            
            # Generate the actual Wordle pattern for this word against today's word
            actualPattern = getWordlePattern(word, todaysWord)
            
            # Check if it matches the desired pattern
            if actualPattern == element:
                matchingWords.append(word)
        
        wordMatches.append(matchingWords)
    
    return wordMatches

"""
Pattern is an array of 6 arrays. Format is [ [0, 2, 0, 1, 0], [1, 0, 2, 0, 1], [0, 0, 0, 0, 0]...]
0 is gray (not present in the word),
1 is yellow (present in the word but in the wrong position),
2 is green (present in the word and in the correct position)
"""
def main(todaysWord, pattern):
    if len(todaysWord) != 5:
        raise ValueError("Word must be 5 letters long")
    if len(pattern) != 6:
        raise ValueError("Pattern array must be 6 elements long")
    
    validWords = loadValidWords()
    wordMatches = matchPattern(todaysWord, pattern, validWords)
    
    for i, matches in enumerate(wordMatches):
        if matches:
            print(f"Row {i + 1}: {matches[0]}")
        else:
            print(f"Row {i + 1}: no match")
    
    return wordMatches
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find Wordle words that match specific color patterns')
    parser.add_argument('word', nargs='?', help='The target word (5 letters)')
    parser.add_argument('patterns', nargs='*', help='Six patterns, each as comma-separated values (e.g., "1,0,0,0,0")')
    parser.add_argument('--example', action='store_true', help='Show usage examples')
    
    args = parser.parse_args()
    
    if args.example:
        print("Usage examples:")
        print('python main.py "crane" "1,0,0,0,0" "0,1,0,0,0" "0,0,1,0,0" "0,0,0,1,0" "0,0,0,0,1" "2,2,2,2,2"')
        print()
        print("Pattern values:")
        print("0 = Gray (letter not in word)")
        print("1 = Yellow (letter in word, wrong position)")
        print("2 = Green (letter in word, correct position)")
        exit(0)
    
    if not args.word:
        print("Error: Target word is required")
        print("Use --example to see usage examples")
        exit(1)
    
    if len(args.patterns) != 6:
        print(f"Error: Exactly 6 patterns required, got {len(args.patterns)}")
        print("Use --example to see usage examples")
        exit(1)
    
    # Parse patterns from command line
    try:
        pattern = []
        for p in args.patterns:
            row = [int(x.strip()) for x in p.split(',')]
            if len(row) != 5:
                raise ValueError(f"Each pattern must have exactly 5 values, got {len(row)}")
            pattern.append(row)
    except ValueError as e:
        print(f"Error parsing patterns: {e}")
        print("Each pattern should be 5 comma-separated integers (0, 1, or 2)")
        print('Example: "1,0,0,0,0"')
        exit(1)
    
    # Run the main function
    try:
        main(args.word.lower(), pattern)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)