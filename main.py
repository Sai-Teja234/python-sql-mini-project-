from insert import insertdata
from update import updatedata
from delete import deletedata 
from read import readdata 
obj=insertdata()
obj2=updatedata()
obj3=deletedata()
obj4=readdata()


print("----------student management system-----------")
print("for insertion press 1,updation press 2 \n deletion press 3,reading press 4")

num=int(input("please enter the options: "))

# INSERTION DATA
if num==1:
    print("choose 1 for student:\n choose 2 for course: \n choose 3 for transaction")
    n=int(input("please enter your option: "))
    if n==1:
        sid=int(input("please enter your studentid: "))
        sname=input("please enter your studentname: ")
        email=input("please enter your studentemail: ")
        city=input("please enter your city: ")
        obj.insertstudent(sid,sname,email,city)

    if n==2:
        cid=int(input("please enter your courseid: "))
        sid=input("please enter your sid: ")
        coursename=input("please enter your coursename: ")
        price=input("please enter your cprice: ")
        obj.insertcourse(cid,sid,coursename,price)

    if n==3:
        tid=int(input("please enter your transid: "))
        sid=input("please enter your student id: ")
        cid=input("please enter your course id: ")
        method=input("please enter your method: ")
        obj.inserttrans(tid,sid,cid,method)


# UPDATION DATA
elif num==2:
    print("choose 1 for update studentdata:\n choose 2 for update coursedata: \n choose 3 for update transaction data:")
    n=int(input("enter number to update:"))
    if n==1:
        sid=int(input("enter student id:"))
        sname=input("enter student name:")
        email=input("enter your email:")
        city=input("enter your city: ")
        obj2.updatestudent(sid,sname,email,city)

    if n==2:
        cid=int(input("enter course id:"))
        sid=input("enter student id:")
        coursename=input("enter course:")
        price=input("enter price: ")
        obj2.updatecourse(cid,sid,coursename,price)

    if n==3:
        tid=int(input("enter transaction id:"))
        sid=input("enter student id:")
        cid=input("enter course id:")
        method=input("enter method of payment: ")
        obj2.updatetrans(tid,sid,cid,method)

            
#Deletion of Data
elif num==3:
    print("choose 1 for delete studentdata:\n choose 2 for delete coursedata:\n choose 3 for delete transactiondata")
    n=int(input("enter the number to delete:"))
    if n==1:
        sid=int(input("enter student id: "))
        obj3.deletestudent(sid)
    if n==2:
        cid=int(input("enter course iD: "))
        obj3.deletecourse(cid)
    if n==3:
        tid=int(input("enter transaction id: "))
        obj3.deletetrans(tid)



# READING OF DATA
elif num==4:
    print("choose 1 read student data:\n choose 2 for read course data:\n choose 3 for read transaction data:")
    n=int(input("enter the number to read:"))
    if n==1:
        obj4.readstudent()
    elif n==2:
       obj4.readcourse()
    elif n==3:
        obj4.readtrans()

    
    
  
  






