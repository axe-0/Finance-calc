#Capestone project 
import math 

print ( "\nWelcome to Capstone Financial services.\n We have some great financial products for you! \n We have the following services to offer you:")
print("  investment - to calculate the amount of interest you'll earn on your investment \n  bond - to calculate the amount you'll have to pay on a home loan \n")
#Ask for user input and covert to lower case 
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

#Confirm validity of input.
while (selection != "investment" and selection != "bond"):
    print("\nError: your entry is not valid. Please try again(tip: confirm spelling is correct)")
    selection = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

print ("Great choice!\n")


if (selection =="investment"):
    #Request investment inputs 
    deposit = float(input("Please enter the amount you wish to invest: R"))
    interest = float(input("Please enter the rate you require ? "))/100
    num_years = float (input("Enter the number of years you wish to invest your money? "))
    option = str(input("Enter your interest option type between 'simple' and 'compound' interest: ")).lower()

 #Confirm validity of option
    while (option != "simple" and option != "compound"):
        print("\nError: your entry is not valid. Please try again(tip: confirm spelling is correct)")
        option = input("Enter your interest option type between 'simple' and 'compound' interest:  ").lower()

    #Cacl interest at different options     
    if( option == "simple"):
        future_value = deposit* (1 + (interest*num_years))

    elif( option == "compound"):
        future_value = deposit * math.pow((1+interest),num_years)

    print ("Your investment of {:,.2f} at a {} interest rate of {:.2f} for {} years will be valued at : \n R{:,.2f} ".format(deposit,option,interest,num_years,future_value))
 

elif(selection == "bond"):
    #Request bond inputs 
    house_value = float(input("Enter the present value of your house : R"))
    int_rate = (float(input("Enter your interest rate : "))/100)/12
    repay_term =  int(input("Enter the number of months you plan to repay the loan : "))
     #Calc monthly repayment 
    repayment= (int_rate * house_value)/(1-(1+int_rate)**(-repay_term))
    
    print("You will have to repay R{:,.2f} a month for the next {} months on your bond.".format(repayment,repay_term))

