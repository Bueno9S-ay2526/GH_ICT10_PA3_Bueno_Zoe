# smthn
from pyscript import display, document


def countries_capital(e):
    document.getElementById('result').innerHTML = ' ' #deletes content in result
    user_input = document.getElementById('user_input').value.capitalize().strip() #removes sapces and makes it so the first letter of each word is capitalized
    countries ={
        'Finland':'Helsinki',
        'Philippines':'Manila',
        'Mongolia':'Ulaanbaatar',
        'Egypt':'Cairo',
        'UK':'London',
        'Denmark':'Copenhagen',
        'Norway':'Oslo',
        'Luxembourg':'Luxembourg'
    }

    countries_checker = user_input in countries

    display_message = (f"This countries's Capital is not on the list.",f"Capital of {user_input} is {countries}.")

    display(display_message[countries_checker], target='result')