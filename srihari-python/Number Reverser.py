def reverse_number(num):
    reversed_num = 0
    while num > 0:
        # Get the last digit of the number using the modulo operator
        digit = num % 10
        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the number using the floor division operator
        num = num // 10
    return reversed_num
y=int(input("Enter the number that you want reversed: "))
print(reverse_number(y))
