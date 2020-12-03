from Eig import eigenvals,eigenvects
from GaussJordan import gauss_jordan
from Multiply import multiply, scalar
from Det import det
from AddSub import add,sub
from Transpose import transpose
from Inverse import inverse
import ast
import os
from numpy import linalg

class GUI:

        def __init__(self):
            self.run()

        def banner(self):
            os.system("clear")
            self.b = '''
            ==================================================

               __   _
              / /  (_)__  ___ ___ _____
             / /__/ / _ \/ -_) _ `/ __/
            /____/_/_//_/\__/\_,_/_/
               ___   __         __
              / _ | / /__ ____ / /  _______ _
             / __ |/ / _ `/ -_) _ \/ __/ _ `/
            /_/ |_/_/\_, /\__/_.__/_/  \_,_/
                    /___/
              _____     __         __     __
             / ___/__ _/ /_____ __/ /__ _/ /____  ____
            / /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/
            \___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/


            ==================================================
            '''
            print(f'{self.b}')

        def selectors(self):
            self.o = '''
                [1]     -   Matrix Addition/Subtraction  -
                [2]     -      Matrix Multiplication     -
                [3]     -        Find Determinant        -
                [4]     -        Matrix Transpose        -
                [5]     -         Matrix Inverse         -
                [6]     -          Eigenvectors          -
                [7]     -          Rank/Nullity          -
                [8]     -           Row Reduce           -

                Select option:  '''
            s = int(input(self.o))

            self.choose(s)



        def choose(self,s):
            if s == 1:
                os.system("clear")
                print("Would you like to add or subtract?\n[1]: Add\n[2]:Subtract")
                option = input("Input: ")
                print("\n\t\t\t\tEnter two matrices\n\t\t\t\t==================")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                b = ast.literal_eval(input("\t\t\t\tB:  "))
                if(option==1):
                    c = add(a,b)
                else:
                    c = sub(a,b)
                if(c != 0):
                    for i in c:
                        print("\t\t\t\t   ",i)
                else:
                    print("Please enter matrices of matching sizes.")
                print()
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
                d = det(a)
                print("\t\t\t\tD: ",d,end='\n\n')
            elif s == 4:
                os.system("clear")
                print("\n\t\t\t\tEnter a matrix\n\t\t\t\t==============")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = transpose(a)
                for i in c:
                    print("\t\t\t\t   ",i)
                print()
            elif s == 5:
                os.system("clear")
                print("\n\t\t\t\tEnter a matrix\n\t\t\t\t==============")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = inverse(a)
                for i in c:
                    print("\t\t\t\t   ",i)
                print()
            elif s == 6:
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
            elif s == 7:
                pass
            elif s == 8:
                os.system("clear")
                print("\n\t\t\t\tEnter a matrix\n\t\t\t\t==============")
                a = ast.literal_eval(input("\t\t\t\tA:  "))
                c = gauss_jordan(a)
                print("\t\t\t\tC: ")
                for i in c:
                    print("\t\t\t\t   ",i)
                print()
            elif s == 9:
                pass
            else:
                print("\t\t\t\tEnter a valid number\n")

        def ask(self):
            a = int(input("\t\t\t\tRun again?\n\t\t\t\t[1]   -  Yes  -\n\t\t\t\t[2]   -  No   -\n\n\t\t\t\t"))
            if a == 1:
                return 1
            else:
                return 0

        def run(self):
            running = 1
            while(running):
                self.banner()
                self.selectors()
                running = self.ask()


if __name__ == "__main__":

    GUI()
