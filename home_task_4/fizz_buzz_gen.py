def fizz_buzz_gen(amount):
    for i in range(1, amount + 1):
        if i%3 == 0 and i%5 == 0:
            yield 'fizz buzz'
        elif i%3 == 0:
            yield 'Fizz'
        elif i%5 == 0:
            yield 'Buzz'
        else:
            yield i


for i in fizz_buzz_gen(45):
    print(i, end=',')