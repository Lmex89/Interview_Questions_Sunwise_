""" Exercise #2
 Help Vasya to determine the minimal number of characters sufficient for storing any year number in the range from A to B.
 
 Constrains
 both directions the years are numbered starting from 1. It is known that (753BC) <= A <= B <= (2012AD).
  
 Test cases:
 753BC-747BC
 output : 2
 
 2000AD-2012AD
 output : 10;

 Proposed by Luis Mex 
 12/6/2020
 """


def intToRoman(num):
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
# Converting to roman
    thousands = m[num // 1000]
    hundereds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
    ans = thousands + hundereds + tens + ones
    return ans
# print(intToRoman(65))


def stringToNumInt(string_input):
    # inputs be like 1BC-1AD
    # this function takes a string like above and converte to, separete
    # integers range A-B years
    years_range = string_input.split('-')
    flag = True
    anyos_range = []
    num = 0
    for j in range(0, 2):
        s = ''
        i = 0
        while flag:
            temp = years_range[j][i]
            if len(s) > 4 or temp == 'A' or temp == 'B':
                flag = False
                if (temp == 'A'):
                    num = int(s) + 753
                elif (temp == 'B'):
                    num = abs(int(s) - 753 - 1)
                break
            s = s + temp
            i += 1
        flag = True
        anyos_range.append(num)

    return anyos_range


def find_min_len(string_range_input):
    # main function
    # this is called striToNumInt and returns decimal as pair
    anyos = stringToNumInt(string_range_input)
    # print(anyos)
    anyos_in_Roman = []
    len_char_in_Roman = []
    # here we found the max len of characters in range input
    for i in range(anyos[0], anyos[1]+1):
        anyos_in_Roman.append(intToRoman(i))
        len_char_in_Roman.append(len(anyos_in_Roman[-1]))
    # print(len_char_in_Roman)
    # print(anyos_in_Roman)
    return max(len_char_in_Roman)


string_input = "753BC-2012AD"
print(find_min_len(string_input))
