import itertools

def solve_cryptarithmetic(word1, word2, result):
    letters = set(word1 + word2 + result)
    
    if len(letters) > 10:
        print("Too many unique letters!")
        return
    
    letters = list(letters)
    digits = range(10)

    # Try all possible digit permutations
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # First letter should not be zero
        if (mapping[word1[0]] == 0 or
            mapping[word2[0]] == 0 or
            mapping[result[0]] == 0):
            continue

        # Convert words to numbers
        num1 = int("".join(str(mapping[ch]) for ch in word1))
        num2 = int("".join(str(mapping[ch]) for ch in word2))
        num3 = int("".join(str(mapping[ch]) for ch in result))

        # Check condition
        if num1 + num2 == num3:
            print("\nSolution found:")
            print(f"  {word1.upper()}   ({num1})")
            print(f"+ {word2.upper()}   ({num2})")
            print("-" * 12)
            print(f"= {result.upper()}  ({num3})")
            return

    print("No solution found.")


# ---- INPUT ----
w1 = input("Enter first word: ").lower()
w2 = input("Enter second word: ").lower()
res = input("Enter result word: ").lower()

solve_cryptarithmetic(w1, w2, res)