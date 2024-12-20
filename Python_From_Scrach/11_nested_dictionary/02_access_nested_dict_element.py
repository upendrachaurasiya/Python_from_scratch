stu_name={
    "ram":{"name":"ram","course":"python","fees":2000},
    "shyam":{"name":"shyam","course":"c++","fees":1000},
    "radha":{"name":"radha","course":"html","fees":1500}
}

print(stu_name)

print()

print(stu_name["ram"])     #output==    {'name': 'ram', 'course': 'python', 'fees': 2000}
print(stu_name["ram"]["fees"])      #output== 2000
print(stu_name["ram"]["name"])      #output=== 'ram'
print(stu_name["radha"]["course"])  #output=== html