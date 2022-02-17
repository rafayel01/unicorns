vowel = ['a', 'e', 'i', 'o', 'u']
vowel_and_consonant = 'y'

inp = input("Enter a letter: ")

if inp in vowel:
    print(f'{inp} is a vowel letter')
elif inp == vowel_and_consonant:
    print(f'{inp} is a vowel and consonant letter')
else:
    print(f'{inp} is a consonant letter')
