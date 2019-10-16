import json
strings = json.loads(open("strings.json", "r").read())

for lang in strings:
    print(lang['country'] + ": " + lang['string'])
