def is_symmetric(input_string):
    reverse_string = input_string[::-1]
    if reverse_string == input_string:
        return True
    else:
        return False

print("Checking if racecar is a palindrome.")
print(is_symmetric("racecar"))
print("Testing is_symmetric on input 'racecar'")
assert is_symmetric("racecar") == True, "The code should show true."
print("PASSED")

print("Checking if batman is a palindrome.")
print(is_symmetric("batman"))
print("Testing is_symmetric on input 'batman'")
assert is_symmetric("batman") == False, "The code should show false."
print("PASSED")
