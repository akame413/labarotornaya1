money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0

while True:
    diff = spend - salary #ежемесячная разница трат и дохода
    if diff > money_capital: #разница будет больше финансовой подушки
        break

    month += 1 # +месяц
    money_capital -= diff # -разница
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", month)
