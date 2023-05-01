import time # import time module for time calculation
import re   # import re for regular expression
sample_stirng = "Hi this is asim how are you i think you asldfjls lsjflks dlskjfd slkj slfdkj sa;lkf "
print(len(re.findall(r'\w+', sample_stirng)))    # prints random string on output screen
start_time = time.time()
new_str = input()
end_time = time.time()

total_time = end_time - start_time      # calculates the total time the user took to type

print(total_time)
