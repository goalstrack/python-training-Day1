'''emp={'empno':101,
     'name':'ravi',
     'salary':9000,
     'name':'ved'}#new name will be considered by eliminating older one
print(emp)'''

emp={'empno':[101,102,103],
     'name':['ravi','anuj','raj'],
     'salary':[9000,12000,32000]
     }
print(emp.keys())
print(emp.values())

print(emp['name'])
#None since 
print(emp.get('grade'))

print(emp.get('grade','N/A'))

a={'grade':'a','leaves':40}

#after emp a will be appended
emp.update(a)
print(emp)

f=emp.copy()
print(f)