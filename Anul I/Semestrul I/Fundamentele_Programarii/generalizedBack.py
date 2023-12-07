'''
@author: Dell
'''
class BackSolver:
    """
      Template for solving problems using backtracking
      Need to inherit from this class and 
      override _consistent, _solution and _solutionFound methods
    """
    def __init__(self,DIM):
        self._DIM = DIM        
        
    def solve(self):
        """
        run the backtracking engine
        use _consistent to check if a candidate solution is valid
        use _solution to check if a consistent candidate is a solution 
        invoke _solutionFound for every solution found
        """
        x=[-1]
        while len(x)>0:
            choosed = False
            while not choosed and x[-1]<self._DIM-1:
                x[-1] += 1
                choosed = self._consistent(x)
            if choosed:
                if self._solution(x):
                    self._solutionFound(x)
                else:
                    x.append(-1)
            else:
                x.pop()
            
    def _consistent(self,x):
        """
          Owerride to provide specific implementation
          x - list of numbers
          return True if x can be extended to maybe becom a solution
        """
        return True
    
    def _solution(self,x):
        """
          Owerride to provide specific implementation
          x - list of numbers
          return True if x is a solution
        """
        return len(x)==self._DIM
    
    def _solutionFound(self,x):
        """
          Owerride to provide specific implementation
          x - list of numbers, represent a solution          
        """
        print(x)
    
# s = BackSolver(4)
# s.solve()
    
class PermutationBack(BackSolver):
    """
    Generate permutations using backtracking
    """
    def _consistent(self,x):
        return not x[-1] in x[:-1]
    
# s = PermutationBack(3)
# s.solve()

class QuenBack(BackSolver):
    
    def __init__(self,DIM):
        BackSolver.__init__(DIM)
        self._nrSol = 0
    
    def _consistent(self,x):
        # no queen on the same column        
        for i in range(len(x) - 1):
            if x[i] == x[-1]:
                return False
        # no queen on the same diagonal
        lastX = len(x)-1
        lastY = x[-1]
        for i in range(len(x)-1):
            if abs(i - lastX) == abs(x[i] - lastY):
                return False
        return True
    
    def _solutionFound(self,x):    
        self._nrSol+=1
        print ("__"*self._DIM,self._nrSol)
        # prepare an empty line on the board
        # print a chess board
        for column in range(self._DIM):
            # prepare a line
            cLine = ["0"] * self._DIM
            cLine[x[column]] = "X"
            print (" ".join(cLine))
        print ("__"*self._DIM)
        
    
        
s = QuenBack(8)
s.solve()
