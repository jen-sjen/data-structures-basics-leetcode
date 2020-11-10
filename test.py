def spiral(matrix):
    res = []
    x = m = len(matrix)
    y = n = len(matrix[0])
    t = 0
    while len(res) < x * y:
        i = t
        print("t:", t, "m:", m, "n:", n)
        for j in range(t, n):
            res.append(matrix[i][j])
        
        if len(res) == x * y:
            break
        j = n - 1
        for i in range(t+1, m):
            res.append(matrix[i][j])
        
        if len(res) == x * y:
            break
        i = m - 1
        for j in range(n - 2, t-1, -1):
            res.append(matrix[i][j])
        
        if len(res) == x * y:
            break
        j = t
        for i in range(m - 2, t, -1):
            res.append(matrix[i][j])
        
        t += 1
        m -= 1
        n -= 1
    return res

if __name__ == "__main__":
    print(spiral([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
]))