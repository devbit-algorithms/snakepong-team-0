import numpy as np
from dllist import DoubleLinkedList

height = 10
width = 10
a = np.array([[i for i in range(height)] for j in range(width)])

def clear_field(self):
    for i in range(height):
        for j in range(width):
            a[i][j] = 0
        # if(j == 0):       
        #     a[i][j] = 0
        # if(i == 0):
        #     a[i][j] = 3

def draw_symbols(self, x, y, symbol):
    a[x][y] = symbol



playingField = a

print(playingField)

# arr = [[0] * width for i in range(height)] # loop will run for the length of the outer list
# for i in range(height):
# # # loop will run for the length of the inner lists
# #     for j in range(width):
# #         if i < j:
# #             arr[i][j] = 8
# #         elif i > j:
# #             arr[i][j] = 4
# #         else:
# #             arr[i][j] = 7
#     for height in arr:
#         print( ' '.join([str(x) for x in height] ) )


pongbar = DoubleLinkedList()

# class Pong:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__x

# class Snake:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
    
#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__x

# class Ball:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__x

# class Field:
#     def __init__(self, width, height):
#         self.__x = width
#         self.__y = height
    
#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__x
