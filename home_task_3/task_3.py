def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def get_number_and_check_is_prime():
    number = int(input("Choose your number: "))

    if is_prime(number):
        print('Number is prime')
    else:
        print('Number is not prime')


number_of_checks = int(input("Choose your number of checks: "))
for i in range(number_of_checks):
    get_number_and_check_is_prime()