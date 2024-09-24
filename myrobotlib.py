
def series(num):
    num = int(num)
    print(1, 2, end=" ")
    a = 1
    b = 2
    for i in range(3, num - 1):
        sum = a + b
        a, b = b, sum
        print(sum, end=" ")

