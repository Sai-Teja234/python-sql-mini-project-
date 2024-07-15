import sqlite3

#Delete data
class deletedata:
    def __init__(self):
        self.conn=sqlite3.connect("sms.db")
        self.cur=self.conn.cursor()

#Delete studentdata 
    def deletestudent(self,sid):
        self.cur.execute(f'''
                         delete from student where sid=(
                         {sid}
                         )
''')
        self.conn.commit()
        print("---------Data deleted successfully-----------")

#Delete coursedata
    def deletecourse(self,cid):
        self.cur.execute(f'''
                         delete from course where cid=(
                         {cid}
                         )
''')
        self.conn.commit()
        print("----------Data Deleted Successfully------------")

#Delete Transaction data
    def deletetrans(self,tid):
        self.cur.execute(f'''
                         delete from trans where tid=(
                         {tid}
                         )

''') 
        self.conn.commit()
        print("---------data deleted successfully----------")

        