import json
x={"name":"don lee","age":"37","city":"japan","hobbies":"acting"}
y=json.dumps(x)
print(y)

import json
x={"name":"don lee","age":"37","city":"japan","hobbies":"acting"}
y=json.dumps(x, indent=4)
print(y)


import json
x={"name":"don lee","age":"37","city":"japan","hobbies":"acting"}
y=json.dumps(x, indent=4,separators=(".","="))
print(y)



import json
x={"name":"don lee","age":"37","city":"japan","hobbies":"acting"}
y=json.dumps(x, indent=4, sort_keys=True)
print(y)