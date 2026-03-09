#Apply the concept of production rules to solve the water jug problem. (A Water Jug Problem: You are given two jugs, a 4-gallon one and a 3-gallon one, a pump which has unlimited water which you can use to fill the jug, and the ground on which water may be poured. Neither jug has any measuring markings on it. How can you get exactly 2 gallons of water in
the 4-gallon jug?)
a_cap = int(input("Enter capacity of Jug A: "))
b_cap = int(input("Enter capacity of Jug B: "))
goal = int(input("Enter goal amount in Jug A: "))

a = 0
b = 0

print("Start State:", (a,b))

while a != goal:

    if a == 0:
        a = a_cap
        print("Action: Fill Jug A ->", (a,b))

    elif b < b_cap:
        pour = min(a, b_cap - b)
        a = a - pour
        b = b + pour
        print("Action: Pour A -> B ->", (a,b))

    else:
        b = 0
        print("Action: Empty Jug B ->", (a,b))

print("Goal Reached:", (a,b))