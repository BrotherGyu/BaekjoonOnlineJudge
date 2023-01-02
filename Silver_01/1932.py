### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='\\'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys

triangle_size = int(sys.stdin.readline())
triangle_list = []
for _ in range(triangle_size):
    triangle_list.append(list(map(int,sys.stdin.readline().split())))

index = 0
for _ in range(triangle_size):
    triangle_size-=1
    for index in range(triangle_size):
        first_value = triangle_list[triangle_size-1][index] + triangle_list[triangle_size][index]
        second_value = triangle_list[triangle_size-1][index] + triangle_list[triangle_size][index+1]
        triangle_list[triangle_size-1][index]=max([first_value, second_value])
print(triangle_list[0][0])