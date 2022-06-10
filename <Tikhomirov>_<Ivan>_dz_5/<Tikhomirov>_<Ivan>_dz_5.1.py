# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield:

def num_generator(n):
    for num in range(1, n, 2):
        yield num

# for num in num_generator(100):
#     print(num)

generated_number = num_generator(30)
print(next(generated_number))
print(next(generated_number))
print(next(generated_number))
print(next(generated_number))
print(next(generated_number))