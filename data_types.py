# primitive/standard datatype
integer_datatype = int(10)
string_datatype = str('abc')
complex_datatype = complex(1, 2)
float_datatype = float(1)

# sequence datatype
# List Datatype
list_datatype = [3,2,1]
print(list_datatype)
list_datatype.pop(2)
print(list_datatype)
list_datatype.sort()
print(list_datatype)
print(list_datatype.count(3))
list_datatype.insert(3,5)
print(list_datatype)
list_datatype.append(9)
print(list_datatype)
list_datatype.reverse()
print(list_datatype)


#String DataType
String_datatype = "helloPython"
print(String_datatype)
print(String_datatype[2:])
print(String_datatype[:4])
print(String_datatype*2)
print(String_datatype.split('P'))
print(len(String_datatype))

# Tuple
tuple_datatype = ('sun','mon','tue','wed','thu','fri','sat')
print((tuple_datatype))
print(len(tuple_datatype))
print(tuple_datatype[2])

# Dictionary Datatype
dict_datatype = {1:"apple",2:"orange",3:"carrot"}
print(dict_datatype)
print(dict_datatype[2])
print(dict_datatype.keys())
print(dict_datatype.values())
dict_datatype.pop(1)
print(dict_datatype)
dict_datatype[4] = 'beetroot'
print(dict_datatype)

#Set DataType
set_datatype = {1,2,'Nishad'}
set_datatype_2 = {2,'nishad','father'}
print(set_datatype)
set_datatype.add('home')
print(set_datatype)
set_datatype.pop()
print(set_datatype)
print(set_datatype.union(set_datatype_2))
print(set_datatype.intersection(set_datatype_2))
print(set_datatype.difference(set_datatype_2))
