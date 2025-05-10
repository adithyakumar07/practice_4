for i in range (7):
	for j in range (4):
		if i+j==3 or i-j==3:
			print("$",end=" ")
		else:
			print(" ",end=" ")
	print( )	