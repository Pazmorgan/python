#ex 1 (Todo sección de funciones)
def sum_odd_numbers(numbers):
    """Suma los numeros impares en una lista de numeros y devuelve el resultado."""
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))




#ex 2 ejem
def unique_list(numbers):
    """Devolver una lista de numeros únicos de dicha lista."""
    return list(set(numbers))

print(unique_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]))



#ex 3 D
def ordered_unique_list(numbers):
   unique_list = [1,2,3,4,5,6,7,8,9,10]
   for number in numbers:
       if number not in unique_list:
           unique_list.append(number)
   return unique_list
   
print(ordered_unique_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]))



#ex 4
def numeros_pares(numbers):
    """Devolver numeros pares de una lista"""
    evens= [2,4,6,8,10]
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

print(numeros_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))       
