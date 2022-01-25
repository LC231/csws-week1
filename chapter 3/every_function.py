languages = ['spanish','english','german','russian','mandarin']

print(len(languages))
languages.append('itlaian')
print(languages)
languages.insert(0,'japanese')
print(languages)
del languages[3]
print(languages)
languages.remove('russian')
print(languages)
popped_language = languages.pop()
print(languages)
print(popped_language)