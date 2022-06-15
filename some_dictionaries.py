stuff_dictionary = {}

stuff_dictionary['fruits'] = ['apple','cranberry', 'grapefruit', 'peaches']

stuff_dictionary['colours'] = ['red','blue', 'yellow']

stuff_dictionary['numbers'] = list(range(100))

#print(dir(stuff_dictionary))

for key, value in stuff_dictionary.items():
    print(key)
    print(value)



stuff_dictionary_2 = {'juices':['cranberry','apple','grape']}
print(stuff_dictionary_2)