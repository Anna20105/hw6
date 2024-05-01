word= 'anna'
new_word =''
for a in word:
    new_word = a + new_word

if new_word == word:
    print('palindrom')
else:
    print(f'word = {word} is not palindrom')