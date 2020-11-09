def prime_or_composite(number):
    if number == 1:
        return "1 is neither prime nor composite."
    if number == 2:
        return "2 is prime."
    for num in range(2, number):
        if number == num + 1:
            return str(number) + " is prime."
        if number % num != 0:
            continue
        if number % num == 0:
            return str(number) + " is composite."
    pass

if __name__ == "__main__":
    numbers = [1, 2, 10, 31, 47, 89, 101, 103, 97, 187, 981, 19201]
    # If you want to test the efficency of your algorithm add this number to the array above -7
    # If you want to test the efficency of your algorithm add this number to the array above 47055833459
    answers = []
    for number in numbers:
        answers.append(prime_or_composite(number))
    
    print(answers)