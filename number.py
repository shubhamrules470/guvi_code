if __name__=="__main__":
	try:
		n=int(input())
		if n==0:
			print("Zero")
		elif n>0:
			print("Positive")
		else:
			print("Negative")
	except:
		print("Invalid Input")