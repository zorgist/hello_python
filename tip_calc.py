cost = float(input("Введите сумму счета:"))
percent = int(input("Введите %чаевых:"))
tip = round((percent/100)*cost, 2)
total = round(cost+tip, 2)
print(f"\nЧаевые: {tip:,.2f} ₽")
print(f"Итого к оплате: {total:,.2f} ₽")