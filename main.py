import random


def foldandswap(numbers):
    for i in range(0,int(len(numbers)/2)):
        sub = numbers[i]
        numbers[i] = numbers[-i]
        numbers[-i] = sub


def main():
    numbers = [2, 3, 0, 5, 4, 1, 6, 9, 8, 7]
    print(numbers)
    foldandswap(numbers)
    print(numbers)

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    foldandswap(numbers)
    print(numbers)


if __name__ == '__main__':
    main()
