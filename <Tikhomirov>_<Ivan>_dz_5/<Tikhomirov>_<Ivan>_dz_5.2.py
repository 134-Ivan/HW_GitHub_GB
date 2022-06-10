# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

num_generator = (num for num in range(1, int(input()), 2))

print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))
print(next(num_generator))