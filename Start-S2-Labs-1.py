# author: LM (AMDG) 1/24/22
#creating a function with one arguement being a list of numbers and another being numbers
#function should iterate through list and multiply each number by the number given
def products(list_numbers, number):
    #creates new list    
    new_lst = []
    #for ;oop to iterate through list 
    for index in list_numbers:
        #adding a new value and setting it equal to the product of the value and number given
        new_value = index * number
        #new value is appended to blank kist       
        new_value= new_lst.append(new_value)
        #prints new list 
        print(new_lst)

products([1, 2, 3, 4], 9)