# Challenge - Done
def same_necklace(first, second):
    for i in range (len(second)):
        if first == second[i:] + second[:i]:
            return True
    return False