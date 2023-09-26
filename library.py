from pickle import load, dump
import os
import datetime

class bookclass:
      def __init__(self):
            self.bookno=0
            self.title=""
            self.author=""
            self.publication=""
            self.subject=""
            self.cost=0.0
            self.status="available"
      def getb(self):
            self.bookno=int(input("Enter book no:"))
            self.title=input("Enter book Title:")
            self.author=input("Enter author name:")
            self.publication=input("Enter publication:")
            self.subject=input("Enter subject:")
            self.cost=float(input("Enter cost of the book:"))
      def dispb(self): 
            print('   ',self.bookno,end='    ')
            print('  ',self.title,end='    ')
            print('    ',self.author,end='    ')
            print('   ',self.publication,end='    ')
            print('   ',self.subject,end='    ')
            print('  ',self.cost,end='  ')
            print('  ',self.status)
      def modb(self):
            print ("Old Name was:",self.title)
            self.title=input("Enter book Title:")
            print("Old Author name was:",self.author)
            self.author=input("Enter author name:")
            print("Old Publication was:",self.publication)
            self.publication=input("Enter publication:")
            print("Old Subject was:",self.subject)
            self.subject=input("Enter subject:")
            print("Old Cost was:",self.cost)
            self.cost=float(input("Enter cost of the book:"))
      def dispb1(self):
      
            print("|    ",self.bookno,"    |    ",self.title,"  |   ",self.author,"  |     ", self.publication,"       |   ",self.subject,"   |",self.status,"|")    



def addbookdetails():         #add book details
      b1=bookclass()
      print("   E N T E R    B O O K   D E T A I L S ")
      b1.getb()
      fp=open("book.dat","ab")
      dump(b1,fp)
      fp.close()
      print()
      print("R E C O R D   A D D E D   S U C C E S S F U L L Y.........")
      

def modbookdetails():
      fp1=open("book.dat","rb")
      fp2=open("temp.dat","wb")
      print(" - E N T E R   N E W   B O O K   D E T A I L S -  ")
      no=int(input("Enter Book no. to modify:"))
      c=0
      try:
            while True:
                  b1=load(fp1)
                  if b1.bookno==no:
                        c=1
                        b1.modb()
                        dump(b1,fp2)
                        fp2.flush()
                  else:
                        dump(b1,fp2)
                        fp2.flush()
      except EOFError:
            pass
      fp1.close()
      fp2.close()
      os.remove("book.dat")
      os.rename("temp.dat","book.dat")


def searchbookdetails(x):
      b1=bookclass()
      fp=open("book.dat","rb")
      print("__"*50)
      try:
            while True:
                  b1=load(fp)
                  if b1.bookno==x:
                        b1.dispb()
      except EOFError:
            print("__"*50)
            pass
      fp.close()

def deletebookdetails(y):
      b1=bookclass()
      fp1=open("book.dat","rb")
      fp2=open("temp.dat","wb")
      print("__"*50)
      c=0
      try:
            while True:
                  b1=load(fp1)
                  if b1.bookno==y:
                        c=1
                        pass
                  else:
                        dump(b1,fp2)
                        fp2.flush()
      except EOFError:
            pass
      fp1.close()
      fp2.close()
      os.remove("book.dat")
      os.rename("temp.dat","book.dat")
                             
                  
def displaybookdetails():
      fp=open("book.dat","rb")
      print ("_"*107)
      print("|  BOOK NO.  |   BOOK TITLE   |        AUTHOR NAME       |     PUBLICATION    |    SUBJECT    |   STATUS  |")
      print ("_"*107)


      try:
            while True:
                  b1=load(fp)
                  b1.dispb1()
      except EOFError:
            print ("_"*107)
      fp.close()
      

'''Def for function Books '''
 
