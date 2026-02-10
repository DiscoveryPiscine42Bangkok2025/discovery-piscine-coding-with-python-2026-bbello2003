#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for i in original_array:
    if i > 5:
        new_array.append(i + 2)
    
unique_values = set(new_array)

print(original_array)
print(unique_values)