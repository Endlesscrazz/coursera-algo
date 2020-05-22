# Uses python3
import sys

def get_change(value):

    p, n, d = 1, 5, 10
    count = 0
    while value > 0:
        if value >= d:
            count += value // d
            value %= d
        elif value >= n:
            count += value // n
            value %= n
        else:
            count += value // p
            break
    return count


if __name__ == '__main__':
    value = int(input())
    print(get_change(value))
