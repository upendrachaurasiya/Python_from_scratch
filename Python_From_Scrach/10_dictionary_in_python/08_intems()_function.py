d={"course":"Python",
"fees":3000,
"duretion":"2 months"}

print(d.items())    #output(dict_items([('course', 'Python'), ('fees', 3000), ('duretion', '2 months')]))

i=d.items()

print(i)            #output(dict_items([('course', 'Python'), ('fees', 3000), ('duretion', '2 months')]))


for i,j in d.items():
    print(i,":",j) 