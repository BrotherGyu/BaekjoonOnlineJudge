## 다이나믹 프로그래밍(DP)
### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='/'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys ## 포함시켜야함
T = int(sys.stdin.readline())
test_case = []
max_k, max_n = 0, 0
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    max_k, max_n = max(max_k, k), max(max_n, n)
    test_case.append([k, n])
apartment_list = [[i for i in range(1,max_n+1)] for _ in range(max_k+1)]
for k_value in range(1, max_k + 1):
    for n_value in range(max_n):
        apartment_list[k_value][n_value] = sum(apartment_list[k_value - 1][:n_value + 1])
for index_list in test_case:
    print(apartment_list[index_list[0]][index_list[1] - 1])