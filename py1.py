x = range(10,210,10)
print(list(x))

my_range = range(1,21)
print([10 * x for x in my_range])

print(list(map(str, my_range)))

a = ["1", 1, "1", 2]
b = list(dict.fromkeys(a))
a = list(set(a))
print(b)
print(a)

myDict = {"a":1, "b":2, "c":3}
myDict2 = dict(a = 1, b = 2)
print(myDict2.get("b"))
print(myDict["b"])
print(myDict["a"] + myDict["b"])

d = {"a": 1, "b": 2}
d["c"] = 3
print(d.get("c"))

print(sum(d.values()))

d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)

from pprint import pprint
abc = {"a":list(range(1,11)), "b":list(range(11,21)), "c":list(range(21,31))}
pprint(abc)

pprint(abc["b"][2])