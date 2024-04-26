# string = input().split()
# r, t = [], []
# v = int(input())
# for i in string:
#     if len(i) == v:
#         t.append(i)
#     else:
#         r.append(t)
#         t = [i]
#     value_0 = i
# r.append(t)
# print(r)

# l = list(map(str, input().split()))
# result, temp = [[]], []
# for i in range(len(l)):
#     for j in range(len(l)):
#         temp = l[j:i + j + 1]
#         if len(temp) == i + 1:
#             result.append(temp)
# print(result)
# n = 8
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i] = 1
#     matrix[i][n - i - 1] = 2
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()

# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
#
#
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
#
n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]

print(minimum , maximum)

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# sum1, sum2 = 0, 0
# for i in range(n):
#     sum1 += matrix[i][i]
#     sum2 += matrix[i][n - i - 1]
# print(sum1 , sum2)

# n, count = int(input()), 0
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         count = (1 for num in matrix[i][j] if num > matrix[i][j])
# print(count)
#
# n = int(input())
# matrix = [[int(_) for _ in input().split()] for i in range(n)]
# max_element = matrix[0][0]
# for i in range(n):
#     for j in range(n):
#         if i < j and i < n - 1 - j and matrix[i][j] > max_element:
#             max_element = matrix[i][j]
#         elif i > j and i > n - 1 - j and matrix[i][j] > max_element:
#             max_element = matrix[i][j]
# print(max_element)





