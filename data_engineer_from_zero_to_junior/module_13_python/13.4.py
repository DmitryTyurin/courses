# Напишите программу, которая принимает строку и выводит количество символов в ней. Пробелы игнорируются.

print(f"Количество символов: {len(input().replace(' ', ''))}")


# Напишите программу, которая принимает строку и выводит её в верхнем и нижнем регистре.

s = input()

print(f"Верхний регистр: {s.upper()}\n"
      f"Нижний регистр: {s.lower()}")


# Напишите программу, которая считает количество вхождений заданного слова в строке.

input_string = input()
search_word = input()

count = input_string.count(search_word)

print(f"Количество вхождений слова '{search_word}': {count}")


# Напишите программу, которая принимает строку и заменяет все пробелы на символ подчеркивания.

print(f"Измененная строка: {input().replace(' ', '_')}")