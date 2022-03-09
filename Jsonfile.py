import json as j

data = [{"name":"Likitha","status":"student" },{"name":"Likitha","status":"student" }]

jsondata=j.dumps(data)

myjsonData= j.loads(jsondata)  #Parsing

print(myjsonData)

