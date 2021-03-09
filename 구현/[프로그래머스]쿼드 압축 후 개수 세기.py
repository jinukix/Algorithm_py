def solution(arr):
    
    global ans

    ans = [0, 0]

    def comp(y, x, l):
        init = arr[y][x]

        for i in range(y, y + l):
            for j in range(x, x + l):
                if arr[i][j] != init:
                    ll = l // 2

                    comp(y, x, ll) 
                    comp(y, x + ll, ll)
                    comp(y + ll, x, ll)
                    comp(y + ll, x + ll, ll)
                    return

        ans[init] += 1

    comp(0, 0, len(arr))
    return ans

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

print(solution(arr))