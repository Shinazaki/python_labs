minutes = int(input("Введите кол-во израссходованных минут: "))
sms = int(input("Введите кол-во израссходованных СМС: "))
internet = int(input("Введите кол-во израссходованных Мб интернета: "))
minutes_addition_price,sms_addition_price,internet_addition_price = 0,0,0
if minutes > 60:
    minutes_addition_price = (minutes - 60) * 0.89

if sms > 30:
    sms_addition_price = (sms - 30) * 0.59

if internet > 1000:
    internet_addition_price = (internet - 1000) * 0.79
      

    print(f"Базовая сумма тарификации:24,99р\nДоп сумма за минуты:{minutes_addition_price}\nДоп сумма за СМС:{sms_addition_price}\nДоп сумма за Интернет:{internet_addition_price}")    
    print(f"Итоговая суммва к выплате: {((24.99+minutes_addition_price+sms_addition_price+internet_addition_price)/100)*102}")