def books():
      chb=0
                
      while chb<6:
            print("     B  O  O  K  S:")
            print()
            print("1.A D D")
            print()
            print("2.M O D I F Y")
            print()
            print("3.S E A R C H")
            print()
            print("4.D E L E T E")
            print()
            print("5.D I S P L A Y   A L L")
            print()
            print("6.- E X I T - ")
            print()
            chb=int(input("E N T E R   Y O U R   C H O I C E :"))
            if chb==1:
                  addbookdetails()
                  print()
            elif chb==2:
                  modbookdetails()
                  print()
            elif chb==3:
                  x=int(input("Enter Book no. to search for:"))
                  print("|  BOOK NO.  |  BOOK TITLE |    AUTHOR NAME   |   PUBLICATION   |  SUBJECT  |   COST  |  STATUS |")
                  searchbookdetails(x)
                  print()
            elif chb==4:
                  y=int(input("Enter no. to delete:"))
                  deletebookdetails(y)
                  print()
            elif chb==5:
                  displaybookdetails()
                  print()
            

                  
"""Section for Member"""

class memberclass:
      def __init__(self):
            self.memcode=0
            self.memname=""
            self.memaddress=""
            self.memphno=0
            self.memjoiningdt=datetime.date.today()
            self.memvalidity=datetime.date.today() + datetime.timedelta(days=365)
            self.memaccount=0.0
            self.memstatus=""
      def getm(self):
            self.memcode=int(input("Enter member no:"))
            print()
            self.memname=input("Enter member name:")
            print()
            self.memaddress=input("Enter member address:")
            print()
            self.memphno=int(input("Enter phone number:"))
            print()
            self.memaccount=float(input("Enter member account:"))
            print()
            self.memstatus="no book issued"
            print()
      def dispm(self):
            print('  ',self.memcode,end="   ")
            print('  ',self.memname,end="   ")
            print('  ',self.memaddress,end="   ")
            print('  ',self.memphno,end="   ")
            print('  ',self.memjoiningdt,end="   ")
            print('  ',self.memvalidity,end="   ")
            print('  ',self.memstatus)
      def modm(self):
            print()
            print("Old Member Name was: ",self.memname)
            print()
            self.memname=input("Enter New name:")
            print()
            print("Old member address was:",self.memaddress)
            print()
            self.memaddress=input("Enter new address:")
            print()
            print("Old member phone number was:",self.memphno)
            print()
            self.memphno=int(input("Enter new phone number:"))
            print()
            print("Old Member date of joining was:",self.memjoiningdt)
            print()
            self.memjoiningdt=input("Enter new date of joining :")
            print()
            print("Old Date of Validity was:",self.memvalidity)
            print()
            self.memvalidity=input("Enter new date till valid:")
            print()
            print("Old Member account was:",self.memaccount)
            print()
            self.memaccount=float(input("Enter new account:"))
            print()
            print("Old member status was:",self.memstatus)
            print()
            self.memstatus=input("Enter new status:")
            print()
      def dispm1(self):
            
            print( "|   ",self.memcode,"  |    ",self.memname,'   |  ',self.memstatus,'  |   ', self.memphno,'   |  ',self.memjoiningdt,'   |  ',self.memvalidity,"  |")
            


def addmemberdetails():         #add member details
      m1=memberclass()
      print("   E N T E R    M E M B E R   D E T A I L S ")
      m1.getm()
      fp=open("member.dat","wb")
      dump(m1,fp)
      fp.close()
      print()
      print("M E M B E R    D E T A I L S   A D D E D   S U C C E S S F U L L Y.........")
      

def modmemberdetails():
      m1=memberclass()
      fp1=open("member.dat","rb")
      fp2=open("temp.dat","wb")
      print("  E N T E R   N E W   M E M B E R   D E T A I L S  ")
      no=int(input("Enter Member no. to modify:"))
      c=0
      try:
            while True:
                  m1=load(fp1)
                  if m1.memcode==no:
                        c=1
                        m1.modm()
                        dump(m1,fp2)
                        fp2.flush()
                  else:
                        dump(m1,fp2)
                        fp2.flush()
      except EOFError:
            pass
      fp1.close()
      fp2.close()
      os.remove("member.dat")
      os.rename("temp.dat","member.dat")


