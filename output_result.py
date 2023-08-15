import json
from des import des,np
fp = open('source.json','r')
citys = json.load(fp)
for city in citys:
    years=city[0]
    payload=city[1]
    name=city[2]
    print(name)
    des(payload,np.arange(years[0],years[1]+1),3,name)
