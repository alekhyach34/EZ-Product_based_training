my_map={}
#putting key value pair
my_map["key"]="This is a value"
my_map[0]="ZERO"
my_map[1.3]="ONE.THREE"
#putting and defaulting if a key does not exist
print(my_map)
try:
  print(my_map[10])
except:
  print("key does not exist")
del my_map[0]
print(my_map)
if "key" in my_map:
  print("key 0 is not present")
else:
  print("key  is not present")