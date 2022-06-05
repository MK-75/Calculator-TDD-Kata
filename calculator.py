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
            delimit = re.search("^//", number)
            if delimit:
                number_string = re.split("^//", number)
                delimiter = re.search("^.", number_string[1])[0]
                numbers = re.sub("^.\\n", "", number_string[1], 1)
                ints = numbers.split(delimiter)
                ans = 0
                for num in ints:
                    ans += int(num)
                return ans
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
