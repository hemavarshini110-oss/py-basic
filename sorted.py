s1 = input()
s2 = input()

# space & capital ignore pannitom
s1 = s1.lower().replace(" ", "")
s2 = s2.lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("true")
else:
    print("false")
