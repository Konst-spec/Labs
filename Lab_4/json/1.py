import json
with open('B:\Lab_1\Lab_4\json\sample-data.json', "r") as file:
    a = file.read()  
    b = json.loads(a)  

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in b["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"], "                            ", i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])