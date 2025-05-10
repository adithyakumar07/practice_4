for i in range (7):
	for j in range (4):
		if j==3 and i==3 or i-j==0 and j<3 or i+j==6 or j>3:
			print("$",end=" ")
		else:
			print(" ",end=" ")
	print( )	