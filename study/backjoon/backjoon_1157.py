word = input().upper()
word_set = list(set(word))

word_dict = {}
for spell in word_set:
    word_dict[spell] = word.count(spell)

word_list = [
    key 
    for key,value in word_dict.items() 
    if max(word_dict.values()) == value
    ]

if len(word_list) > 1:
    print('?')
else:
    print(word_list[0])