
programing_languages = ["Python", "C#", "Java", "Javascript"]

result = type(programing_languages)
result = programing_languages[1]
result = programing_languages
result = programing_languages[:2]

#güncelleme
programing_languages[-1] = "Php"
result = programing_languages
result = len(programing_languages)
result = programing_languages + ["Go","Delphi"]

result = "C#" in programing_languages 
result = "React" in programing_languages 

del programing_languages[3]

for language in programing_languages:
    print(language)


print(result)