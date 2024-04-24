from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)   
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rup@Ras#54'
app.config['MYSQL_DB'] = 'e_bond'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("rug_1.html")

@app.route('/a_1', methods = ["POST", "GET"])
def a_1():
    if request.method == "POST":        
        s1 = request.form["parameter"]
        s2 = request.form["box"]
        cursor = mysql.connection.cursor()
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
        cursor.execute("SELECT * FROM complete_bonds WHERE " + s1 + " LIKE %s", ('%' + s2 + '%',))

        data = cursor.fetchall()

        cursor.close()

    return render_template("rug_1_1.html", a_1_data = data) 

@app.route('/a_2', methods = ["POST", "GET"])
def a_2():
    if request.method == "POST":        
        cmpny = request.form["cmpny"]
        cursor = mysql.connection.cursor()
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
        cursor.execute("SELECT YEAR(Date_of_Purchase) as Year_of_purchase, count(*) as `No. of bonds puchased` from company_bonds  where Name_of_the_Purchaser = %s group by Year_of_Purchase",(cmpny,))

        data = cursor.fetchall()
        # print(data[0])
        # print(data[1])

        cursor.close()

    return render_template("rug_2.html", a_2_data = data) 

@app.route('/a_3', methods = ["POST", "GET"])
def a_3():
    if request.method == "POST":        
        party = request.form["party"]
        cursor = mysql.connection.cursor()
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
        cursor.execute("SELECT YEAR(Date_of_Encashment) as Year_of_encashment, count(*) as `No. of bonds puchased` from party_bonds_1  where Name_of_the_Political_Party = %s group by Year_of_Encashment",(party,))

        data = cursor.fetchall()
        # print(data[0])
        # print(data[1])

        cursor.close()

    return render_template("rug_3.html", a_3_data = data)

@app.route('/a_4', methods = ["POST", "GET"])
def a_4():
    if request.method == "POST":        
        party = request.form["party"]
        cursor = mysql.connection.cursor()
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
        cursor.execute("select Name_of_the_Purchaser as `Company/Indivisual`, sum(Denominations) as `Total amount contributed`from complete_bonds where Name_of_the_Political_Party = %s group by Name_of_the_Purchaser",(party,))

        data = cursor.fetchall()
        # print(data[0])
        # print(data[1])

        cursor.close()

    return render_template("rug_1.html", a_4_data = data)

@app.route('/a_5', methods = ["POST", "GET"])
def a_5():
    if request.method == "POST":        
        cmpny = request.form["cmpny"]
        cursor = mysql.connection.cursor()
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
        cursor.execute("select Name_of_the_Political_Party as `Political Party`, sum(Denominations) as `Total amount contributed`from complete_bonds where Name_of_the_Purchaser = %s group by Name_of_the_Political_Party",(cmpny,))

        data = cursor.fetchall()
        # print(data[0])
        # print(data[1])

        cursor.close()

    return render_template("rug_1.html", a_5_data = data)

@app.route('/a_6', methods = ["POST", "GET"])
def a_6():
    # data = None
    if request.method == "POST":        
        k = request.form["true"]
        cursor = mysql.connection.cursor()
        if k == "YES":
        # cursor.execute("select * from complete_bonds where s1 like %s = s2 like %s",(s1,s2))
            cursor.execute("select Name_of_the_Political_Party as 'Party', sum(Denominations) as `Total amount given` from party_bonds_1 group by Name_of_the_Political_Party")

            data = cursor.fetchall()
        # print(data[0])
        # print(data[1])

        cursor.close()

    return render_template("rug_6.html", a_6_data = data)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 