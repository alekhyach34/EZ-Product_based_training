my_map={}
#putting a key value pair
my_map["key"]="This is a value"
my_map[0]="ZERO"
my_map[1,3]="ONE.THREE"

#Printing and defaulting if a key does not exist
print(my_map)
try:
    print(my_map[10])
except:
    print("Key does not exist")
#print(my_map[1,3])

del my_map[0]
print(my_map)

if "0" in my_map:
    print("Key 0 is present")
else:
    print("key 0 is not present")

if "key" in my_map:
    print("Key key is present")
else:
    print("key key is not present")
