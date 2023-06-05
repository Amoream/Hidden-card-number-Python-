"""
Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent “4444444444444444”, then it should return “4444”.
"""

def hide_card_number():

    hidden_code = ""

    #Retrieve the card number of the user
    card_num = input('Enter your credit card number: ')

    #Add the digits into the empty string as * and overwrite the last * by the digits of the card's numbers
    for digit in card_num:
        hidden_code += '*'
    hidden_code += card_num[-4:]

    return hidden_code


hide_the_code = hide_card_number()
print(hide_the_code)
