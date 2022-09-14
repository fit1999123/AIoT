
class fruit:
    
    
    def __init__(self,stock,price,string):
        self.stocks = stock
        self.string = string
        self.prices = price    
    def accounts(self):
        if self.stocks>0:
            self.stocks-=1
        else:
            self.prices = 0
            
Banana = fruit(6,4,"Banana")
Apple = fruit(0,2,"Apple")
Durian= fruit(32,1.5,"Durian")
Pear = fruit(15,3,"Pear")

def Rechung(bills):
    
    cost = 0    
    
    for bill in bills:
        
        bill.accounts()
        
        cost += bill.prices
        
    return cost 

bills = [Banana,Durian,Apple] 



if __name__=="__main__":
    
    total_cost = Rechung(bills) 
    print("total costs =",total_cost)

    for i in [Banana,Apple,Durian,Pear]:
        
        print(i.string+"'s stocks =",i.stocks)