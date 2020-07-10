class Solution:
    def islandPerimeter(self, grid):

        # constants and variables for vertices
        VISITED = 1
        UNVISITED = 0
        LAND_VERTEX = 1
        OCEAN_VERTEX = 0
        NOTHING = -1
        vertice_of_width = len(grid[0]) + 1
        vertice_of_height = len(grid) + 1

        # the number of edges
        edges = 0

        # init the vertices
        vertices = [[(OCEAN_VERTEX, UNVISITED)] * vertice_of_width] * vertice_of_height
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:     # if the grid is a land, change the vertex to LAND_VERTEX
                    vertices[i][j] = tuple([LAND_VERTEX, UNVISITED])    # assign a new tuple
                    vertices[i][j+1] = tuple([LAND_VERTEX, UNVISITED])
                    vertices[i+1][j] = tuple([LAND_VERTEX, UNVISITED])
                    vertices[i+1][j+1] = tuple([LAND_VERTEX, UNVISITED])

        # init for DFS (finding the strting vertex)
        starting_vertex = (0, 0)
        for i in range(len(vertices)):
            found_starting_vertex = False
            for j in range(len(vertices[i])):
                if vertices[i][j] == (LAND_VERTEX, UNVISITED):
                    starting_vertex = (i, j)
                    found_starting_vertex = True        # break twice if the starting_vertex is found
                    break
            if found_starting_vertex: break
        print(vertices)

        # # DFS
        # running_i = starting_vertex[0]    # runner of height
        # running_j = starting_vertex[1]    # runner of width
        # finished_cycle = False
        #
        # while not finished_cycle:
        #     '''
        #         precedence for runner's next position
        #         1. left
        #         2. down
        #         3. right
        #         4. up
        #     '''
        #     # if runner can go left
        #     if running_j > 0 and vertices[running_i][running_j - 1] == (LAND_VERTEX, UNVISITED):
        #         running_j -= 1
        #         vertices[running_i][running_j - 1] = (1, VISITED)
        #         edges += 1
        #     # if runner can go down
        #     elif running_i < vertice_of_height - 1 and vertices[running_i + 1][running_j] == (LAND_VERTEX, UNVISITED):
        #         running_i += 1
        #         vertices[running_i + 1][running_j] = (1, VISITED)
        #         edges += 1
        #     # if runner can go right
        #     elif running_j < vertice_of_width - 1 and vertices[running_i][running_j + 1] == (LAND_VERTEX, UNVISITED):
        #         running_j += 1
        #         vertices[running_i][running_j + 1] = (1, VISITED)
        #         edges += 1
        #     # if runner can go up
        #     elif running_i > 0 and vertices[running_i - 1][running_j] == (LAND_VERTEX, UNVISITED):
        #         running_i -= 1
        #         vertices[running_i - 1][running_j] = (1, VISITED)
        #         edges += 1
        #
        #     # if runner reaches to the starting vertex again
        #     if running_i == starting_vertex[0] and running_j == starting_vertex[1]:
        #         finished_cycle = True
        #
        # return edges

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
