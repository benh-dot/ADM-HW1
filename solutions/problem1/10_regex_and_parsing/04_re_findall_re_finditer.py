import re

consonants = "qwrtypsdfghjklzxcvbnm"
vowels = "aeiou"
pattern = rf'(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])'

matches = re.findall(pattern, input(), flags=re.IGNORECASE)
print("\n".join(matches) if matches else -1)
