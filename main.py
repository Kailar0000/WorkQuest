# Рекурсия, которая создаст все возможные варианты
def str_funcion_draw(str_funcion_array, index):
    str_funcion_temp_array = [] # Временный список для уравнений
    for str_ellement in str_funcion_array:
        for ellement in sim_array:
            str_temp = str_ellement
            str_temp = str_temp + ellement + str(num_array[index])
            str_funcion_temp_array.append(str_temp)

    index = index + 1
    if (index > 9): # Ограничение для рекурсии
        return str_funcion_temp_array
    else:
        return str_funcion_draw(str_funcion_temp_array, index)

# Функция, которая отсеет неправильные варианты.
def only_tru(str_funcion_array, num_tru):
    only_tru_array = []
    for ellement in str_funcion_array:
        sum = eval(ellement)
        if (sum == num_tru):
            str_temp = ellement + "= 200"
            only_tru_array.append(str_temp)
    return only_tru_array

num_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] # Задаем список чисел.
sim_array = ["-", "", "+"] # Список символов
num_tru = 200 # Перемена отвечающий чему должно равняется уравнение
index = 1
str_function_array = ["9"] # Список отвечающий за уравнения

str_function_array = str_funcion_draw(str_function_array, index) # Запуск рекурсии
str_function_array = only_tru(str_function_array, num_tru) # Запуск функции
print(str_function_array)