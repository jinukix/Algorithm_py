

def quadtree(x, y, n):

    if n == 1:
        return str(image[x][y])

    result = []

    for i in range(x, x+n):
        for j in range(y, y+n):

            if(image[i][j] != image[x][y]):

                result.append("(")
                result.extend(quadtree(x, y, n//2))
                result.extend(quadtree(x, y+n//2, n//2))
                result.extend(quadtree(x+n//2, y, n//2))
                result.extend(quadtree(x+n//2, y+n//2, n//2))
                result.append(")")

                return result

    return str(image[x][y])


n = int(input())

image = [list(map(int, input()))for i in range(n)]
print("".join(quadtree(0, 0, n)))
