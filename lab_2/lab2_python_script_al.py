#Question 1: multiply all list items together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = 1
##equal to 1 because you don't want to multiply by zero

for i in part1:
    result1 = result1 * i

print('The answer to Question 1 is:', result1)

#Question 2: Add all list items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0

for i in part2:
    result2 = result2 + i

print('The answer to Question 2 is:', result2)

#Question 3: add only even list items together
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0

for i in part3:
    if i % 2 == 0:
        result3 = result3 + i

print('The answer to Question 3 is:', result3)
