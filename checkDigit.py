import sys 
"""checkDigit.py: Determines the check Digit from different methods."""
"""This could be done by a call on the console or a call from a web browser"""
"""From the consoule  user>python checkDigit.py"""

"""From the web:     python checkDigit.py <barcodeNumber> <barcodeList>"""
"""Return from Wea:  <status>|<checkdigit>|ISBN10|ISBN13|USBank|UPC """
"""Note at the end after the checkDigit it list all the possible options, this is so it """
"""automatically populates a pull down list on the web site"""

"""Web Example   call: python checkdigit.py 12345678901 ISBN10 """
"""Web Example return: GOOD|2|ISBN10|ISBN13|USBank|UPC  """ 

__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"

def selectVersion(question):
    if (sys.version_info > (3,0)):
        # python3 code
        selection = input(question)
    else:
        selection = raw_input(question)

    return selection


def ISBN10(Number):
    i = 0
    sumProduct = 0
    while( i < 9 ):
        theProduct = 10-i
        sumProduct = sumProduct + int(Number[i])*theProduct
        i = i +1
    checkDigit = 11 - sumProduct % 11
    if( checkDigit == 11 ):
        checkDigit = 0
    if( checkDigit == 10 ):
        checkDigit = "X"

    return checkDigit            
    
def USBank(Number):
    # We will start from the left and use the weight 7, 5, 3, 2
    # Pad the account number with 0 for a length of 12
    Number = format(Number, "0>12s")
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
    
    return checkDigit

def ISBN13(Number):
    lenNumber = len(Number)
           
    # Add the even number of digits 
    i = 1
    evenNumbers=0
    while( i < lenNumber ):
        evenNumbers = evenNumbers + int(Number[i])
        i = i +2
    evenNumbers = evenNumbers*3
    
    # sum odd numbers
    i = 0
    oddNumbers=0
    while( i < lenNumber ):
        oddNumbers = oddNumbers + int(Number[i])
        i = i +2
    
    # Add the evenNumbers to the Odd Numbers
    totalSumProduct = evenNumbers + oddNumbers


    # find the modulo of the totalSumProduct
    remainder = totalSumProduct % 10

    # subtract 10 from the remainder to get the check digit
    checkDigit = 10 - remainder
    if( checkDigit == 10 ):
        checkDigit = 0
    return checkDigit

def UPCBarcode(Number):
    lenNumber = len(Number)
           
    # Add the odd number of digits 
    i = 0
    oddNumbers=0
    while( i < lenNumber ):
        oddNumbers = oddNumbers + int(Number[i])
        i = i +2
    oddNumbers = oddNumbers*3
            
    # sum even numbers
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
    if( checkDigit == 10 ):
        checkDigit = 0

    return checkDigit

def doSelection(n,Number,methodType):
    checkDigit = 0
    if ( n == 0 ) :
        print("Good by")

    else:
        if( methodType == "PRINT" ):
            Number = "A"
            print( welcomeStatementList[n] )
        while ( Number.isdigit() == False or methodType == "CALL") :
            if( methodType == "PRINT" ):
                if( digitLimitList[n] >= 0 ):
                    Number = selectVersion("Input "+str(digitLimitList[n])+" numbers: ")
                else:
                    Number = selectVersion("Input no more than "+str(abs(digitLimitList[n]))+" numbers: ")
            if( Number.isdigit() == True and 
                ( (len(Number) == digitLimitList[n] and digitLimitList[n] > 0) or 
                    (len(Number) <= abs(digitLimitList[n]) and digitLimitList[n] < 0) ) ):  
                if ( n == 1 ):
                    checkDigit = UPCBarcode(Number)
                elif ( n == 2 ):
                    checkDigit = ISBN10(Number)
                elif ( n == 3 ):
                    checkDigit = ISBN13(Number)
                elif ( n == 4 ):
                    checkDigit = USBank(Number)
                else:
                    checkDigit = "ERROR: Choice '"+str(n)+"' does not exist."
                
                if( methodType == "PRINT" ):
                    # print response
                    print(" ")
                    print("Check Digit is: ")
                    print(checkDigit)
                    print(" ")
                if(methodType == "CALL"  ):
                    break
            else:
                if( Number.isdigit() == True ): 
                    if( digitLimitList[n] < 0 ):
                        checkDigit = "ERROR: Input contains more than "+str( abs(digitLimitList[n]) )+" numbers."
                    else:
                        checkDigit = "ERROR: Input does not contain "+str( digitLimitList[n] )+" numbers."
                else:
                        checkDigit = "ERROR: Input is not all digits."
                Number = "A"
           
                if( methodType == "PRINT" ):
                    # print response to error  
                    print(" ")
                    print(checkDigit)
                    print(" ")
                if(methodType == "CALL"  ):
                    break
    return checkDigit


# Start of main body
question1="Choose a selection: "
choice=9999

# dictionary list

isbn10 = {
    'welcomeStatement': 'Calculationg ISBN10',
    'digitLimit': 9, }
# Barcode types
barcodeList="ISBN10|ISBN13|USBank|UPC"

#  Welcome Statement for each barcode
welcomeStatementList = [
    "Good by",
    "Calculating UPC barcode check digit:",
    "Calculating ISBN 10 barcode check digit:",
    "Calculating ISBN 13 barcode check digit:",
    "Calculating US Bank account number Check digit:"
    ]

# digitLimit for each barcode
digitLimitList = [
    0,
    11,
    9,
    12,
    -12
    ]


#check to see if this is a call
if( len(sys.argv) > 2):
    #this is a web call
    #check if all numbers
    if( sys.argv[1].isdigit() == True ):
        checkDigit = ""
        if( sys.argv[2] == 'ISBN10' ):
            n = 1
        elif( sys.argv[2] == 'ISBN13' ):
            n = 2
        elif( sys.argv[2] == 'UPC' ):
            n = 3
        elif( sys.argv[2] == 'USBank' ):
            n = 4
        else:
            checkDigit = "No method for "+sys.argv[2] 
        if(checkDigit == ""):
          checkDigit = doSelection(n,sys.argv[1],"CALL")
    else:
        checkDigit = "Barcode is not all numbers"

    status = "GOOD"
    if( str(checkDigit).isdigit() == False ):
        status = "BAD"
    if( sys.argv[1] == "0" and sys.argv[2] == "0" ):
        checkDigit = "" 
    value1 = status+"|"+str(checkDigit)+"|"+barcodeList
    print(value1)
else:

    while choice > 0:
        print("0. End")
        print("1. UPC Barcode")
        print("2. ISBN 10 Barcode")
        print("3. ISBN 13 Barcode")
        print("4. US Bank check number")
        print(" ")
        choice = selectVersion(question1)


        if( choice.isdigit() == True ):
            choice = int(choice)
            checkDigit = doSelection(choice,"","PRINT")
      
        else:
            print(" ")
            print("***Warning**** I don't understand choice '"+choice+"', please try again.")
            print(" ")

    
