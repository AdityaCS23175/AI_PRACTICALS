#PRELAB – Awareness of Google Colab and VS Code to Implement a Python Program to find a magic square of given dimension.

def generateSquare(n):

    # create n x n matrix filled with 0
    magicSquare = [[0 for i in range(n)] for j in range(n)]

    # starting position
    i = n // 2
    j = n - 1

    num = 1
    total = n * n

    while num <= total:

        # condition 1: if row becomes -1 and column becomes n
        if i == -1 and j == n:
            j = n - 2
            i = 0

        else:
            # if column becomes n
            if j == n:
                j = 0

            # if row becomes -1
            if i < 0:
                i = n - 1

        # condition 2: if cell already filled
        if magicSquare[i][j] != 0:
            j = j - 2
            i = i + 1
            continue

        else:
            magicSquare[i][j] = num
            num = num + 1

        # move to next position
        j = j + 1
        i = i - 1

    # printing magic square
    print("\nMagic Square:\n")
    for x in range(n):
        for y in range(n):
            print("%2d" % magicSquare[x][y], end=" ")
        print()

    print("\nSum of each row/column =", n * (n*n + 1) // 2)


# Driver code
n = int(input("Enter odd number for Magic Square: "))
generateSquare(n)