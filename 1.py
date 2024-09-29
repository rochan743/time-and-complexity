number_list=[1,3,5,4,2,3,4,5,4]
def get_total(numbers_list):
    total = 0
    for number in numbers_list:
        total+= number
    return total

print(get_total(number_list))    