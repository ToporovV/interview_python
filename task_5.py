# Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна
# передаваться фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции
# реализовать вложенную функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит
# средства в последний день каждого месяца, кроме первого и последнего. Например, при сроке вклада в
# 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно
# внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.


def calc_up(valid_percent_item, dep_term, up_amount):
    sum_up_amount = 0
    percent_for_month = valid_percent_item / 12
    for i in range(dep_term - 2):
        sum_up_amount += up_amount
        sum_up_amount += sum_up_amount / 100 * percent_for_month
    return sum_up_amount


def calc_deposit(begin_sum, dep_term, up_amount):
    dep_default_dict = {
        "begin_sum": begin_sum,
        "end_sum": None,
        "6": [5, 6, 7],
        "12": [6, 7, 8],
        "24": [5, 6.5, 7.5]
    }
    if begin_sum >= 100001:
        i = 2
    elif begin_sum >= 10001:
        i = 1
    elif begin_sum >= 1000:
        i = 0
    else:
        print("Сумма депозита не может быть меньше 1000.")
        return
    valid_percent_list = dep_default_dict.get(str(dep_term))
    valid_percent_item = valid_percent_list[i]
    percents_for_months = valid_percent_item / 12 * int(dep_term)
    end_sum = begin_sum + (begin_sum / 100 * percents_for_months) + calc_up(valid_percent_item, dep_term, up_amount)
    print(f'Cумма Вашего вклада на конец срока будет сотавлять {round(end_sum,2)} руб.')


# calc_deposit(100, 6, 200)
calc_deposit(1000, 6, 500)
calc_deposit(1050, 12, 1000)
# calc_deposit(1070, 24)
# calc_deposit(10001, 6)
# calc_deposit(1004501, 12)
# calc_deposit(1008701, 24)
# calc_deposit(10001, 6)