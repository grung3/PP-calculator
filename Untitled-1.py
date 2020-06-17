print("Hello, and welcome to the pp identifier. Please enter your pp size ")
original = input("Please enter your pp size: ")

if ((original >= 'a' and original <= 'z')
        or (original >= 'A' and original <= 'Z')):
    print("That is not a number. Please enter a digit.")
elif original.isalpha and (original >= '5'):
    print("Wow! " + original + " inches, that's really big")
elif original.isalpha and (original < '5'):
    print("Really, " + str(original) + " inches is really small")
