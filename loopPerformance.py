import time

# Create a large list of integers
my_list = list(range(10000000))

# Example "for" loop
start_time = time.time()
for num in my_list:
    pass
end_time = time.time()
for_time = end_time - start_time
print(f": {for_time:.6f} seconds") # 0.628944 seconds

# Example "while" loop
start_time = time.time()
i = 0
while i < len(my_list):
    i += 1
end_time = time.time()
while_time = end_time - start_time
print(f"{while_time:.6f} seconds") # 0.769406 seconds
