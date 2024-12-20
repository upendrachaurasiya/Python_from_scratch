import json
d={"name":"ram",
"address":"USA",
"job":"software developer"}

to_json=json.dumps(d)
print(type(to_json))
print(to_json)

# Convert JSON to dictionary now  

frm_json=json.loads(to_json)
print(type(frm_json))
print(frm_json)