temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

print("Wednesday:", temperatures[2])
print("Max Temperatures:", max(temperatures))
print("Min Temperatures:", min(temperatures))
print("Average Temperatures:", round(sum(temperatures)/len(temperatures), 1))

i = 0
for temp in temperatures:
    if temp > 17:
        i += 1
print("Temperatures above 17 degrees:", i)

print("Sorted from highest to lowest:", sorted(temperatures))

