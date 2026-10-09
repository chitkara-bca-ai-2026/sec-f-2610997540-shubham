Sentence = input("Enter a sentence: ")

Words = len(Sentence.split())

Vowels = 0
Consonants = 0
Digits = 0
Spaces = 0
Special_Characters = 0

for ch in Sentence:

    if ch.lower() in "aeiou":
        Vowels = Vowels + 1

    elif ch.isalpha():
        Consonants = Consonants + 1

    elif ch.isdigit():
        Digits = Digits + 1

    elif ch == " ":
        Spaces = Spaces + 1

    else:
        Special_Characters = Special_Characters + 1

Total_Characters = len(Sentence)

Total_Letters = Vowels + Consonants

Vowel_Percentage = (Vowels / Total_Letters) * 100

print(f"""
==========================================
          DOCUMENT ANALYSIS REPORT
==========================================

Sentence: {Sentence}
Total characters: {Total_Characters}

--- Character Breakdown ---

Words:              {Words}
Vowels:             {Vowels}
Consonants:         {Consonants}
Digits:             {Digits}
Spaces:             {Spaces}
Special characters: {Special_Characters}

--- Summary ---

Total letters:      {Total_Letters}
Vowel percentage:   {Vowel_Percentage:.1f}%

==========================================
Analysis Complete!
==========================================
""")