my_list = [["a",56],["b",23],["c",36]]

my_list.sort(key=lambda element: element[1],reverse=True)

print(my_list)