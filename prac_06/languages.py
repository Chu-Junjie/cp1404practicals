"""
languages
Estimate: 20 minutes
Actual:   20 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

# python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
# ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
# visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
# print(python)

languages = []
languages.append(ProgrammingLanguage("Python", "Dynamic", True, 1991))
languages.append(ProgrammingLanguage("Ruby", "Dynamic", True, 1995))
languages.append(ProgrammingLanguage("Visual Basic", "Static", False, 1991))

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
