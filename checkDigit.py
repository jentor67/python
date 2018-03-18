import sys

"""checkDigit.py: Determines the check Digit from different methods."""
"""user>python checkDigit.py"""

__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"

def selectVersion(question):
    if (sys.version_info > (3,0)):
        # python3 code
        selection = input(question)
    else:
        selection = raw_input(question)

    return selection

def ISBN10():
    print("Calculating ISBN10 check digit:")
    Number = "A"

    while( Number.isdigit() == False ):
        Number = selectVersion("Input 9 digit ISBN 10 Number: ")
        if( Number.isdigit() == True and len(Number) == 9 ):
            i = 0
            sumProduct = 0
            while( i < 9 ):
                theProduct = 10-i
                sumProduct = sumProduct + int(Number[i])*theProduct
                i = i +1
            checkDigit = 11 - sumProduct % 11
            print(" ")
            print("The Check Digit is "+str(checkDigit))
            print(" ")
            break
        else:
            print(" ")
            if( Number.isdigit() == True ): 
                print("***WARNING*** Input does not contain 9 digits, please try again.")
            else:
                print("***WARNING*** Input is not all digits, please try again.")
            Number = "A"
            
    
def USBank():
    print("Calculating US Bank account number Check digit:")
    Number = "A"
    while ( Number.isdigit() == False ) :
        Number = selectVersion("Input Account Number: ")
        if( Number.isdigit() == True and len(Number) <= 12 ):
            # We will start from the left and use the weight 7, 5, 3, 2
            # Pad the account number with 0 for a length of 12
            Number = format(Number, "0>12s")
            print("The account number used will be "+str(Number))
            i = 0
            weights = "753275327532"
            sumProduct = 0
            while( i < 12 ):
                product=int(weights[i])*int(Number[i])
                # this will give us values from 0 to 63
                # sum the digits of the product

                if( product > 9 ):
                    # The product has 2 digits 
                    sumProduct = sumProduct + int(str(product)[0]) + int(str(product)[1])
                else: 
                    # The product has 1 digit
                    sumProduct = sumProduct + product  

                i = i + 1
            checkDigit = 10 - ( sumProduct % 10)   
            print(" ")
            print("The Check Digit is "+str(checkDigit))
            print(" ")
        else:
            print(" ")
            if( Number.isdigit() == True ): 
                print("***WARNING*** Input contains more than 12 digits, please try again.")
            else:
                print("***WARNING*** Input is not all digits, please try again.")
            Number = "A"


def UPCBarcode():
    print("Calculating UPC barcode check digit:")
    Number = "A"
    while ( Number.isdigit() == False ) :
        Number = selectVersion("Input the 11 digit UPC Number: ")
        if( Number.isdigit() == True and len(Number) == 11 ):
            lenNumber = len(Number)
           
            # Add the odd number of digits 
            i = 0
            oddNumbers=0
            while( i < lenNumber ):
                oddNumbers = oddNumbers + int(Number[i])
                i = i +2
            oddNumbers = oddNumbers*3
            
            # sum evan numbers
            i = 1
            evenNumbers=0
            while( i < lenNumber ):
                evenNumbers = evenNumbers + int(Number[i])
                i = i +2
    
            # Add the evenNumbers to the Odd Numbers
            totalSumProduct = evenNumbers + oddNumbers


            # find the modulo of the totalSumProduct
            remainder = totalSumProduct % 10

            # subtract 10 from the remainder to get the check digit
            checkDigit = 10 - remainder
            print(" ")
            print("The checkDigit is "+str(checkDigit))
            print(" ")
            break
        else:
            print(" ")
            if( Number.isdigit() == True ): 
                print("***WARNING*** Input does not contain 11 digits, please try again.")
            else:
                print("***WARNING*** Input is not all digits, please try again.")
            Number = "A"


def doSelection(n):
    if ( n == 0 ) :
        print("Good by")
    elif ( n == 1 ):
        UPCBarcode()
    elif ( n == 2 ):
        ISBN10()
    elif ( n == 3 ):
        USBank()
    else:
        print(" ")
        print("***Warning*** Choice '"+str(n)+"' does not exit, please try again.")
        print(" ")

question1="Choose a selection: "
choice=9999

while choice > 0:
    print("0. End")
    print("1. UPC Barcode")
    print("2. ISBN 10 Barcode")
    print("3. US Bank check number")
    print(" ")
    choice = selectVersion(question1)


    if( choice.isdigit() == True ):
        choice = int(choice)
        doSelection(choice)
      
    else:
        print(" ")
        print("***Warning**** I don't understand choice '"+choice+"', please try again.")
        print(" ")

    
