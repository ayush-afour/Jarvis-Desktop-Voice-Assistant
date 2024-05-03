def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: The principal amount.
    :param rate: The interest rate (as a percentage).
    :param time: The time period over which the interest is calculated.
    :return: The interest amount.
    """
    interest = (principal * rate * time) / 100
    return interest

def calculate_total_amount(principal, rate, time):
    """
    Calculate the total amount after simple interest.

    :param principal: The principal amount.
    :param rate: The interest rate (as a percentage).
    :param time: The time period over which the interest is calculated.
    :return: The total amount (principal + interest).
    """
    interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + interest
    return total_amount

def calculate_principal_from_interest(interest, rate, time):
    """
    Calculate the principal amount given the interest.

    :param interest: The interest amount.
    :param rate: The interest rate (as a percentage).
    :param time: The time period over which the interest is calculated.
    :return: The principal amount.
    """
    principal = (interest * 100) / (rate * time)
    return principal