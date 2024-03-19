Number = int(input("Enter the Number of terms "))

# first two terms
first, second = 0, 1
count = 0

if Number <= 0:
   print("Please enter a number which is greater than 0 !!")

else:
   print("Fibonacci sequence is :")
   while count < Number:
       print(first)
       curr = first + second
       first = second
       second = curr
       count += 1
print("Anakha R Menon")
print("CH.EN.U4CSE20103\n")
