#Answer 5
quant=int(input("Enter quantity of item purchased:"))
cost=100*quant
if cost>1000:
	cost=cost-(.1*cost)
	print("Total Cost:%d"%cost)
else:
	print("Total Cost:%d"%cost)
	
