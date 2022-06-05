# String calculator code
import re

def add(number):
    """Addition of two numbers

    Args:
        number (str): string containing numbers to add
    
    Returns:
        int: addition of two numbers
    """
    try:
        if number == " ":
            return 0
        else:
            numbers = number.split(",")
            nums_len = len(numbers)
            if nums_len <= 1 and "\n" not in numbers[0]:
                return int(numbers[0])
            ans = 0
            for nums in numbers:
                if "\n" in nums:
                    s = nums.split("\n")
                    for num in s:
                        ans += int(num)
                    continue
                ans += int(nums)
            return ans
    except:
        return "Input is not correct"
