def lev_distance(i, j, s1, s2, matrix):
    if i == 0 and j == 0:
        return 0
    elif j == 0 and i > 0:
        return i
    elif i == 0 and j > 0:
        return j
    else:
        m = 0 if s1[i-1] == s2[j-1] else 1
        return min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+m)

 
def levenshtein_distance(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            matrix[i][j] = lev_distance(i, j, s1, s2, matrix)
    return matrix[n][m]


s1 = open('C:/Users/User/Desktop/plagiat/files/__init__.py', 'r').readline()
s2 = open('C:/Users/User/Desktop/plagiat/plagiat1/__main__.py', 'r').readline()

s1 = str(s1)
s2 = str(s2)

print(levenshtein_distance(s1, s2))