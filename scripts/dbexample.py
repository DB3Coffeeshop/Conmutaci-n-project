import MySQLdb

def conectar():
    db = MySQLdb.connect("LocalHost", "root", "natalia1", "COMPENSAR") #Ignoren la contra, no supe como cambiarla
    cur = db.cursor()
    sql = "INSERT INTO Student(code, name) VALUES(1244, 'caca')"
    sql2 = "SELECT * FROM Student"
    search = "SELECT * FROM Student WHERE code=123"
    cur.execute(search)
    #db.commit()
    data = cur.fetchall()

    for i in data:
        print i

    db.close

conectar()
