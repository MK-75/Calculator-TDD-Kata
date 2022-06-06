# String calculator code
import re

class NegativeNumberError(Exception):
    """Raised when negative number is found
    
    Attributes:
        numbers: list of negative numbers
    """
    def __init__(self, numbers, message = "Negatives not allowed - "):
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
            delimiter = ","     # Default delimiter is ','
            delimit = re.search("^//", number)      # Check if delimiter is changed
            ans = 0
            flag = 0
            negative = []
            numbers = []

            # If new delimiter is present
            if delimit:
                number_string = re.split("^//", number)
                delimiter = re.search("^.", number_string[1])[0]    # Get the new delimiter
                number = re.sub("^.\\n", "", number_string[1], 1)
            
            numbers = number.split(delimiter) 
            nums_len = len(numbers)

            if nums_len <= 1 and "\n" not in numbers[0]:
                return int(numbers[0])
            
            for nums in  numbers:
                if "\n" in nums:
                    s = nums.split("\n")
                    for num in s:
                        if int(num) < 0:
                            flag = 1
                            negative.append(str(num))
                            continue
                        ans += int(num)
                    continue
                if int(nums) < 0:
                    flag = 1
                    negative.append(str(nums))
                    continue
                ans += int(nums)
            if flag:
                x = ",".join(negative)
                raise NegativeNumberError(x)
            return ans
    except ValueError:
        return "Input is not correct"
    except TypeError:
        return "Input is not correct"
    except NegativeNumberError as ex:
        print(ex)
