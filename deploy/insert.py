class insertdata:
    def insertstudent(self, sid, sname, email, city):
        # Insert student logic here
        print(f"Student inserted: {sid}, {sname}, {email}, {city}")

    def insertcourse(self, cid, sid, coursename, price):
        # Insert course logic here
        print(f"Course inserted: {cid}, {sid}, {coursename}, {price}")

    def inserttrans(self, tid, sid, cid, method):
        # Insert transaction logic here
        print(f"Transaction inserted: {tid}, {sid}, {cid}, {method}")
