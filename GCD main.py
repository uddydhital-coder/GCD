#Program to find find HCF/GCD
#Enter 2 numbers
numberLargest = int(input("Enter Largest number: "))
numberSmallest = int(input("Enter Smallest number "))

#Using Eucliden Algorithims
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is : ",numberLargest)
