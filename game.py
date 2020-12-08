import numpy as np
from dllist import DoubleLinkedList

from ball import Ball
from field import Field
from pong import Pong
from snake import Snake

height = 10
width = 10
a = np.array([[i for i in range(height)] for j in range(width)])
for i in range(height):
    for j in range(width):
        if(j == 0):       
            a[i][j] = 0
        if(i == 0):
            a[i][j] = 3


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