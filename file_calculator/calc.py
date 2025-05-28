import logging
logging.basicConfig(
  filename='calculator.log',
  level=logging.INFO,
  format='%(asctime)s -%(levelname)s - %(message)s'
)

a = float(input("Введите первое число: "))
operation = input("Выберите операцию(+, -, *, /): ")
b = float(input("Введите второе число: "))
logging.info(f"Пользователь ввел: {a} {operation} {b}")

if operation == "+":
  result = a+b
elif operation == "-":
  result = a-b
elif operation == "*":
  result = a*b
elif operation == "/":
 if b != 0:
  result = a/b
 else:
   result = "Ошибка: деление на ноль"
   logging.warning("Попытка деления на ноль")
else: 
   result = "Неверная операция"
   logging.error(f"Неверная операция: {operation}")    
print("Результат: ", result)
logging.info(f"Результат: {result}")

      
