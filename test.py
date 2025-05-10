for i in range (7):
	for j in range (4):
		if j-i==3 or j+i==3:
			print("$",end=" ")
		else:
			print(" ",end=" ")
	print( )	