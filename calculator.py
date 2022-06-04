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
        ans = 0
        if nums_len == 2:
            ans = int(numbers[0]) + int(numbers[1])
        elif nums_len == 3:
            ans = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
        elif nums_len == 4:
            ans = int(numbers[0]) + int(numbers[1]) + int(numbers[2]) + int(numbers[3])
        return ans
