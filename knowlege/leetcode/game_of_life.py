def gameOflife(board):
	cp = board.copy()
	for i range(len(cp)):
		for j in range(len(cp[0])):
			ct = 0;
			if i>=1:
				ct += cp[i-1][j]
				if j>=1:
					ct += cp[i-1][j-1]
				if j<=len(cp[0])-2:
					ct += cp[i-1][j+1]
			if
