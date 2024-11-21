from flask import Flask, request, jsonify, render_template, url_for, flash, session, redirect
import mysql.connector


app=Flask(__name__)

db=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#1234",
    database="stock_management"
)

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/BuyPhone.html")
def buy():
    return render_template("BuyPhone.html")


@app.route('/oppo.html',methods=["GET","POST"])
def oppo():
    if request.method=="POST":
        m_no=request.form.get('m_no')
        co=request.form.get('count')
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )
        c=conn.cursor(dictionary=True)
        c.execute("update table oppo set stock=stock-%s where m_no=%s",(co,m_no))
        conn.commit()
        c.close()
        conn.close()

    else:
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )

        c=conn.cursor(dictionary=True)
        c.execute("Select * from oppo")
        u=c.fetchall()
        c.close()
        conn.close()
        return render_template('oppo.html',u=u)


@app.route('/redmi.html',methods=["GET","POST"])
def redmi():
    if request.method=="POST":
        m_no=request.form.get('m_no')
        co=request.form.get('count')
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )
        c=conn.cursor(dictionary=True)
        c.execute("update table redmi set stock=stock-%s where m_no=%s",(co,m_no))
        conn.commit()
        c.close()
        conn.close()

    else:
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )

        c=conn.cursor(dictionary=True)
        c.execute("Select * from redmi")
        u=c.fetchall()
        c.close()
        conn.close()
        return render_template('redmi.html',u=u)

@app.route('/sam.html',methods=["GET","POST"])
def sam():
    if request.method=="POST":
        m_no=request.form.get('m_no')
        co=request.form.get('count')
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )
        c=conn.cursor(dictionary=True)
        c.execute("update table sam set stock=stock-%s where m_no=%s",(co,m_no))
        conn.commit()
        c.close()
        conn.close()

    else:
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )

        c=conn.cursor(dictionary=True)
        c.execute("Select * from sam")
        u=c.fetchall()
        c.close()
        conn.close()
        return render_template('sam.html',u=u)
    

@app.route('/vivo.html',methods=["GET","POST"])
def vivo():
    if request.method=="POST":
        m_no=request.form.get('m_no')
        co=request.form.get('count')
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )
        c=conn.cursor(dictionary=True)
        c.execute("update table vivo set stock=stock-%s where m_no=%s",(co,m_no))
        conn.commit()
        c.close()
        conn.close()

    else:
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )

        c=conn.cursor(dictionary=True)
        c.execute("Select * from vivo")
        u=c.fetchall()
        c.close()
        conn.close()
        return render_template('vivo.html',u=u)
    


@app.route('/AddPhone.html',methods=["GET","POST"])
def add():

    if request.method=='POST':
        m_no=request.form.get('Model_Number')
        m_name=request.form.get('Model_Name')
        pri=request.form.get('Price')
        sto=request.form.get('Storage')
        dis=request.form.get('Display')
        ram=request.form.get('RAM')
        st=request.form.get('Stock')
        com=request.form.get('Company')
        conn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="#1234",
            database="stock_management"
        )
        c=conn.cursor(dictionary=True)
        c.execute('insert into %s values(%s,%s,%s,%s,%s,%s,%s)',(com,m_no,m_name,pri,ram,sto,dis,st))
        conn.commit()
        c.close()
        conn.close()
    
    else:
        return render_template('AddPhone.html')

if __name__=="__main__":
    app.run(debug=True)