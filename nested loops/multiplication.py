#Create  a  python  program  to  print  the  multiplication  tables  of  different numbers
for i in range(1,11):
        print(f"Multiplication table for {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()