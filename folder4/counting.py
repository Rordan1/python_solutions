if __name__ == '__main__':
    n = int(input())

def counting():
    numbers = [i + 1 for i in range(0, n)]
    return numbers

result = counting()
print(result)
