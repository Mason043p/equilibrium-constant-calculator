while true:
try:
    a = float(input("What is a's starting value?"))
    b = float(input("What is b's starting value? "))
    forward_rate_constant = float(input("What is the value of the forward rate constant as a decimal? "))
    reverse_rate_constant = float(input("What is the value of the reverse rate constant as a decimal? "))
    number_of_calculations = int(input("How many calculations would you like to make? "))
except ValueError:
    print("Please input a number, not letters")     

def formula():
    
    global a
    global b
    global forward_rate_constant
    global reverse_rate_constant

    a = a - a * forward_rate_constant  
    a = a + b * reverse_rate_constant
    b = b * reverse_rate_constant + a * forward_rate_constant
    q = b / a
    print("a = " , a , "b = " , b , "q =  " , q)


count = 0
while count < number_of_calculations:
    count = count + 1
    formula()

