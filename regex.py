import re

pattern = re.compile(r'\+370\s\d{3}\s\d{5}%')

tekstas = "+370 600 12456"

rezultatas = pattern.search(tekstas)

print(rezultatas)



def split_names(name):
    pattern = re.compile(r'^([A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
    result = pattern.search(name)
    if result:
        print(f'Visa eilutė: {result.group(0)}')
        print(f'Kreipinys: {result.group(1)}')
        print(f'Vardas: {result.group(2)}')
        print(f'Pavardė: {result.group(3)}')
        print('----------------------------------')
        print(result.group())
        print(result.groups())
    else:
        print('Įvestis neatitinka šablono')

split_names('Mr. Clint Eastwood')