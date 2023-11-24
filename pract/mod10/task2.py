import re

def is_valid_date(input_string):

    """
    Checks string is a date in one of several formats.

    Args:
    password (str): The date to be validated.

    Returns:
    bool: True if the date meets the criteria, False otherwise.

    Examples:
    >>> is_valid_date('20 января 1806')
    True
    >>> is_valid_date('1924, July 25')
    True
    >>> is_valid_date('26/09/1635')
    True
    >>> is_valid_date('3.1.1506')
    True
    >>> is_valid_date('31.1.1144')
    True
    >>> is_valid_date('31.2.2004')
    False
    >>> is_valid_date('25.08-1002')
    False
    >>> is_valid_date('декабря 19, 1838')
    False
    >>> is_valid_date('8.20.1973')
    False
    >>> is_valid_date('Jun 7, -1563')
    False
    >>> is_valid_date('31 июня 2023')
    False
    >>> is_valid_date('29 февраля 2015')
    False
    >>> is_valid_date('7 May, 2056')
    False
    >>> is_valid_date('31 июня 2015')
    False
    """
    
    date_formats = [
        r'(([0-2])?[0-8]|19)[.]0?2[.]\d{4}', # день.месяц.год
        r'(([0-2])?[0-9]|30)[.]0?(?:4|6|9|11)[.]\d{4}',
        r'(([0-2])?([0-9]|30|31))[.]0?(?:1|3|5|7|8|10|12)[.]\d{4}',
        
        r'\d{4}[.]0?2[.](([0-2])?[0-8]|19)', # год.месяц.день
        r'\d{4}[.]0?(?:4|6|9|11)[.](([0-2])?[0-9]|30)',
        r'\d{4}[.]0?(?:1|3|5|7|8|10|12)[.](([0-2])?[0-9]|30|31)',

        r'(([0-2])?[0-8]|19)[/]0?2[/]\d{4}', # день/месяц/год
        r'(([0-2])?[0-9]|30)[/]0?(?:4|6|9|11)[/]\d{4}',
        r'(([0-2])?([0-9]|30|31))[/]0?(?:1|3|5|7|8|10|12)[/]\d{4}',
        
        r'\d{4}[/]0?2[/](([0-2])?[0-8]|19)', # год/месяц/день
        r'\d{4}[/]0?(?:4|6|9|11)[/](([0-2])?[0-9]|30)',
        r'\d{4}[/]0?(?:1|3|5|7|8|10|12)[/](([0-2])?[0-9]|30|31)',

        r'(([0-2])?[0-8]|19)[-]0?2[-]\d{4}', # день-месяц-год
        r'(([0-2])?[0-9]|30)[-]0?(?:4|6|9|11)[-]\d{4}',
        r'(([0-2])?([0-9]|30|31))[-]0?(?:1|3|5|7|8|10|12)[-]\d{4}',
        
        r'\d{4}[-]0?2[-](([0-2])?[0-8]|19)', # год-месяц-день
        r'\d{4}[-]0?(?:4|6|9|11)[-](([0-2])?[0-9]|30)',
        r'\d{4}[-]0?(?:1|3|5|7|8|10|12)[-](([0-2])?[0-9]|30|31)',

        r'(([0-2])?[0-8]|19)\s(февраля)\s\d{4}', #день месяц_rus год  
        r'(([0-2])?[0-9]|30)\s(?:апреля|июня|сентября|ноября)\s\d{4}',
        r'(([0-2])?[0-9]|30|31)\s(?:января|марта|мая|июля|августа|октября|декабря)\s\d{4}',

        r'(?:February|Feb)\s(([0-2])?[0-8]|19),\s\d{4}', #Месяц/мес_eng день, год   
        r'(?:April|June|September|November|Apr|Jun|Sep|Nov)\s(([0-2])?[0-9]|30),\s\d{4}',
        r'(?:January|March|May|July|August|October|December|Jan|Mar|May|Jul|Aug|Oct|Dec)\s(([0-2])?[0-9]|30|31),\s\d{4}',

        r'\d{4},\s(?:February|Feb)\s(([0-2])?[0-8]|19)', #год, Месяц/мес_eng день    
        r'\d{4},\s(?:April|June|September|November|Apr|Jun|Sep|Nov)\s(([0-2])?[0-9]|30)',
        r'\d{4},\s(?:January|March|May|July|August|October|December|Jan|Mar|May|Jul|Aug|Oct|Dec)\s(([0-2])?[0-9]|30|31)'    
    ]
    for date_format in date_formats:
        if re.match(date_format, input_string):
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
