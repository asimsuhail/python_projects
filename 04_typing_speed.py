import time
import re
sample_stirng = "Hi this is asim how are you i think you asldfjls lsjflks dlskjfd slkj slfdkj sa;lkf "
print(len(re.findall(r'\w+', sample_stirng)))
start_time = time.time()
new_str = input()
end_time = time.time()

total_time = end_time - start_time

print(total_time)