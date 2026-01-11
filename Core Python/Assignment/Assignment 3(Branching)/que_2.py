# WAP to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter an alphabet: ")

vowels = "aeiouAEIOU"

if ch in vowels:
    print(ch, "is a vowel")
else:
    print(ch, "is a consonant")
