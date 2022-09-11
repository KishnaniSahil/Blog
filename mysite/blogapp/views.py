from ssl import HAS_TLSv1_1
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
# from requests import request

# Create your views here.

def about(request):
    # title = request.POST['blogTitle']
    # content = request.POST['content']
    # cursor = connection.cursor()
    # cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    # # cursor = connection.cursor()
    cursor=connection.cursor()
    cursor.execute("SELECT * from new_table")
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={'keyposts':posts}
    return render(request,'blogapp/home.html',context)
def create(request):
    return render(request,"blogapp/form.html")
def insert(request):
    # print(request)
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO new_table (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from new_table where content='gif'")
    return  redirect('/text/about') 
def edit(request,pk):
    print(pk)
    cursor = connection.cursor()
    cursor.execute("SELECT * from new_table where  id=%s",pk)
    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context={'keyposts':posts[0]}
    print(context)
    return render(request,"blogapp/form2.html", context)
def update(request):
    title=request.POST['blogTitle']   
    content=request.POST['content'] 
    id=request.POST['id']
    cursor = connection.cursor()
    cursor.execute("UPDATE new_table set title=%s,content=%s where id=%s",(title,content,id)) 
    return  redirect('/text/about') 

        # return HttpResponse("<h1>Hello Template</h1>")
        # return render(request,'blogapp/home.html')

