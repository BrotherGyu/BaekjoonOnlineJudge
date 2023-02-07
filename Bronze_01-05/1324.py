## 다이나믹 프로그래밍(DP)
### Load_Test_Case ###
import os
import sys
file_dir_path=os.path.dirname(os.path.realpath(__file__))
test_file_name='\\'+os.path.basename(__file__).replace('.py','.txt')
sys.stdin = open(file_dir_path + test_file_name, "r")
######################
import sys ## 포함시켜야함
from collections import deque
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split(' ')))
y = list(map(int, sys.stdin.readline().split(' ')))

x_que, y_que = deque(), deque()
trash_count = 0
for x_val, y_val in zip(x, y):
    if not (len(x_que) and len(y_que)):
        x_que.append(x_val)
        y_que.append(y_val)
        continue
    if x_que[-1] <= x_val:
        x_que.append(x_val)
    if y_que[-1] <= y_val:
        y_que.append(y_val)
while True:
    try:
        if x_que[0] == y_que[0]:
            x_que.popleft()
            y_que.popleft()
            trash_count += 1
            continue
        if x_que[0] < y_que[0]:
            x_que.popleft()
        else:
            y_que.popleft()
    except IndexError:
        break
print(trash_count)