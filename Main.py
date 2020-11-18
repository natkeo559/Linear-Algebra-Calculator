from Eig import eigenvals,eigenvects
from GaussJordan import gauss_jordan
from Multiply import multiply, scalar
from Det import det
import ast
import os

class GUI:

        def __init__(self):
            self.banner()
            self.selectors()

        def banner(self):
            os.system("clear")
            b = '''
            ==================================================

               __   _                     
              / /  (_)__  ___ ___ _____  
             / /__/ / _ \/ -_) _ `/ __/ 
            /____/_/_//_/\__/\_,_/_/   
               ___   __         __             
              / _ | / /__ ____ / /  _______ _
             / __ |/ / _ `/ -_) _ \/ __/ _ `/
            /_/ |_/_/\_, /\__/_.__/_/  \_,_/  
              _____     __         __     __          
             / ___/__ _/ /_____ __/ /__ _/ /____  ____
            / /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/
            \___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/   
                                                                                                                         
                                                                                                    
            ==================================================
            '''
            print(f'{b}')

        def selectors(self):
            self.o = '''
                [1]     -   Matrix Addition/Subtraction  -
                [2]     -      Matrix Multiplication     -
                [3]     -        Find Determinant        -
                [4]     -          Eigenvectors          -
                [5]     -           Row Reduce           -

                Select option:  '''
            s = int(input(self.o))

            if s == 1:
                pass
            elif s == 2:
                os.system("clear")
                print("\n\t\t\t\tEnter two matrices\n\t\t\t\t==================")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                b = ast.literal_eval(input("\t\t\t\tB:  "))
                c = multiply(a,b)
                print("\t\t\t\tC: ")
                for i in c:
                    print("\t\t\t\t   ",i)
                print()
            elif s == 3:
                os.system("clear")
                print("\n\t\t\t\tEnter a square matrix\n\t\t\t\t=====================")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = det(a)
                print("\t\t\t\tC: ",c,end='\n\n')
            elif s == 4:
                os.system("clear")
                print("\n\t\t\t\tEnter a matrix\n\t\t\t\t==============")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = eigenvals(a)
                d = eigenvects(a)
                print("\t\t\t\tEigenvalues:")
                for i in c:
                    print("\t\t\t\t   ",i)
                print("\n\t\t\t\tEigenvectors:")
                for i in range(len(d)):
                    print("\t\t\t\t   ",c[i],"=",d[i])
                print()
            elif s == 5:
                os.system("clear")
                print("\n\t\t\t\tEnter a matrix\n\t\t\t\t==============")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = gauss_jordan(a)
                print("\t\t\t\tC: ")
                for i in c:
                    print("\t\t\t\t   ",i)
                print()


if __name__ == "__main__":
    
    GUI()