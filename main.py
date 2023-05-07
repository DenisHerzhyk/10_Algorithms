# 1).

def buble_sort(list):
    for item in range(len(list) - 1, 0, -1):
        for i in range(item):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


list = [1, 88, 5, 43, 75, 4, 7, 9, 5, 3, 22, 15, 35, 33]
print("Input here:", list)
print("Output here:", buble_sort(list))


# 2).

def linear_sort(list, find_elem):
    low = 0
    find_result = False
    while low < len(list) and not find_result:
        if list[low] == find_elem:
            find_result = True
        else:
            low += 1
    return find_result


list = [1, 88, 5, 43, 75, 4, 7, 9, 5, 3, 22, 15, 35, 33]
find_elem = 9

if linear_sort(list, find_elem):
    print("We found him:", list.index(find_elem))
else:
    print("We aint found him")


# 3).

def binarn_func(list, elem):
    low = 0
    high = len(list) - 1
    find_result = False

    while low < high and not find_result:
        middle = (high + low) // 2
        guess = list[middle]
        if guess == elem:
            find_result = True
            return find_result
        if guess > elem:
            high = middle - 1
        elif guess < elem:
            low = middle + 1
    return find_result


list = sorted([1, 88, 5, 43, 75, 4, 7, 9, 5, 3, 22, 15, 35, 33])
elem = 4
print("Input list", list)

print("Output result", binarn_func(list, elem), list.index(elem))


# 4).

def func(n):
    for i in range(1, n + 1):
        # Проверяем, является ли i простым числом
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        # Если i - простое число, выводим его на экран
        if is_prime:
            print(i)


func(10)


# 5).

def func(n):
    list = []
    for i in range(2, n):
        if i ** 3 < n:
            list.append(i ** 3)
    return list


print(func(1000))


# 6).

def func(number):
    result = False
    listi = list(str(number))
    if int(listi[len(str(number)) - 1]) in range(0, 9, 2):
        result = True
        print(result)
    else:
        print(result)


func(24945638940387 ** 3)
