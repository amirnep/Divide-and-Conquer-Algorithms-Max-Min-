#Algorithm Design: Dr. Pira
#Chapter1 Project by Amir Nematpour - 981830281
#Shahid Madani University

import Class as c

arr_num = [] #Array for save numbers

n = int(input("Please Enter How Many Numbers Do You Want: "))

for _ in range (n):
    num = int(input("Please Enter number: "))
    arr_num.append(num)

if __name__ == '__main__':
    
    answer = c.find(arr_num)

    print()
    print(c.find.findminmax.__doc__)
    print("Minimum is: ",min(answer.findminmax())) #Find min
    print("Maximum is: ",max(answer.findminmax())) #Find max
    print()

quit = input("If You Want To Exit Please Press Enter.")
