#Write a python program using while loop that prints a triangle pattern of stars. 
stars = 5
i = 1

while i <= stars:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
