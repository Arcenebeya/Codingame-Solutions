n = int(input())
strings = [input() for i in range(n)]

for string in reversed(strings):
    print(*map(ord,reversed(string)), sep='')
