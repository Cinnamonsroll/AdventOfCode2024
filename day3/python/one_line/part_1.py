print(sum(int(x)*int(y) for x,y in __import__('re').findall(r"mul\((\d+),(\d+)\)", open("input.txt").read())))
