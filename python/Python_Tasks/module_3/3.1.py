# Выведите True если если коллекция сохранила свой порядок, иначе False.

coins = list(map(int, input().split()))

if sorted(coins) == coins:
    print(True)
else:
    print(False)


# На вход программе подается строка с числами, в котором числа разделены символом пробела.
# Необходимо вычислить сумму всех чисел в этом тексте и вывести результат на следующей строке.

nums = list(map(int, input().split()))

print(sum(nums))


# Из списка чисел, представленного в виде строки, разделенной пробелами, определите и выведите третье по величине отсортированного по убыванию.

nums = list(map(int, input().split()))

nums.sort(reverse=True)

print(nums[2])
