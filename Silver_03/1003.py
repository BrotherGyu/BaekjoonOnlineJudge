## 다이나믹 프로그래밍(DP)
### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='/'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys ## 포함시켜야함
### 여기서부터 작성 ###
T = int(sys.stdin.readline())
test_case = [int(sys.stdin.readline()) for _ in range(T)]
answer_list = [[1, 0], [0, 1]]
for index in range(2, max(test_case)+1):
    first_list = answer_list[index - 2]
    second_list = answer_list[index - 1]
    answer_list.append([first_list[0] + second_list[0], first_list[1] + second_list[1]])
for value in test_case:
    print(answer_list[value][0], answer_list[value][1])