def searchmemberdetails(x):
      m1=memberclass()
      fp=open("member.dat","rb")
      print("__"*50)
      try:
            while True:
                  m1=load(fp)
                  if m1.memcode==x:
                        m1.dispm()
      except EOFError:
            print("__"*50)
            pass
      fp.close()

def deletememberdetails(y):
      m1=memberclass()
      fp1=open("member.dat","rb")
      fp2=open("temp.dat","wb")
      print("__"*50)
      c=0
      try:
            while True:
                  m1=load(fp1)
                  if m1.book==y:
                        c=1
                        pass
                  else:
                        dump(m1,fp2)
                        fp2.flush()
      except EOFError:
            pass
      fp1.close()
      fp2.close()
      os.remove("member.dat")
      os.rename("temp.dat","member.dat")  
                             
                  
def displaymemberdetails():
      m1=memberclass()
      fp=open("member.dat","rb")
      print("__"*50)
      print("|MEMBER CODE","|  MEMBER NAME  ","|    STATUS  ","|  PHONE NUMBER","  | JOINING DATE   ","|    VALIDITY  |")
      print("__"*50)
      try:
            while True:
                  m1=load(fp)
                  m1.dispm1()
      except EOFError:
            print("__"*50)
            fp.close()
      


def members():
      chm=0
                  
      while chm<6:
            print("     M E M B E R S :")
            print()
            print("1.A D D")
            print()
            print("2.M O D I F Y")
            print()
            print("3.S E A R C H")
            print()
            print("4.D E L E T E")
            print()
            print("5.D I S P L A Y  A L L ")
            print()
            print("6.-E X I T-")
            print()
            chm=int(input("E N T E R   Y O U R   C H O I C E:"))
            print()
            if chm==1:
                  addmemberdetails()
                  print()
            elif chm==2:
                  modmemberdetails()
                  print()
            elif chm==3:
                  x=int(input("Enter Member number to search:"))
                  searchmemberdetails(x)
                  print()
            elif chm==4:
                  y=int(input("Enter Member number to delete:"))
                  deletememberdetails(y)
                  print()
            elif chm==5:
                  displaymemberdetails()
                  print()


                  
"""Def for issues function"""
class issue:
      def __init__(self):
            self.mcode=0
            self.mname=""
            self.bname=""
            self.bcode=0
            self.issuedate=""
            self.returndate=""
      def geti(self):
            print(self.mcode,end=" ")
            print(self.mname,end=" ")
            print(self.bname,end=" ")
            print(self.bcode,end=" ")
            print(self.issuedate,end=" ")
            print(self.returndate,end=" ")
      def dispi(self):
            print("member code is:",self.mcode)
            print("member name is:",self.mname)
            print("book name is:",self.bname)
            print("book code is:",self.bcode)
            print("Issue date is:",self.issuedate)
            print("return date is:",self.returndate)
      
           


