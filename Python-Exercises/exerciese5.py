str1 = "P@#yn26at^&i5ve"
chars_count = 0
digit_count = 0
symbol_count = 0

for char in str1:
    if char.isalpha():
        chars_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print(f'char count{chars_count}, digit count {digit_count}, symbol count {symbol_count}')

