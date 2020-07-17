import time

start_time = time.time()

with open('names_1.txt', 'r') as f:
	names1 = f.read().split("\n")

with open('names_2.txt', 'r') as f:
	names2 = f.read().split("\n")

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name1 in names1:
	if name1 in names2:
		duplicates.append(name1)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# stretch list comprehension
# duplicates = [name for name in set(names1).intersection(names2)]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
