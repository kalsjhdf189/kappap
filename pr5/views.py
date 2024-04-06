from django.shortcuts import render
import sqlite3

# Create your views here.
def index(request):
    flag = False
    if request.method == "POST":
        login = request.POST.get("login", None)
        password = request.POST.get("password", None)
        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()
        select_sql = "SELECT * FROM users WHERE login = '{}' and password = '{}';".format(login, password)
        cursor = cursor.execute(select_sql)
        for row in cursor:
            if row[0] == login:
                flag = True
    if flag == False:
        return render(request, "index.html")
    else:
        return render(request, "main.html", {'data': login})
