def to_upper(string):
    """функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return string.upper()

def capitalize_words(string):
    """
    Функция, которая делает заглавными первые буквы каждого слова в строке.

    :param string: строка, которую нужно обработать
    :type string: str
    :return: строка с заглавными первыми буквами каждого слова
    :rtype: str
    """
    return ' '.join(word.capitalize() for word in string.split())