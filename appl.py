from flask import Flask, render_template, request, redirect
import datetime
import os

appl = Flask("Note Creation Center")
notes=[]

@appl.route("/")
def home():
    return render_template("main.html", notes = notes, dir = dir)
    
@appl.route("/submit", method =["POST"])
def submit():
    time = datetime.datetime.now()
    print(time)
    ntname = request.form["name"]
    print(ntname)
    notes.append({"name":ntname, "date":time})
    
    ntname +=".html"
    dir = ntname
    print(dir)
    
    ## Creating a file for the note ##
    file = open(ntname, "w")
    file.write(request.formp["data"])
    file.close()
    return redirect("/")

@appl.route("/note/<string:name>", methods =["GET","POST"])
def view(name):
    ## opening the file created to be read and viewed by the user ##
    file = open(name, "r")
    print(file.read())
    return redirect("/", name = name)
    
if __name__ == "__main__":
    appl.run(host = "0.0.0.0", port = 5001)
    
    
