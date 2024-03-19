from sys import maxsize

def maxSubArraySum(a, size):

    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    A = []
    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1

    print("\nMaximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
    print("sub array : ",end=" ")
    for i in range(size):
        if (i>=start) and (i<=end):
            print(a[i],end=" ")
    print("\n")
a = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSubArraySum(a, len(a))

print("Anakha R Menon")
print("ROLL.NO-CH.EN.U4CSE20103\n")