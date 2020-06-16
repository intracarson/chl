# Challenge
def same_necklace(first, second):
    for i in range (len(second)):
        if first == second[i:] + second[:i]:
            return True
    return False

# Optional Bonus 1
def repeats(first):
    counter = 0
    if first == "":
        counter += 1
        return counter
    for i in range (len(first)):
        if first == first[i:] + first[:i]:
            counter += 1
    return counter

# Optional Bonus 2
def enable1_parse():
    enable1_file = open("enable1.txt", "r")
    

    enable1_file.close()
enable1_parse()