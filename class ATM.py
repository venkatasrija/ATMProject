class ATM:
    def __init__(self,username):
        self.data={'Srija':['77a00',2500,2222],'Bindu':['33b55',3000,3333]}
        self.username=username
        self.c=2
        self.verify()
    def verify(self):
        if self.username not in self.data:
           return 'invalid username end'
        elif self.username in self.data:
            while(self.c>=0): 
                password=input("enter password:") 
                if password==self.data[self.username][0] :
                   self.options()  
                elif self.c>=0:
                    print("invalid password ",self.c," chances ")
                    self.c-=1
                '''elif self.c<=0:
                    print("your account blocked!!!")
                    self.c-=1'''
                #break
            #eghprint(self.c)
            return "your account blocked"
    def options(self):
        while(1):
            print("select any operation")
            print("1.deposit\n2.withdrawl\n3.check balance\n4.change password")
            c=int(input())
            if c>4:
                print("entered invalid option please select again...")
                self.options()
            elif c==1:
                credit=int(input("enter credit amount:"))
                pin=int(input("enter your pin:"))
                if pin==self.data[self.username][2]:
                    self.data[self.username][1]+=credit
                    print("amount credited sucessfully")
                else:
                    print("wrong pin")
                    self.options()
            elif c==2:
                debit=int(input("enter debit amount:"))
                pin=int(input("enter your pin:"))
                if pin==self.data[self.username][2]:
                    if debit<=self.data[self.username][1]:
                        self.data[self.username][1]-=debit
                        print("amount debited sucessfully")
                    else:
                        print("insuffcient balance!!")
                else:
                    print("wrong pin")
                    self.options()
            elif c==3:
                pin=int(input("enter your pin:"))
                if pin==self.data[self.username][2]:
                    print(self.data[self.username][1]," rupees is your current balance in your account")
                else:
                    print("wrong pin")
                    self.options()
            elif c==4:
                pin=int(input("enter your pin:"))
                if pin==self.data[self.username][2]:
                    newpassword=input("enter new password:")
                    confirmpassword=input("enter confirm password:")
                    if newpassword==confirmpassword:
                        self.data[self.username][0]=newpassword
                    else:
                        print("new password and confirm password not matching")
                else:
                    print("wrong pin")
                    self.options()
            elif c==5:
                exit() 
           
username=input("enter user name:") 
a=ATM(username)
print(a.verify())