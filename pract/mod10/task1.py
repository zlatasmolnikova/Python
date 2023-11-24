import re

def check_password(password):

    """
    Checks the validity of a password based on specific criteria.

    Args:
    password (str): The password to be validated.

    Returns:
    bool: True if the password meets the criteria, False otherwise.

    Examples:
    >>> check_password('rtG&3FG#Tr^e')
    True
    >>> check_password('a^A1@*@1Aa')
    True
    >>> check_password('oF^a1D@y5%e6')
    True
    >>> check_password('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    >>> check_password('weakpassword')
    False
    >>> check_password('пароль')
    False
    >>> check_password('password')
    False
    >>> check_password('qwerty')
    False
    >>> check_password('lOngPa$$W0Rd')
    False
    """
    
    if re.match(r'^(?=.*[a-z].{2,})(?=.*\d)(?=.*[^,.!?])(?=(.*[^\w\s]){3,})(?=.*[^\w\s\d]).{8,}$', password):
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
