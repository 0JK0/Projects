#card_number = 49927398716

card_number = input("--> Enter an 11 digits number: ")

# Put the string of numbers into a list
number_list = [int(number) for number in str(card_number)]

# Invert the numbers
number_list.reverse()

# Multiply every second number
two_digits = []
for i in range(0, len(number_list), 2): #range(start, stop, step)
    number_list[i] *= 2
    # If a number has more than 2 digits sum the digits.
    if number_list[i] >= 10:
        two_digits.append(number_list[i])
        sum_digits = sum(int(digit) for digit in str(number_list[i]))
        number_list[i] = sum_digits

#Sum all the numbers and if the resulting number is round the card is correct
final_number = sum(number_list)
print(final_number)

if final_number % 10 == 0:
    print("THIS NUMBER IS VALID!!")
else:
   print("THIS NUMBER IS NOT VALID!!")