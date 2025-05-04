import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = [] # перечень товаров в чеке
        self.__number_items = 0 # количество товаров в чеке
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70} # товары магазина и их стоимость
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10} # налоговая ставка на товары

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if not name or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1


    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    
    def check_amount(self):
        total = []
        for items in self.__name_items:
            if items in self.__item_price.keys():
                total.append(self.__item_price[items])
        
        if len(total) > 10:
            result = sum(total) * 0.9
        else:
            result = sum(total)

        return result


    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for items in self.__name_items:
            if self.__tax_rate[items] == 20:
                twenty_percent_tax.append(items)
                total.append(self.__item_price[items])
        
        if len(total) > 10:
            result = (sum(total) * 0.9) * 0.2
        else:
            result = sum(total) * 0.2

        return result


    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for items in self.__name_items:
            if self.__tax_rate[items] == 10:
                ten_percent_tax.append(items)
                total.append(self.__item_price[items])
        
        if len(total) > 10:
            result = (sum(total) * 0.9) * 0.1
        else:
            result = sum(total) * 0.1
        
        return result


    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
    
    @staticmethod
    def get_telephone_number(telephone_number):

        if not telephone_number.isdigit():
            raise ValueError('Необходимо ввести цифры')
        elif len(telephone_number) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'


    @staticmethod
    def get_date_and_time():
        date_and_time = []
        date = []
        now = datetime.datetime.now()
        functions_add_data_in_date = [
            lambda x: date.append(['часы', x.hour]),
            lambda x: date.append(['минуты', x.minute]),
            lambda x: date.append(['день', x.day]),
            lambda x: date.append(['месяц', x.month]),
            lambda x: date.append(['год', x.year])
        ]
        for func in functions_add_data_in_date:
            func(now)

        for items in date:
            date_and_time.append(f'{items[0]} : {items[1]}')

        return print(date_and_time)


register = OnlineSalesRegisterCollector()


register.add_item_to_cheque('чипсы')
register.add_item_to_cheque('кола')
register.add_item_to_cheque('молоко')
register.delete_item_from_check('кола')

print("Сумма чека:", register.check_amount())

print("Налог 20%:", register.twenty_percent_tax_calculation())  # только чипсы
print("Налог 10%:", register.ten_percent_tax_calculation())      # только молоко
print("Общий налог:", register.total_tax())

print("Телефон:", OnlineSalesRegisterCollector.get_telephone_number("9876543210"))

OnlineSalesRegisterCollector.get_date_and_time()