SURNAME_INDEX = 0
FIRSTNAME_INDEX = 1
ADULT_AGE = 18


def create_person(surname, firstname, age):
    return surname, firstname, age


def get_names_of_adult_persons(persons):
    return [f'{person[SURNAME_INDEX]} {person[FIRSTNAME_INDEX]}'
            for person in persons if person[2] >= ADULT_AGE]

# The code in line 15 is a Python conditional statement that ensures a script runs only when executed directly and not when imported as a module.
if __name__ == '__main__':
    persons_list = []

    mike = create_person('Davis', 'Mike', '25')
    john = create_person('Roberts', 'John', 16)
    lee = create_person('Willams', 46, 'Lee')

    persons_list.append(mike)
    persons_list.append(john)
    persons_list.append('lee')

    print(get_names_of_adult_persons(persons_list))




# Below is an examply of an implementation of a python function for reference

# def my_function(num1: int, num2: int, text: str) -> int:
#    """
#    This function takes two integers and a string, then returns an integer.
#    
#    Parameters:
#    num1 (int): The first integer input.
#    num2 (int): The second integer input.
#    text (str): A string input.
#    
#    Returns:
#    int: An integer result.
#    """
#    # Example operation: return the sum of numbers multiplied by the length of text
#    return (num1 + num2) * len(text)

# Example usage
# result = my_function(3, 5, "hello")
# print(result)  # Output: (3 + 5) * 5 = 40