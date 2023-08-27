arr= ["lightcar","liver","lightscar"]
lent=min(len(arr[0]),len(arr[1]),len(arr[2]))
for i in range(0,lent):
    if arr[0][i]!=arr[1][i] or arr[1][i]!=arr[2][i] or arr[0][i]!=arr[2][i]:
        print(arr[0][:i])
        break
