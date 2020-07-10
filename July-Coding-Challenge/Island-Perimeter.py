class Solution:
    def islandPerimeter(self, grid):
        # constants and variables for vertices (use NA constant to make more simple)
        VISITED = 1
        UNVISITED = 0
        NA = -1
        vertice_of_width = len(grid[0]) + 1
        vertice_of_height = len(grid) + 1

        # the number of edges
        edges = 0

        # init the vertices
        vertices = [[NA] * vertice_of_width for i in range(vertice_of_height)]  # solve the tuple address problem
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:     # if the grid is a land, change the vertex to LAND_VERTEX
                    vertices[i][j] = UNVISITED    # change NA to UNVISITED land vertex
                    vertices[i][j+1] = UNVISITED
                    vertices[i+1][j] = UNVISITED
                    vertices[i+1][j+1] = UNVISITED

        # init for DFS (finding the strting vertex)
        starting_vertex = None
        for i in range(len(vertices)):
            found_starting_vertex = False
            for j in range(len(vertices[i])):
                if vertices[i][j] == UNVISITED:
                    starting_vertex = (i, j)
                    found_starting_vertex = True        # break twice if the starting_vertex is found
                    break
            if found_starting_vertex: break

        # DFS
        running_i = starting_vertex[0]    # runner of height
        running_j = starting_vertex[1]    # runner of width
        finished_cycle = False

        while not finished_cycle:
            '''
                precedence for runner's next position
                1. left
                2. down
                3. right
                4. up
            '''
            # if runner can go left
            if running_j > 0 and vertices[running_i][running_j - 1] == UNVISITED:
                vertices[running_i][running_j - 1] = VISITED
                running_j -= 1
                edges += 1
            # if runner can go down
            elif running_i < vertice_of_height - 1 and vertices[running_i + 1][running_j] == UNVISITED:
                vertices[running_i + 1][running_j] = VISITED
                running_i += 1
                edges += 1
            # if runner can go right
            elif running_j < vertice_of_width - 1 and vertices[running_i][running_j + 1] == UNVISITED:
                vertices[running_i][running_j + 1] = VISITED
                running_j += 1
                edges += 1
            # if runner can go up
            elif running_i > 0 and vertices[running_i - 1][running_j] == UNVISITED:
                vertices[running_i - 1][running_j] = VISITED
                running_i -= 1
                edges += 1

            # if runner reaches to the starting vertex again
            if running_i == starting_vertex[0] and running_j == starting_vertex[1]:
                finished_cycle = True

        return edges

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
