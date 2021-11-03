# program to determine the count of a given character in a group of inputs
def gatherinput():
    strings = []
    while True:
        line=input("Input a string:")
        if line == '-1':
            break
        strings.append(line)
    return strings

def countinstances(character,vals):
    count = 0
    for string in vals:
        for char in string:
            if char == character:
                count += 1
    return count

def main():
    selectedchar = input("Select a character to count: ")
    if len(selectedchar) != 1:
        print("ONE character please!")
        quit()
    values = gatherinput()
    count = countinstances(selectedchar,values)
    print("Counted",count,"instances of", selectedchar)
main()