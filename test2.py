file_name = './quote.csv'

one = '1'
two = 'Emil'
three = 'Rasmussen'
oneTwoThree = 'Emil,Rasmussen'
with open(file_name, 'a') as file_object:
    file_object.write(oneTwoThree)
