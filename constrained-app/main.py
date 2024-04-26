# Restriction: can use functions or built-in functions, lists, diccionaries
# exceptions and library functions

import re

def main():
    persons = []
    while (option:=get_option()) != '5':
        search_person(option, persons)
        add_person(option, persons)
        pass

def get_option() -> str:
    with open('restricted-app/text/options.txt') as menu:
        option = input(menu.read())
    return option

def search_person(option, persons):
    # search by filters or search by any match on args
    if option != '1': return

def add_person(option, persons:list[dict]):
    if option != '2': return
    ## help-hint: args '{key}={value}', run=2131242* name=edu
    if is_input_valid(user_input:=input()) and run_available(user_input, persons):
        if (person:=get_person(user_input)) is not None:
            persons.append(person)
        print(get_person(user_input))
    else:
        print('not available')

def is_input_valid(input:str):
    # is required to enter a run on the input
    # the signature of the args is by kwargs '{key}={value}'
    run_required = r"(?=.*(\brun=\d{1,3}(?:\.\d{1,3}){2}-[\dkK]\b))"
    args_pattern = r"(\b[a-z]+=([a-zA-Z]+|(\d{1,3}(\.\d{1,3}){2}-[\dkK]))\b\s*)*"
    return re.fullmatch(f'{run_required}{args_pattern}', input)

def run_available(input:str, persons:list[dict]):
    input_run = re.findall(r'\brun=(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])', input)[-1]
    print(f'persons:{persons}')
    return not any((person.get('run') == input_run) for person in persons)

def get_person(input:str):
    #restrict the structure of a person information by {run*, name, lastname, e-mail}
    person = {key:None for key in ['run', 'name', 'lastname', 'e-mail']}
    kwarg_pattern = re.compile(r"\b([a-z]+)=([a-zA-Z]+|(\d{1,3}(?:\.\d{1,3}){2}-[\dkK])+)\b")
    matches = []
    for match in kwarg_pattern.finditer(input):
        key, value = match.groups()[0:2]
        if key in person:
            person[key] = value
        else:
            print(f'invalid key! <{key}:{value}>')
            return None
    return person

main()