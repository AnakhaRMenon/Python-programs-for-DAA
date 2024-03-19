numOfVertices = 4

Infinity = 999


# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(numOfVertices):
        for i in range(numOfVertices):
            for j in range(numOfVertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        print("A",k+1,"=")
        print_solution(distance)
        print(" ")


# Printing the solution
def print_solution(distance):
    for i in range(numOfVertices):
        for j in range(numOfVertices):
            if(distance[i][j] == Infinity):
                print("Infinity", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [   [0, 3, Infinity, 7],
        [8, 0, 2, Infinity],
        [5, Infinity, 0, 1],
        [2, Infinity, Infinity, 0]]
floyd_warshall(G)

print("Anakha R Menon")
print("ROLL.NO-CH.EN.U4CSE20103\n")
