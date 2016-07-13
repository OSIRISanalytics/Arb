
def convLay(layodds, commision = 0):
	return(1+(1*(1-commision)/(layodds - 1)))

print convLay(2.5)

class H2H:
	
	def __init__(self,home,away,home_back,home_lay,away_back,away_lay):
		self.home = home
		self.away = away
		self.home_back = home_back
		self.home_lay = home_lay
		self.away_back = away_back
		self.away_lay = away_lay

	def isArb(self):
		bb = 1 / self.home_back + 1 / self.away_back
		ll = 1 / convLay(self.home_lay) + 1 / convLay(self.away_lay)
		bl = 1 / self.home_back + 1 / convLay(self.away_lay)
		lb = 1 / convLay(self.home_lay) + 1 / self.away_back

		if (min(bb,ll,bl,lb) < 1):
			print "You've done found an arb son"
		else:
			print "No arbs available"

	#def arbBets(self):

test = H2H("Tom","Hannah",2,2,2,2)

test.isArb()
