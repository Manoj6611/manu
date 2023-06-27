tuple=[{4,5},{2,3},{6,7},{2,8}]
print("the list of original tuples")
print(tuple)
tuple.sort(key=lambda x:x[0]+x[1])
print("\n sorted list of tuples\n",tuples)