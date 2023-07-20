def print_1_n(n):
    if n>0:
        print_1_n(n-1)
        print(n,end=" ")
    return " "
n=int(input())
print(print_1_n(n))