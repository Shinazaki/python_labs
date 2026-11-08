password = input("Введите пароль: ")

if len(password) <=16:
    print(f"Вы ввели пароль:{password}, пароль слишком короткий")
if password.isalnum() == True:
    print(f"Вы ввели пароль:{password}, пароль слабый пароль")
print(f"Вы ввели пароль:{password}, надёжный пароль")    