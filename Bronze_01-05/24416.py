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
def fibo(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append(answer[i-1] + answer[i-2])
    return answer[-1]
print(fibo(n),n-2)