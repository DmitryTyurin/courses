#Напишите простой калькулятор, который будет принимать два числа на вход и выводить на экран сумму и разность чисел.
#Для получения чисел необходимо использовать конструкцию read

#!/bin/bash

read num1
read num2

echo $((num1 + num2))
echo $((num1 - num2))


#Напишите программу которая будет на основе введенного числа выводить одно из следующих сообщений:
#Число <> положительное
#Число <> отрицательное
#Число равно 0
#Вместо <> необходимо будет вставить введенное число

#!/bin/bash

read a
if [ $a -gt 0 ]; then
  echo "Число $a положительное"
elif [ $a -lt 0 ]; then
  echo "Число $a отрицательное"
else
  echo "Число равно 0"
fi