def issuebook():
      i1=issue()
      b1=bookclass()
      m1=memberclass()
      mn=int(input("Enter Member code:"))
      fp=open("member.dat","rb")
      c1=0
      try:
            while True:
                  m1=load(fp)
                  if m1.memcode==mn:
                        c1=1
                        break
      except EOFError:
            pass
      fp.close()
      
      if (c1==1) and m1.memstatus=="no book issued":
            i1.mcode=m1.memcode
            i1.mname=m1.memname

            bkc=int(input("Enter Book  code to be issued .."))
            fp1=open("book.dat","rb")
            c2=0   
            try:
                  while True:
                        b1=load(fp1)
                        if b1.bookno==bkc:
                              c2=1
                              break
            except EOFError:
                  pass
            fp1.close()
            if c2==1 and b1.status=="available":
                  i1.bcode=b1.bookno
                  i1.bname=b1.title
                  i1.issuedate=datetime.date.today() + datetime.timedelta(days=0)
                  i1.returndate=datetime.date.today() + datetime.timedelta(days=15)
                  i1.geti()
                  fp=open("Transaction.dat","wb")
                  dump(i1,fp)
                  fp.close()

                  # modifying member status
                  
                  fp1=open("member.dat","rb")
                  fp2=open("temp.dat","wb")
                  try:
                        while True:
                              m1=load(fp1)
                              if m1.memcode==i1.mcode:
                                    m1.memstatus="book issued"
                                    dump(m1,fp2)
                              else:
                                    dump(m1,fp2)
                  except EOFError:
                        pass
                  fp1.close()
                  fp2.close()

                  os.remove("member.dat")
                  os.rename("temp.dat","member.dat")
                  
                  # modifying book status

                  fp1=open("book.dat","rb")
                  fp2=open("temp.dat","wb")
                  try:
                        while True:
                              b1=load(fp1)
                              if b1.bookno==i1.bcode:
                                    b1.status="issued"
                                    dump(b1,fp2)
                              else:
                                    dump(b1,fp2)
                  except EOFError:
                        pass
                  fp1.close()
                  fp2.close()

                  os.remove("book.dat")
                  os.rename("temp.dat","book.dat")

            else:
                  print(" Book code does not exist or book is already issued")
            
            
      else:
            print("Member does not exist")



def returnbook():
      i1=issue()
      b1=bookclass()
      m1=memberclass()
      mn=int(input("Enter Member code:"))
      fp=open("member.dat","rb")
      c1=0
      try:
            while True:
                  m1=load(fp)
                  if m1.memcode==mn:
                        c1=1
                        break
      except EOFError:
            pass
      fp.close()
      
      if (c1==1) and m1.memstatus=="book issued":
            i1.mcode=m1.memcode
            i1.mname=m1.memname

            bkc=int(input("Enter Book code to return.."))
            fp1=open("book.dat","rb")
            c2=0   
            try:
                  while True:
                        b1=load(fp1)
                        if b1.bookno==bkc:
                              c2=1
                              break
            except EOFError:
                  pass
            fp1.close()
            if c2==1 and b1.status=="issued":
                  i1.bcode=b1.bookno
                  i1.bname=b1.title
                  i1.geti()
                  fp=open("Transaction.dat","ab")
                  dump(i1,fp)
                  fp.close()

                  # modifying member status
                  
                  fp1=open("member.dat","rb")
                  fp2=open("temp.dat","wb")
                  try:
                        while True:
                              m1=load(fp1)
                              if m1.memcode==i1.mcode:
                                    m1.memstatus="no book issued"
                                    dump(m1,fp2)
                              else:
                                    dump(m1,fp2)
                  except EOFError:
                        pass
                  fp1.close()
                  fp2.close()

                  os.remove("member.dat")
                  os.rename("temp.dat","member.dat")
                  
                  # modifying book status

                  fp1=open("book.dat","rb")
                  fp2=open("temp.dat","wb")
                  try:
                        while True:
                              b1=load(fp1)
                              if b1.bookno==i1.bcode:
                                    b1.status="available"
                                    dump(b1,fp2)
                              else:
                                    dump(b1,fp2)
                  except EOFError:
                        pass
                  fp1.close()
                  fp2.close()

                  os.remove("book.dat")
                  os.rename("temp.dat","book.dat")

            else:
                  print(" Book code does not exist or book was not issued")
            
            
      else:
            print("Member does not exist")









def issues():
      chi=0
      
            
      while chi<3:
            print("     I S S U E S:")
            print()
            print("1.I S S U E   A   B O O K")
            print()
            print("2.R E T U R N   A   B O O K")
            print()
            print("3.-E X I T- ")
            chi=int(input("E N T E R   Y O U R   C H O I C E :"))
            if chi==1:
                  issuebook()
            elif chi==2:
                  returnbook()



