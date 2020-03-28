from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return

    def comparator(a, b):
        if a.score == b.score:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            return 0  
        
        elif a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        return 0

data = [["amy",100],["david",100],["heraldo",50],["aakansha",75],["aleksa",150]]

tran = []

for [name,score] in data:
	tran.append(Player(name,score))

tran = sorted(tran, key=cmp_to_key(Player.comparator))
for i in tran:
    print(i.name, i.score)	
