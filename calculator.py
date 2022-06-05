# String calculator code
import re

class NegativeNumberError(Exception):
    """Raised when negative number is found
    
    Attributes:
        numbers: list of negative numbers
    """
    def __init__(self, numbers, message = "negatives not allowed - "):
        self.numbers = numbers
        self.message = message + numbers 
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.message}'

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
                flag = 0
                number_string = re.split("^//", number)
                delimiter = re.search("^.", number_string[1])[0]
                numbers = re.sub("^.\\n", "", number_string[1], 1)
                ints = numbers.split(delimiter)
                ans = 0
                negative = []
                for num in ints:
                    if int(num) < 0:
                        flag = 1
                        negative.append(num)
                        continue
                    ans += int(num)
                if flag:
                    x = ",".join(negative)
                    raise NegativeNumberError(x)
                return ans
            else:
                flag = 0
                numbers = number.split(",")
                nums_len = len(numbers)
                if nums_len <= 1 and "\n" not in numbers[0]:
                    return int(numbers[0])
                ans = 0
                negative_nums = []
                for nums in numbers:
                    if "\n" in nums:
                        s = nums.split("\n")
                        print(s)
                        for num in s:
                            if int(num) < 0:
                                flag = 1
                                negative_nums.append(str(num))
                                continue
                            ans += int(num)
                        continue
                    if int(nums) < 0:
                        flag = 1
                        negative_nums.append(str(nums))
                    ans += int(nums)
                if flag:
                    x = ",".join(negative_nums)
                    raise NegativeNumberError(x)
                return ans
    except ValueError:
        return "Input is not correct"
    except TypeError:
        return "Input is not correct"
