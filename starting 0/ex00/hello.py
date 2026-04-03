ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list
ft_list[1] = 'World!'

#tuple
myCampusCountry = 'Morocco'

tmp_list = list(ft_tuple)
tmp_list[1] = myCampusCountry
ft_tuple = tuple(tmp_list)

# set
# '''first method'''
# ft_set.pop()
# ft_set.add('Benguerir')

# '''second method'''
# ft_set.remove('tutu!')
# ft_set.add('Benguerir')

'''third method (best practice)'''
lst = list(ft_set)
lst.remove('tutu!')
lst.append('Benguerir')
ft_set = set(lst)



# dict
ft_dict["Hello"] = '1337'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
