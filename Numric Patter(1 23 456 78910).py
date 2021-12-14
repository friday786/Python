# Give the number of rows of the triangle as static input and store it in a variable.
numbOfRows = 4
# Take a variable and initialize it with 1 say Number.
Number = 1
# Loop from 1 to the number of rows of the triangle using For loop.
for m in range(1, numbOfRows+1):
  # Using another For loop, loop from 1 to the parent loop iterator value (Nested For loop).
    for n in range(1, m+1):
        # Inside the inner for loop print the Number with a space character.
        print(Number, end=' ')
        # Increase the value of Number by 1.
        Number = Number+1
    # Print the Newline Character after the end of the inner for loop.
    print()