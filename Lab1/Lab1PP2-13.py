
#Input
num = input("Please input a number between 10,000 and 999,999 [Please include a \',\' between thousands]: ")
#Processing
arr = num.split(',')
thousandsPlace = int(arr[0])
hundredsPlace = int(arr[1])
number = (thousandsPlace*1000) + hundredsPlace
#Output
print(number)

'''
Please input a number between 10,000 and 999,999 [Please include a ',' between thousands]: 10,999
10999
'''