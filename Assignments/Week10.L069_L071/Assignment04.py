# التكليف 04

#     قم بعمل Function تقوم بنفس آلية عمل ال all وقم بتسميتها my_all
#     قم بعمل Function تقوم بنفس آلية عمل ال any وقم بتسميتها my_any
#     قم بعمل Function تقوم بنفس آلية عمل ال min وقم بتسميتها my_min
#     قم بعمل Function تقوم بنفس آلية عمل ال max وقم بتسميتها my_max
#     تأكد ان my_min + my_max تقبل List أو Tuple

# # my_all
# print(my_all([1, 2, 3])) # True
# print(my_all([1, 2, 3, []])) # False

# # my_any
# print(my_any([0, 1, [], False])) # True
# print(my_any([(), 0, False])) # False

# # my_min
# print(my_min([10, 100, -20, -100, 50])) # -100
# print(my_min((10, 100, -20, -100, 50))) # -100

# # my_max
# print(my_max([10, 100, -20, -100, 50, 700])) # 700
# print(my_max((10, 100, -20, -100, 50, 700))) # 700


# =========================================================

def my_all(items):
    for item in items:
        if bool(item):
            print(item)
            continue
        else:
            return False

    return True


def my_any(items):

    for item in items:
        if bool(item):
            return True
    return False


def my_min(numbers):
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num

    return min_number


def my_max(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number


# my_all
print(my_all([1, 2, 3]))  # True
print(my_all([1, 2, 3, []]))  # False

# my_any
print(my_any([0, 1, [], False]))  # True
print(my_any([(), 0, False]))  # False

# my_min
print(my_min([10, 100, -20, -100, 50]))  # -100
print(my_min((10, 100, -20, -100, 50)))  # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 700)))  # 700
