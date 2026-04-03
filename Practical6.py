import itertools

# take input
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

# get unique letters
letters = list(set(word1 + word2 + result))

# check limit
if len(letters) > 10:
    print("Too many letters!")
    exit()

# try all digit combinations
for perm in itertools.permutations(range(10), len(letters)):
    mapping = dict(zip(letters, perm))

    # first letter should not be zero
    if (mapping[word1[0]] == 0 or 
        mapping[word2[0]] == 0 or 
        mapping[result[0]] == 0):
        continue

    # convert to numbers
    num1 = int("".join(str(mapping[ch]) for ch in word1))
    num2 = int("".join(str(mapping[ch]) for ch in word2))
    num3 = int("".join(str(mapping[ch]) for ch in result))

    # check condition
    if num1 + num2 == num3:
        print("\nSolution found:\n")
        print(f"  {word1}   ({num1})")
        print(f"+ {word2}   ({num2})")
        print("------------")
        print(f"= {result}  ({num3})")
        break
else:
    print("No solution found.")