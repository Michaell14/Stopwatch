for t in range(int(input())):
    print("Case #" + str(t+1) + ":", end = " ")

    n = int(input())
    v = list(map(int, input().split()))
    largestSeen = -1
    ans = 0
    for i in range(n):
        works = v[i] > largestSeen
        if i != n-1:
            works = works and v[i] > v[i+1]
        ans += works
        largestSeen = max(largestSeen, v[i])
    print(ans)
