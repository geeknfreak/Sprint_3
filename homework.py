import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


#1. Напиши геттеры

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

#2. Добавь товар в чек

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError ('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        if name not in self.__item_price:
            raise NameError ('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

#3. Удали товар из чека

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError ('Позиция отсутствует в чеке')
        
        self.__name_items.remove(name)
        self.__number_items -=1

#4. Посчитай общую стоимость товаров
    
    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])

        if self.__number_items > 10:
            return sum(total) * 0.9
        else: return sum(total)

#5. Вычисли НДС для товаров со ставкой 20%

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])

            if self.__number_items > 10:
                total_sum = sum(total) * 0.9
            else: total_sum = sum(total)

        return total_sum * 0.2

#6. Вычисли НДС для товаров со ставкой 10%

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])

            if self.__number_items > 10:
                total_sum = sum(total) * 0.9
            else: total_sum = sum(total)

        return total_sum * 0.1

#7. Посчитай общую сумму налогов
    
    def total_tax(self):
            return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
 
#8. Верни номер телефона покупателя

    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        str_number = str(telephone_number)
        if len(str_number) < 10:
            raise ValueError ('Необходимо ввести 10 цифр после "+7"')

        return f'+7{str_number}'


# Создаем экземпляр кассы
cash_register = OnlineSalesRegisterCollector()

# Добавляем товары
cash_register.add_item_to_cheque('чипсы')
cash_register.add_item_to_cheque('кола')
cash_register.add_item_to_cheque('молоко')

# Получаем информацию
print(cash_register.name_items)        # ['чипсы', 'кола', 'молоко']
print(cash_register.number_items)       # 3
print(cash_register.check_amount())     # 50 + 100 + 55 = 205
print(cash_register.total_tax())        # Сумма НДС

# Получаем номер телефона
print(OnlineSalesRegisterCollector.get_telephone_number(1234567890))  # +71234567890
