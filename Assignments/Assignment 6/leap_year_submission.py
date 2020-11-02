def leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        return str(year) + " is a leap year"
    elif year % 4 == 0 and not year % 100 == 0:
        return str(year) + " is a leap year"
    else:
        return str(year) + " is not a leap year"

        


if __name__ == "__main__":
    years = [2000, 1994, 1912, 3002, 1700, 1400]
    answers = []
    for year in years:
        answers.append(leap_year(year))
    
    print(answers)