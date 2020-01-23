from collections import OrderedDict

od = OrderedDict()

od[1] = 1
od[2] = 2
od[3] = 3

for key,value in od.items():
    print(key,value)

od.pop(2)
for key,value in od.items():
    print(key,value)

od[2] = 22
for key,value in od.items():
    print(key,value)

od.move_to_end(3)
for key,value in od.items():
    print(key,value)