password = input("Введите пароль: ")

if len(password) <=16:
    assert False, "Слишком короткий"
if password.isalnum() == True:
    assert False, "Слабый пароль"
print("Надёжный пароль")    