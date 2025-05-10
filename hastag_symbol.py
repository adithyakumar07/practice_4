for i in range (6):
	for j in range (5):
		if i==1 or j==1 or j==3:
			print("$",end=" ")
		elif i==4:
			print("$",end=" ")
		else:
			print(" ",end=" ")
	print( )