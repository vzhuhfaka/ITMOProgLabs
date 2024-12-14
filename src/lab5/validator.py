import codecs
import re


def clear_file(path_):
    """
    Функция для очистки содержимого файла
    """
    with open(path_, 'w'):
        pass


def format_data(data_):
    """
    Функция, которая форматирует данные

    Пример: '56342;2;+4-989-234-56' -> ['56342', '2', '+4-989-234-56']
    """
    return [i.split(';') for i in data_]


def read_data(path_):
    """
    Функция, которая читает данные из файла
    """
    with codecs.open(path_, 'r', 'utf-8') as f:
        return [i.strip() for i in f.readlines()]


def write_types_data(path_, data_, type_):
    """
    Записывает выбранный тип данных в файл
    """
    with codecs.open(path_, 'a+', 'utf-8') as f:
        if type_ == str:
            f.write(data_)
        if type_ == list:
            for i in data_:
                if isinstance(i, list):
                    f.write(str(i)[1:-1] + '\n')
                else:
                    f.write(str(i)+'\n')


def check_phone_number(phone_number_):
    """
    Функция, которая проверяет валидность номера телефона, используя регулярное выражение,
    которое соответствует формату "+x-xxx-xxx-xx-xx"

    Пример: phone_number="+7-123-456-78-90" -> True
    """
    regex = r'\+\d-\d{3}-\d{3}-\d{2}-\d{2}'

    if re.fullmatch(regex, phone_number_):
        return True
    return False


def check_address(address_):
    """
    Функция, которая проверяет валидность адреса

    Пример: address="Великобритания. Англия. Лондон. Бейкер-стрит" -> True
    """
    split_address = address_.split('.')
    if len(split_address) == 4:
        return True
    return False


def dict_to_string(dict_):
    """
    Функция, которая преобразует словарь в строку

    Пример: dict={'a': 2, 'b': 3} -> 'a x2, b x3'
    """
    res = ''
    for key, value in dict_.items():
        res += f'{key} x{value}, '
    return res[:-2]


def count_repetitive(data_):
    """
    Функция, считающая количество повторяющихся элементов, которые встречаются в списке

    Пример: list=[1, 2, 3, 3, 4, 1] -> {1: 2, 2: 1, 3: 2, 4: 1}
    """
    repetition = {}
    for i in data_:
        if i in repetition.keys():
            repetition[i] += 1
        else:
            repetition[i] = 1
    return repetition


def sort_by_priority(data_):
    """
    Функция, которая сортирует заказы по приоритету
    """
    priority = {'MAX': 2, 'MIDDLE': 1, 'LOW': 0}
    sorted_data = sorted(data_, key=lambda x: priority[x[5]], reverse=True)
    return sorted_data


def sort_by_country(data_):
    """
    Функция, которая сортирует заказы по стране в нужном порядке
    """
    def country_key(x):
        """
        Ключ для сортировки
        """
        country = x[3].split('.')[0]
        if country == 'Россия':
            return 0
        else:
            return 1

    first_russia = sorted(data_, key=country_key)  # список, где заказы с России в начале

    last_russia_index = 0  # последнее вхождение заказа, в котором адрес Россия

    # Находим last_russia_index
    for i in first_russia:
        if i[3].split('.')[0] == 'Россия':
            last_russia_index = first_russia.index(i)
        else:
            break

    russia = first_russia[:last_russia_index+1]  # часть с Россией
    other = sorted(first_russia[last_russia_index+1:], key=lambda x: x[3])  # остальные страны, отсортированные в алфавитном порядке
    full = russia + other  # объединяем

    return full


def sort_order(data_):
    """
    Функция, которая сортирует заказы по правильному порядку стран(первая Россия, потом другие страны в алфавитном порядке),
    а после чего сортирует заказы по приоритету
    """
    countries = {}  # словарь с заказами для каждой страны
    orders = sort_by_country(data_)

    for order in orders:
        country = order[3].split('.')[0]  # получаем страну в заказе

        # Добавляем в словарь заказ, в зависимости от страны
        if country in countries.keys():
            countries[country].append(order)
        else:
            countries[country] = [order]

    # В словаре сортируем заказы в каждой стране по приоритету
    for key, value in countries.items():
        countries[key] = sort_by_priority(value)

    sorted_orders = []

    # Объединяем все отсортированные заказы в один список
    for key, value in countries.items():
        sorted_orders += value

    return sorted_orders


class Validator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        """
        Главная функция валидатора, которая возвращает список валидных и невалидных заказов
        """
        data_ = self.data
        orders_valid = []
        orders_invalid = []
        for order in data_:
            flag = True  # флаг для проверки валидности заказа

            # Получим каждый элемент
            order_number = order[0]
            products = order[1]
            surname = order[2]
            address = order[3]
            phone_number = order[4]
            priority = order[5]

            if not check_phone_number(phone_number):
                flag = False
                error_string = f'{order_number};2;{phone_number if phone_number else 'no data'}'
                orders_invalid.append(error_string)

            if not check_address(address):
                flag = False
                error_string = f'{order_number};1;{address if address else 'no data'}'
                orders_invalid.append(error_string)

            products_dict = count_repetitive(products.split(', '))  # считаем количество повторяющихся продуктов
            products_repetitive = dict_to_string(products_dict)  # итоговая строка с продуктами, учитывая повторения

            if flag:
                orders_valid.append([order_number, products_repetitive, surname, address, phone_number, priority])

        orders_valid_ = sort_order(orders_valid)  # сортируем список всех заказов
        return [orders_valid_, orders_invalid]


if __name__ == '__main__':
    NON_VALID_PATH = 'non_valid_orders.txt'
    ORDER_COUNTRY_PATH = 'order_country.txt'
    clear_file(ORDER_COUNTRY_PATH)
    clear_file(NON_VALID_PATH)
    data_ = read_data('orders.txt')
    data_format = format_data(data_)

    obj = Validator(data_format)
    v = obj.validate()

    write_types_data(ORDER_COUNTRY_PATH, v[0], list)
    write_types_data(NON_VALID_PATH, v[1], list)
