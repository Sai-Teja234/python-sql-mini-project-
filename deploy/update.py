class updatedata:
    def updatestudent(self, sid, sname, email, city):
        # Update student logic here
        print(f"Student updated: {sid}, {sname}, {email}, {city}")

    def updatecourse(self, cid, sid, coursename, price):
        # Update course logic here
        print(f"Course updated: {cid}, {sid}, {coursename}, {price}")

    def updatetrans(self, tid, sid, cid, method):
        # Update transaction logic here
        print(f"Transaction updated: {tid}, {sid}, {cid}, {method}")
