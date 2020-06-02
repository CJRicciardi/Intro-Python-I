"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open("foo.txt", "r")
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

n = open("bar.txt", "w")
n.write(
    """
    Get up, stand up, stand up for your rights!
    Get up, stand up, don't give up the fight!

    Most people think,
    Great God will come from the skies
    Take away everything
    And make everybody feel high
    But if you know what life is worth
    You will look for yours on earth
    And now you see the light
    You stand up for your rights. Jah!

    Get up, stand up!
    Stand up for your rights!
    """)

n.close()