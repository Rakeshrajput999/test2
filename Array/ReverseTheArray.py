"""
Write a program to reverse an array or string"""


# iterative way /

def ReverseListIterative(A,start,end):
    while start <end :
        A[start] ,A[end]= A[end],A[start]
        start += 1
        end -=1
"""time complexity O(n)"""


# recursion way

def ReverseListRecursive(A,start,end):
    if start >= end:
        return 
    A[start],A[end]= A[end],A[start]
    ReverseListRecursive(A,start+1,end-1)
"""time complexity O(n)"""


# python List Slicing
def reverseListSlicing(A):
    print(A[ : :-1])

# driver code 

A = [1,4,3,5,4,3,7]
print (A)
ReverseListIterative(A,0,len(A)-1)
print("output vie iterative way")
print(A)
ReverseListRecursive(A,0,len(A)-1)
print ("output vie recursion")
print(A)

print("output vie slicing")
reverseListSlicing(A)

