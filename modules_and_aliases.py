def reverse_string(s):
    """Function to reverse a string"""
    return s[::-1]

def capitalize_string(s):
    """Function to capitalize each word in a string"""
    return s.title()

import text_utils as tu

string_to_reverse = "hello world"
reversed_string = tu.reverse_string(string_to_reverse)
print(f"Reversed String: {reversed_string}")

# Example usage of capitalize_string function
string_to_capitalize = "hello world"
capitalized_string = tu.capitalize_string(string_to_capitalize)
print(f"Capitalized String: {capitalized_string}")
