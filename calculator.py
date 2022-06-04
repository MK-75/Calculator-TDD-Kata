# String calculator code

def add(number):
    """Addition of two numbers

    Args:
        number (str): string containing numbers to add
    
    Returns:
        int: addition of two numbers
    """
    if number == " ":
        return 0
    else:
        numbers = number.split(",")
        nums_len = len(numbers)
        if nums_len <= 1:
            return int(numbers[0])
    
        ans = int(numbers[0]) + int(numbers[1])
        return ans
