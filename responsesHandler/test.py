from flask import Flask, render_template, request, jsonify
from mysql import connector as myc
app = Flask("__name__")

details = dict()

@app.route("/")
@app.route("/register")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    details["name"] = request.form.get("name")
    details["username"] = request.form.get("username")
    details["age"] = request.form.get("age")
    details["email"] =request.form.get("email")
    details["password"] = request.form.get("password")
    details["confirmpassword"] = request.form.get("confirmpass")
    details["phnum"] = request.form.get("phnum")

    databaseInsertion()

    return render_template("form.html")

@app.route("/request")
def requestJson():
    return jsonify(
        name=details["name"],
        username=details["username"],
        age=details["age"],
        email=details["email"],
        phnum=details["phnum"],
        password=details["password"],
        confirmpassword=details["confirmpassword"]
    )

def databaseInsertion():
    # mysql = MySQL()
    # app.config['MYSQL_DATABASE_USER'] = 'root'
    # app.config['MYSQL_DATABASE_PASSWORD'] = ''
    # app.config['MYSQL_DATABASE_DB'] = 'flaskdb'
    # app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    # mysql.init_app(app)

    # conn = mysql.connect()
    # cursor =conn.cursor()

    # cursor.execute("INSERT INTO userdata(`FullName`, `UserName`, `Age`, `Email`, `PhoneNumber`, `Password`, `ConfirmPassword`) VALUES ("
    # +str(details["name"])+","+str(details["username"])+","+str(details["age"])
    # +","+str(details["email"])+","+str(details["phnum"])+","+str(details["password"])
    # +","+str(details["confirmpassword"])+')')
    
    mydb = myc.connect(host="localhost",user="root",password="",database="flaskdb")

    mycursor = mydb.cursor()
    sql = "INSERT INTO userdata (FullName, UserName, Age, Email, PhoneNumber, Password, ConfirmPassword) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (str(details["name"]), str(details["username"]), str(details["age"]), str(details["email"]), str(details["phnum"]), str(details["password"]), str(details["confirmpassword"]))
    mycursor.execute(sql, val)
    mydb.commit()

if __name__=="__main__":
    app.run(debug=True)