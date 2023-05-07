#1
word = input('Введіть слово: ')
if word == word[::-1]:
  print('+')
else:
  print('-')
#2
text = input('Введіть текст: ')
word = input('Введіть слово для пошуку: ')
if word in text:
  print('YES')
else:
  print('NO')
#3
str = input('Введіть рядок: ')
if str.startswith('abc'):
    str = 'www'
else:
    str = str + 'qqq'
print(str)
#4
text = input('Введіть текст: ')
text = ''.join(filter(lambda x: not x.isdigit(), text))
print(text)
#5
email = input('Введіть електронну пошту: ')
if '@' in email and '.' in email:
  print('YES')
else:
  print('NO')