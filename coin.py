'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
num = input()
N = input().split()
msg=""

for r in range(1,len(N)-1):
    firstHalf=0
    secondHalf=0
    for a in range(r):
        firstHalf += int(N[int(a)])
    for t in range(r+1,len(N)):
        secondHalf += int(N[int(t)])

    if(secondHalf==firstHalf):
        msg="YES"
        break;
if(msg==""):
    print("NO")
print(msg)
