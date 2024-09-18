def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    
    if year % 4 ==0:
        if year % 100==0:
            if year % 400==0:
                print("Leap Year")
                return True
            else:
                print("Not Leap Year")
                return False
        else:
            print("Leap Year")
            return True
    else:
        print("Not Leap Year")
        return False

is_leap_year(2400)
is_leap_year(2100)
is_leap_year(1989)