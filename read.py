import sqlite3

class readdata:
    def __init__(self):
        self.conn=sqlite3.connect("sms.db")
        self.cur=self.conn.cursor()
    
    #Read Student Data
    def readstudent(self):
        self.cur.execute("select * from student")
        student=self.cur.fetchall()
        print("------------Student Data Accessed---------------")
        for studentdata in student:
            print(studentdata)

    #Read Course Data
    def readcourse(self):
        self.cur.execute("select * from course")
        course=self.cur.fetchall()
        print("------------Course Data Accessed-------------")
        for coursedata in course:
            print(coursedata)

    #Read Transaction data
    def readtrans(self):
        self.cur.execute("select * from trans")
        trans=self.cur.fetchall()
        print("--------Transaction Data Accessed-----------")
        for transdata in trans:
            print(transdata)



    