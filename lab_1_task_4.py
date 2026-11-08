string = input("Введите строку: ")
string = string.lower()
if string == string[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")    
