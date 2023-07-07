""" 2. Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии """
from decimal import Decimal

names = ['Иван', 'Дмитрий', 'Мария']
salary = [100, 120, 140]
bonus = ['10.2%', '14.3%', '15.6%']


extra_salary = {name: Decimal(salary) * Decimal(bonus.replace('%', '')) for name, salary, bonus in zip(names, salary, bonus)}

for name, award in extra_salary.items():
    print(f"{name} => {award}")

