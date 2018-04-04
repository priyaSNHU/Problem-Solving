changed = [False] * n    # Will be true if we change value at that position during for loop
for i in range(n/2):
    if arr[i]==arr[-(i+1)]: # Both are already equal
        continue
    if arr[i]>arr[-(i+1)]:
        arr[-(i+1)] = arr[i]
        changed[-(i+1)] = True
    else:
        arr[i] = arr[-(i+1)]
        changed[i] = True
    k -=  1
    if k<0:         # Means solution doesn't exist
        print -1
    pos = 0
while k>=0 and pos<n/2:
    if arr[pos] == 9:  # Nothing to do in this case
        pos += 1
        continue
    if k>=1 and (changed[pos] or changed[-(pos+1)]):
        arr[pos] = arr[-(pos+1)] = 9
        k-=1
    elif k>=2:
        arr[pos] = arr[-(pos+1)] = 9
        k-=2
    pos += 1
if n%2!=0 and k>0:  # If n is odd check if middle element can be made 9
    arr[n/2] = 9
print ''.join(map(str, arr))
