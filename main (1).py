from validate1 import *
class BankMagSystem:
  BankName='ICICI'
  IFSC_Code='ICICI0099'
  def __init__(self,AccNo,AccHolName,Age,Gender,DOB,Address,City,TypeofAcc,bal,PanNo,AdNo):
    self.AccNo=AccNo
    self.AccHolName=AccHolName
    self.Age=Age
    self.Gender=Gender
    self.DOB=DOB
    self.Address=Address
    self.City=City
    self.TypeofAcc=TypeofAcc
    self.bal=bal
    self.PanNo=PanNo
    self.AdNo=AdNo
  def display1(self):
    print(self.AccNo," ",self.BankName," ",self.IFSC_Code," ",self.AccHolName," ",self.Age," ",self.Gender," ",self.DOB," ",self.Address," ",self.City," ",self.TypeofAcc," ",self.bal," ",self.PanNo," ",self.AdNo)
Bankdis={}
while True:
  print("Greetings from ICICI bank")
  print("1 for insert bank details")
  print("2 for display details of account holders")
  print("3 for search details")
  print("4 for update details")
  print("5 for delete record")
  print("6 for deposit money")
  print("7 for withdraw money")
  print("8 for fund transfer")
  print("9 for balance enquiry")
  print("10 for name of the account holder with highest balance")
  print("11 for exit")
  choice=int(input("enter the choice"))
  if choice==1:
    while True:
      AccNo=input("enter account number")
      if val_AccountNumber(AccNo):
        break
      else:
        print("invalid!! please enter it again")
    while True:
        AccHolName=input("enter the name")
        if val_AccName(AccHolName):
            break
        else:
            print("invalid!! please enter it again")
    Age=input("enter the age")
    while True:
        Gender=input("enter the gender")
        if val_Gen(Gender):
            break
        else:
            print("invalid!! please enter it again")
    while True:
        DOB=input("enter the date")
        if val_Dob(DOB):
            break
        else:
            print("invalid!! please enter it again")
    Address=input("enter the address")
    while True:
        City=input("enter the city")
        if val_City(City):
            break
        else:
            print("invalid!! please enter it again")
    while True:
        TypeofAcc=input("enter account type")
        if val_AccType(TypeofAcc):
            break
        else:
            print("invalid!! please enter it again")
    bal=int(input("enter the initial deposit amount"))
    while True:
        PanNo=input("enter pan number")
        if val_PanNumber(PanNo):
            break
        else:
            print("invalid!! please enter it again")
    while True:
        AdNo=input("enter adhar number")
        if val_AdNumber(AdNo):
            break
        else:
            print("invalid!! please enter it again")
    obj=BankMagSystem(AccNo,AccHolName,Age,Gender,DOB,Address,City,TypeofAcc,bal,PanNo,AdNo)
    # Banklis.append(obj)
    if AccNo in Bankdis.keys():
        print("Account number is already present")
    else:
        Bankdis[AccNo]=obj
  elif choice==2:
    for i in Bankdis.values():
      i.display1()
  elif choice==3:
    print("enter A to search by AccNO")
    print("enter B to search by name")
    ch=input("enter choice")
    if ch=='A':
        a=input("enter ACCNO")
        for k,v in Bankdis.items():
            if k==a:
                v.display1()

    if ch=='B':
        n=input("enter name")
        for k,v in Bankdis.items():
            if v.AccHolName==v:
                v.display1()
  elif choice==4:
    AccNo=input("enter the account number you want to update")
    print("enter A to Update name")
    print("enter B to update address")
    print("enter C to update DOB")
    ch=input("enter choice")
    if ch=='A':
        for k,v in Bankdis.items():
            if k == AccNo:
                n=input("enter the name to update")
                v.AccHolName=n
                print("name updated")
            else:
                print("recheck account number")
    if ch=='B':
        for k,v in Bankdis.items():
            if k == AccNo:
                a=input("enter the address to update")
                v.address=a
                print("address updated")
            else:
                print("recheck account number")
    if ch=='C':
        for k,v in Bankdis.items():
            if k == AccNo:
                d=input("enter the DOB to update")
                v.DOB=d
                print("DOB updated")
            else:
                print("recheck account number")
  elif choice==5:
    AccNo=input("enter account number to be deleted")
    if AccNo in Bankdis.keys():
        del Bankdis[AccNo]
        print("account deleted")
    else:
        print("recheck account number")
  elif choice==6:
    AccNo=input("enter account number in which you want to deposit")
    for k,v in Bankdis.items():
            if k == AccNo:
                amt=int(input("enter the amount you want to deposit"))
                v.bal=v.bal+amt
            else:
                print("recheck account number")
  elif choice==7:
    AccNo=input("enter account number in which you want to withdraw amount")
    for k,v in Bankdis.items():
            if k == AccNo:
                amt=int(input("enter the amount you want to withdraw"))
                if amt<v.bal:
                    v.bal=v.bal-amt
                    print("Amount withdrawn Thank you for using ICICI")
                else:
                    print("Insufficient funds")
            else:
                print("recheck account number")
  elif choice==8:
    while True:
      AccNo1=input("enter account number from which you want to transfer funds")
      if AccNo1 not in Bankdis.keys():
        print("recheck account number")
      else:
        break
    while True:
      AccNo2=input("enter account number from which you want to transfer funds")
      if AccNo2 not in Bankdis.keys():
        print("recheck account number")
      else:
        break
    amt=int(input("enter the amount you want to transfer"))
    for k,v in Bankdis.items():
      if k==AccNo1:
        v.bal=v.bal-amt

    for k,v in Bankdis.items():
      if k==AccNo2:
        v.bal=v.bal+amt
        print("transfer successfull")
  elif choice==9:
    AccNo=input("enter account number")
    for k,v in Bankdis.items():
            if k == AccNo:
                print("balance = ",v.bal)
            else:
                print("recheck acoount number")
  elif choice==10:
    high_bal=0
    name=""
    for k,v in Bankdis.items():
      bal=v.bal
      if bal>high_bal:
        high_bal=bal
        name=v.AccHolName
    print(name)
  elif choice==11:
      break
  else:
    print("invalid choice")