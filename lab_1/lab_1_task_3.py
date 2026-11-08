money = int(input("Введите кол-во денег: "))
currency = [100,50,10,5,2,1]

for nominal in currency:
    count = money // nominal
    money %= nominal
    print(f"{nominal}:{count}")