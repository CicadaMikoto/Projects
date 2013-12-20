#**Reverse a String**
#Enter a string and the program will reverse it and print it out.

originalStr = ''
reverseStr = ''

originalStr = raw_input("Enter a string to be reversed: ")

for ch in range(len(originalStr)):
    reverseStr += originalStr[((len(originalStr) - 1) - ch)]

print reverseStr