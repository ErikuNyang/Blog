import copy
# Python3 program to find the longest path in a matrix
# Returns length of the longest path beginning with mat[i][j].
# This function mainly uses lookup table dp[i][j] which contains the longest path value from the position i,j

# LongestPath search class, containing longest path and the paht's lengh, and matrix
class LongestPath:
    def __init__(self):
        self.longestPath                =   []          # Longest Path variable
        self.longestPathLength          =   None        # Longest Path Length variable
        self.mat                        =   None        # Matrix variable

# find the longest path from a cell
def findLongestFromACell(i, j, mat, dp):
    # append the sqaure to a temporary longest path list to track the path
    temp.append(mat.mat[i][j])

    # find length n,m (row and column) for i,j interation since it is not n x n matrix
    n = len(mat.mat)
    m = len(mat.mat[i])

    # Base case: return 0 to add to the x, y variables that counts path length from each cell
    if (i >= n or j >= m):
        return 0

    # current cell already has path value, so do not calculate the further length from this cell
    if (dp[i][j] != -1):
        return dp[i][j]

    # x stores the longest path legnth value received from cell on the right
    # y stores the longest path length value received from cell under the current cell
    # Initialize both variables with -1 when accessing the current cell for the first time..
    x, y = -1, -1

    # add + 1 to the path counter x if current cell is larger then the next cell's value(j+1) and evaluate the cell
    if (j < m-1 and ((mat.mat[i][j]) > mat.mat[i][j + 1])):
        x = 1 + findLongestFromACell(i, j + 1, mat, dp)

    # add + 1 to the path counter y if current cell is larger then the next cell's value(i+1) and evaluate the cell
    if (i < n-1 and (mat.mat[i][j] > mat.mat[i + 1][j])):
        y = 1 + findLongestFromACell(i + 1, j, mat, dp)

    # If none of the adjacent one (right or down) is smaller, we will take 1
    # otherwise we will pick maximum from all directions and assign the value to dp[i][j]
    dp[i][j] = max(x, max(y, 1))

    # at the end of the path, compare the length of current longest path with this temporary longest path
    # if temporary path is longer, then update the longest path
    if len(mat.longestPath) < len(temp):
        mat.longestPath = copy.deepcopy(temp)
    
    # clear the temporary longest path
    temp.clear()
    # return current longest path length
    return dp[i][j]


# Returns length of the longest path beginning with any cell
def findLongestOverAll(mat):
    mat.longestPathLength = 1 # Initialize result

    # Copy the matrix to a new matrix with the same size
    dp = copy.deepcopy(mat.mat)
    
    #initialize dp matrix to -1
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            dp[i][j] = -1

    # declare temporary longest path list
    global temp
    temp = []
    
    # Compute longest path beginning from all cells
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if (dp[i][j] == -1):
                findLongestFromACell(i, j, mat, dp)
            # Update the logest path length 
            mat.longestPathLength = max(mat.longestPathLength, dp[i][j])
    print(mat.longestPath)
    return mat.longestPathLength

# main function 
if __name__ == "__main__":
    # construct an instance of LogestPath class
    matPath = LongestPath()

    # read an input file and create a matrix out of it
    with open('input3.txt','r') as f:
        datalist = (map(lambda x: [ int(y) for y in x ] , [ i.rstrip().split() for i in f.readlines() ] ))
    
    # assign matrix to the instance's matrix variable mathPath.mat
    matPath.mat = (list(datalist))
    
    print("Length of the longest path is ", findLongestOverAll(matPath))