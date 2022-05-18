# -*- coding: utf-8 -*-
a = {'name':'pey', 'phone':'0109993323'}
print(a.keys()) # dict_keys(['name', 'phone'])
print(type(a.keys()))
print(list(a.keys()))
print(a.values())
print(a.keys())
print(a.items())
a.clear()
print(a)

a = {'name':'pey', 'phone':'0109993323'}
print(a.get('name')) # pey
print(a.get('hello')) # None
print('name' in a) # True
print('email' in a) # False