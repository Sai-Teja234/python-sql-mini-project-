from flask import Flask, request, render_template, redirect, url_for
from insert import insertdata
from update import updatedata
from delete import deletedata
from read import readdata

app = Flask(__name__)

obj = insertdata()
obj2 = updatedata()
obj3 = deletedata()
obj4 = readdata()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        data_type = request.form['data_type']
        if data_type == 'student':
            sid = request.form['sid']
            sname = request.form['sname']
            email = request.form['email']
            city = request.form['city']
            obj.insertstudent(sid, sname, email, city)
        elif data_type == 'course':
            cid = request.form['cid']
            sid = request.form['sid']
            coursename = request.form['coursename']
            price = request.form['price']
            obj.insertcourse(cid, sid, coursename, price)
        elif data_type == 'transaction':
            tid = request.form['tid']
            sid = request.form['sid']
            cid = request.form['cid']
            method = request.form['method']
            obj.inserttrans(tid, sid, cid, method)
        return redirect(url_for('index'))
    return render_template('insert.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        data_type = request.form['data_type']
        if data_type == 'student':
            sid = request.form['sid']
            sname = request.form['sname']
            email = request.form['email']
            city = request.form['city']
            obj2.updatestudent(sid, sname, email, city)
        elif data_type == 'course':
            cid = request.form['cid']
            sid = request.form['sid']
            coursename = request.form['coursename']
            price = request.form['price']
            obj2.updatecourse(cid, sid, coursename, price)
        elif data_type == 'transaction':
            tid = request.form['tid']
            sid = request.form['sid']
            cid = request.form['cid']
            method = request.form['method']
            obj2.updatetrans(tid, sid, cid, method)
        return redirect(url_for('index'))
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        data_type = request.form['data_type']
        if data_type == 'student':
            sid = request.form['sid']
            obj3.deletestudent(sid)
        elif data_type == 'course':
            cid = request.form['cid']
            obj3.deletecourse(cid)
        elif data_type == 'transaction':
            tid = request.form['tid']
            obj3.deletetrans(tid)
        return redirect(url_for('index'))
    return render_template('delete.html')

@app.route('/read', methods=['GET', 'POST'])
def read():
    data = None
    if request.method == 'POST':
        data_type = request.form['data_type']
        if data_type == 'student':
            data = obj4.readstudent()
        elif data_type == 'course':
            data = obj4.readcourse()
        elif data_type == 'transaction':
            data = obj4.readtrans()
    return render_template('read.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
