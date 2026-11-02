

Sentence = input("Enter a sentence: ")

Position = int(input("Enter position for indexing: "))

Character = Sentence[Position]

Start_Index = int(input("Enter start index for slicing: "))
End_Index = int(input("Enter end index for slicing: "))

Sliced_String = Sentence[Start_Index:End_Index]

Uppercase = Sentence.upper()
Lowercase = Sentence.lower()

Word_To_Replace = input("Enter word to replace: ")
Replacement_Word = input("Enter replacement word: ")

After_Replace = Sentence.replace(Word_To_Replace, Replacement_Word)

Length = len(Sentence)

print(f"""
--- Processing Results ---

Character at position {Position} : '{Character}'
Sliced string [{Start_Index}:{End_Index}] : '{Sliced_String}'
Uppercase                    : {Uppercase}
Lowercase                    : {Lowercase}
After replace                : {After_Replace}
Length of sentence           : {Length}

==========================================
Analysis Complete!
==========================================
""")