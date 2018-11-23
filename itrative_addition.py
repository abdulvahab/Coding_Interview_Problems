def palindrome(string):             # get user string
    length = len(string)                             # calculate length

    for i in range(0, length // 2):                  # loop through string to check for mismatch
        # comapre letter from front and back untill you reach in the middle
        if string[i] != string[length-(i+1)]:
            # as soon as you found a mismatch exit with print
            return False
        else:
            return True

def reversed_string(string):
    return string[::-1]

def add(counter,string):
    number = str(string)
    reversed_number = reversed_string(number)
    string = str (int(number) + int(reversed_number))
    counter += 1
    return counter ,string

string = input('Enter your string: ')
counter, string = add(0,string)
while(palindrome(string)):
    counter, string = add(counter,string)

print(counter, string)
