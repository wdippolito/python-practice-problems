from collections import Counter
def check(s, t):
    source_Count = Counter(s)
    target_Count = Counter(t)
    count = 0
    while True:
        for k, v in source_Count.items():
            print(v - target_Count[k])   
            source_Count[k] -= target_Count[k]               
        count += 1
    print(count)

if __name__ =="__main__":
    s = "mononommon"
    t = "monmon"
    check(s,t)