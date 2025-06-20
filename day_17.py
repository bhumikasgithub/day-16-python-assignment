'''#1
def evenly_divisible(a, b, c):
    total = 0  # Start with 0
    for num in range(a, b + 1):  # Loop from a to b inclusive
        if num % c == 0:         # Check if num is divisible by c
            total += num         # Add it to the total
    return total  # Return the final sum
print(evenly_divisible(1, 10, 20))  # ➞ 0
print(evenly_divisible(1, 10, 2))   # ➞ 30
print(evenly_divisible(1, 10, 3))   # ➞ 18

#2
def correct_signs(expression):
    return eval(expression)

# Test examples
print(correct_signs("3 < 7 < 11"))        # ➞ True
print(correct_signs("13 > 44 > 33 > 1"))  # ➞ False
print(correct_signs("1 < 2 < 6 < 9 > 3")) # ➞ True
'''
#3
def replace_vowels(text, char):
    vowels = "aeiouAEIOU"  # All vowels (both small and capital)
    result = ""
    
    for letter in text:
        if letter in vowels:
            result += char     # Replace vowel with given character
        else:
            result += letter   # Keep consonants as they are
    return result
print(replace_vowels("the aardvark", "#"))   # ➞ "th# ##rdv#rk"
print(replace_vowels("minnie mouse", "?"))   # ➞ "m?nn?? m??s?"
print(replace_vowels("shakespeare", "*"))    # ➞ "sh*k*sp**r*"

