### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='/'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
## 1번째 풀이
import sys
print(len(sys.stdin.readline().split()))
## 2번째 풀이
"""
print(len(input().split()))
"""