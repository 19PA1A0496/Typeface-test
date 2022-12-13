import fileinput
def sg(t):
    t = t.upper()
    s = ""
    s += t[0]
    di = {"BFPV": "1", "CGJKQSXZ": "2",
                  "DT": "3",
                  "L": "4", "MN": "5", "R": "6",
                  "AEIOUHWY": "."}
    for ch in t[1:]:
        for k in di.keys():
            if ch in k:
                c = di[k]
                if c != '.':
                    if c != s[-1]:
                        s += c
    s = s[:7].ljust(7, "0")
    return s
 
s = input()
l = []
ans = []
for line in fileinput.input(files ='input.txt'):
    nl = list(line.split())
    for ele in nl:
        if sg(ele) == sg(s):
            ans.append(ele)
print(ans)