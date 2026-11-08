text = input("Введите текст: ").split()
print(f"Общее количество слов: {len(text)}")
max_count = -1
max_len = 0
min_len = 999
for word in text:
    print(f"Слово {word} встречается: {text.count(word)} раз")
    if text.count(word) > max_count:
        max_count = text.count(word)
        max_frequency_word = word
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word 
    if len(word) < min_len:
            min_len = len(word)
            min_len_word = word       
print(f"Само часто встречающееся слово: {max_frequency_word}")        
print(f"Самое длинное слово: {max_len_word}")
print(f"Самое короткое слово: {min_len_word}")

print("После удаления слов менее 3 символов ")
max_len = 0
min_len = 999

for word in text:
    if len(word) < 3:
         text.remove(word)
         continue
    print(f"Слово {word} встречается: {text.count(word)} раз")
    if text.count(word) > max_count:
        max_count = text.count(word)
        max_frequency_word = word
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word 
    if len(word) < min_len:
            min_len = len(word)
            min_len_word = word  
print(f"Само часто встречающееся слово: {max_frequency_word}")        
print(f"Самое длинное слово: {max_len_word}")
print(f"Самое короткое слово: {min_len_word}")            