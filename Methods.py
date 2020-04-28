def capital_cities(state):
    if state == 'NSW':
        capital = 'Sydney'
        print(f'Capital of {state} is : {capital}')
    elif state == 'Victoria':
        capital = 'Melbourne'
        print(f'Capital of {state} is : {capital}')
    elif state == 'Queensland':
        capital = 'Brisbane'
        print(f'Capital of {state} is : {capital}')
    else:
        print(f'Hey! there is no such state called {state} in Australia')


capital_cities('Andhra')
