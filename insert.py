import sqlite3

class insertdata:
    def __init__(self):
        self.conn=sqlite3.connect("sms.db")
        self.cur=self.conn.cursor()
    
    def insertstudent(self,sid,sname,email,city):
        self.cur.execute(f'''
                         INSERT INTO STUDENT VALUES(
                          {sid},
                         "{sname}",
                         "{email}",
                         "{city}"
                         )
''')
        self.conn.commit()
        print("---------DATA ADDED SUCCESSFULLY--------")


    def insertcourse(self,CID,SID,COURSENAME,PRICE):
        self.cur.execute(f'''
                         INSERT INTO COURSE VALUES(
                         {CID},
                         {SID},
                         "{COURSENAME}",
                         {PRICE}
                         )

''')
        self.conn.commit()
        print("---------DATA ADDED SUCCESSFULLY--------")
        
    def inserttrans(self,TID,SID,CID,METHOD):
        self.cur.execute(f'''
                         INSERT INTO TRANS VALUES(
                         {TID},
                         {SID},
                         {CID},
                         "{METHOD}" 
                         )

''')
        self.conn.commit()
        print("---------DATA ADDED SUCCESSFULLY--------")





   
   