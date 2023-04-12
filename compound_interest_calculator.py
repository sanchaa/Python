# A Simple and Compound Interest Calculator

def print_intro():
    print("Welcome to the Sanz's Compound Interest Calculator.")
    print('This program calculates your potential returns when you invest with us')


'''VARIABLES TO INCORPORATE

    •P is the principal amount (the amount you start with).
    •r is the annual rate of interest (as a decimal).
    •t is the number of years the amount is invested.
    •A is the amount at the end of the investment.'''


def get_input():
    starting_amount = int(input("What amount would you like to start with? "))
    annual_rate = float(input("What interest rate do you want on your account? "))
    number_of_years = int(input("How many years would you like to invest with us? "))
    return starting_amount, annual_rate, number_of_years


def simple_interest(principal, rate, years):
    si = principal * (1 + (rate / 100) * years)
    return si


def compound_interest(principal, rate, years):
    # ci = (principal * (1 + (rate / (4 * 100)))) ** (4 * years)
    ci = principal * ((1 + (rate / 100) / 4) ** (4 * years))
    return ci


def print_simple_output(principal, rate, years, result):
    print('Your simple interest is: £{:.2f}'.format(result))


def print_compounding_output(principal, rate, years, result):
    print('Your compound interest is: £{:2.2f}'.format(result))


# ---------- Challenge Functions (Optional) ----------

def print_target_output(principal, rate, years):
    years = 0
    amount = 0 
    target = amount + years
    while amount < target:
        amount = compound_interest(principal, rate, years)
        years = years + 1
    return years


# def get_target_input():


def get_choice():
    print()
    print()
    choice = input()
    return choice

# ---------- Main driver function ----------
# 1.	Print a welcome message explaining the purpose of the program.
# 2.	Prompt the user for the necessary inputs (see formulae and brief) and convert the values the user enters into
#       suitable data types.
# 3.	Perform the simple and compound interest calculations.
# 4.	Print the results to the terminal in the format specified. '''


def main():
    print_intro()
    principal, rate, years = get_input()
    si = simple_interest(principal, rate, years)
    ci = compound_interest(principal, rate, years)
    print_simple_output(principal, rate, years, si)
    print_compounding_output(principal, rate, years, ci)
    print_target_output(principal, rate, years)
    get_choice()
    # get_choice = get_choice()
    # if get_choice == 2:

    
if __name__ == '__main__':
    main()
