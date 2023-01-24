from mock_data import catalog

def print_catalog_total():
    total = 0
    for prod in catalog:
        total = total + prod["price"]

    print(f"the total of the catalog is:{total} USD")






print_catalog_total()










def say_hello():
    print("Hello there!")

def print_the_sum(a,b):
    print(a + b)


def print_the_division(a,b):
    if b == 0:
        print("Error: division by zero is not allowed")
    else:
        print(a / b)


def print_the_cheaper(num1, num2):
    if num1 < num2:
        print(num1)

    else:
        print(num2)

def print_all_number():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    for n in nums:
        print(n)

def print_the_sum():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]

    total = 0 
    for n in nums:
        total += n

    print(total)


def print_the_sum_40():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    total = 0
    for n in nums:
        if n > 40:
            total = total + n

    print (total)


def print_count_lowers():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    count = 0
    for n in nums:
        if n <= 50:
            count = count + 1
    print(count)




# say_hello()
# print_the_sum(21, 21)
# print_the_division(10,4)
# print_the_division(300, 0)

# print_the_cheaper(34, 10)
# print_the_cheaper(3, 100)

#print_all_number()

#print_the_sum()

#print_the_sum_40()

#print_count_lowers()