"""Def for Info reports function"""
def memwithbook():
      m1=memberclass()
      fp=open("member.dat","rb")
      print("__"*50)
      print("MEMBER CODE\t","MEMBER NAME")
      print("__"*50)
      try:
            while True:
                  m1=load(fp)
                  if m1.memstatus=="book issued":
                        print(m1.memcode,"\t",m1.memname)
      except EOFError:
            print("__"*50)
            fp.close()
      



def memwithoutbook():
      m1=memberclass()
      fp=open("member.dat","rb")
      print("__"*50)
      print(" |  MEMBER CODE     |"," MEMBER NAME  |")
      print("__"*50)
      try:
            while True:
                  m1=load(fp)
                  if m1.memstatus=="no book issued":
                        print('    ',m1.memcode,"    ",m1.memname)
      except EOFError:
            print("__"*50)
            fp.close()


def bookissued():
      b1=bookclass()
      fp=open("book.dat","rb")
      print("__"*50)
      print("Book Code","\t","Name of Book")
      print("__"*50)
      try:
      
            while True:
                  b1=load(fp)
                  if b1.status=="issued":
                        print(b1.bookno,"\t",b1.title)
      except EOFError:
            print("__"*50)
            fp.close()


def bookavailable():
      b1=bookclass()
      fp=open("book.dat","rb")
      print("__"*50)
      print("Book Code","\t","Name of Book")
      print("__"*50)
      try:
            while True:
                  b1=load(fp)
                  if b1.status=="available":
                        print(b1.bookno,"\t",b1.title)
      except EOFError:
            print("__"*40)
            fp.close()
      


def findauthor(x):
      b1=bookclass()
      fp=open("book.dat","rb")
      print("__"*50)
      print("Book Code","\t","Name of Book","\t","Author")
      print("__"*50)
      try:
            while True:
                  b1=load(fp)
                  if b1.author==x:
                        print(b1.bookno,"\t",b1.title,"\t",b1.author)
      except EOFError:
            print("__"*50)
            fp.close()
      

def defaulter():
      i1=issue()
      fp=open("Transaction.dat","rb")
      try:
            while True:
                  i1=load(fp)
                  stat=i1.returndate < datetime.date.today()
                  if(stat==True):
                        i1.geti()
      except EOFError:
            pass
      fp.close()
      print()
      
      
      

def reports():
      chrs=0
      
      
      while chrs<7:
            print("     I N F O   R E P O R T S :")
            print()
            print("1. L I S T   O F   M E M B E R S   H A V I N G   B O O K S  ")
            print()
            print("2. L I S T   O F   M E M B E R S   W I T H O U T   B O O K S")
            print()
            print("3. L I S T   O F   B O O K S   I S S U E D")
            print()
            print("4. L I S T   O F   B O O K S   A V A I L A B L E")
            print()
            print("5. F I N D   A    B O O K   O F   A   P A R T I C U L A R   A U T H O R")
            print()
            print("6. D E F A U L T E R S")
            print()
            print("7. -E X I T- ")
            print()
            chrs=int(input("E N T E R   Y O U R   C H O I C E :"))
            print()
            if chrs==1:
                  memwithbook()
                  print()
            elif chrs==2:
                  memwithoutbook()
                  print()
            elif chrs==3:
                  bookissued()
                  print()
            elif chrs==4:
                  bookavailable()
                  print()
            elif chrs==5:
                  a=input("Enter name of author to find:")
                  findauthor(a)
                  print()
            elif chrs==6:
                  print('____'*15)
                  defaulter()
                  print('____'*15)
                  print()


"""Def for book class with parameter"""





'''mainprogram'''


ch=0
while ch<5:
      print()
      print("      M  A  I  N     M  E  N  U:")
      print()
      print("1. B O O K S")
      print()
      print("2. M E M B E R S")
      print()
      print("3. I S S U E S")
      print()
      print("4. R E P O R T S")
      print()
      print("5. E X I T")
      print()
      ch=int(input("- E N T E R   Y O U R   C H O I C E -"))
      print()
      if ch==1:
            books()
      elif ch==2:
            members()
      elif ch==3:
            issues()
      elif ch==4:
            reports()
      


            
      



