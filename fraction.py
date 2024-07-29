class F:
    def __init__(self,n,d=1):
  
        self.n=n
        self.d=d
        if(self.check()):
            exit()
        
    def check(self):
        if self.d == 0:
            print("Denominator Cannot be Zero")
            return None

    
    def __str__(self):
        if self.d == 0:
            return "Denominator cannot be Zero"
        return "{}/{}".format(self.n,self.d)

    def __add__(self,other):
        
        if self.d==0 or other.d==0:
            return None
        num= self.n*other.d+self.d*other.n
        den=self.d*other.d
        ret_num=num/den
        print("{}/{}".format(num,den))
        return ret_num
    
    def __sub__(self,other):
        if self.d ==0 or other.d == 0:
            return None
        num = self.n*other.d - self.d* other.n
        den = self.d*other.d 
        ret_num = num/den
        return ret_num
    def __mul__(self,other):
        if self.d == 0 or other.d==0:
            return None
        num = self.n*other.n
        den = self.d*other.d
        ret_num = num/den
        return ret_num 
    
fr = F(1,2)
f  = F(2)

# print(fr+f)
# print(fr-f)
# print(fr*f)