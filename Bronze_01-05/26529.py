## 다이나믹 프로그래밍(DP)
### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='/'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys ## 포함시켜야함
n = int(sys.stdin.readline())
fibo_list = [1,1]
for i in range(2,46):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
for _ in range(n):
    index = int(sys.stdin.readline())
    print(fibo_list[index])