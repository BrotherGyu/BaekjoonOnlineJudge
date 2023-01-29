### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='\\'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys ## 포함시켜야함

for i in range(3):
    
    ### 여기서부터 작성 ###
    x, y = map(int, sys.stdin.readline().split())
    dp_li = [[0]*(y+1) for _ in range(x+1)]
    dp_li[1][1] = 1
    for x_val in range(x):
        for y_val in range(y):
            if x_val == 0 and y_val == 0:
                continue
            dp_li[x_val + 1][y_val + 1] = (dp_li[x_val][y_val] + dp_li[x_val + 1][y_val] + dp_li[x_val][y_val + 1])%(10**9+7)
    print(dp_li[x][y])


    