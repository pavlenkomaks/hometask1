nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e', 'f', 'g']
my_list = [n+2 for n in nums]
print(my_list)

new_list = [(digit, num) for digit in (digits) for num in range(4)]
print(new_list)

#map()
s = list(map(str, input().split()))
print(s)