def hh(list_of_numbers):
    while True:
        while 0 in list_of_numbers:
            list_of_numbers.remove(0)
        if len(list_of_numbers) == 0:
            return True
        list_of_numbers.sort(reverse=True)
        N = list_of_numbers[0]
        del list_of_numbers[0]
        
        print(N)
        if N > len(list_of_numbers):
            return False
        list_of_numbers = [N - 1 for N in list_of_numbers]
        

                   
    


print(hh([[5, 3, 0, 2, 6, 2, 0, 7, 2, 5]]))