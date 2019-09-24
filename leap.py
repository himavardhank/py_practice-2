def check_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,"is leap year")
    else:
        print("not a leap year")
check_year(1975)
