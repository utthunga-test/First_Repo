class student:

    school = 'telusko'

    def _init_(self,m1,m2,m3):
        self.m1=10
        self.m2=20
        self.m3=30

    def avg(self):
        return (self.m1+self.m2+self.m3/3)

s1 = student()
s2 = student()

print(s1.avg())
        