from flask import Flask, redirect, url_for, request,render_template,Response
import csv
import os,datetime
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/newMovies')
def fetchNewMovies():
	oldtime=[]
	for files in os.listdir("."):
			if files.endswith(".csv"):
				t=str(datetime.datetime.fromtimestamp(os.path.getmtime(files))).split()[1]
				x=t.split(":")
				oldtime.append(float(x[2])+float(x[1])*60+float(x[0])*3600)
	while True:
		i=0
		for files in os.listdir("."):
			if files.endswith(".csv"):
				t=str(datetime.datetime.fromtimestamp(os.path.getmtime(files))).split()[1]
				x=t.split(":")
				sums=int(float(x[2])+float(x[1])*60+float(x[0])*3600)
				if sums>oldtime[i]:
					oldtime[i]=sums
					film=list(csv.reader(open(files)))[-1]
					print film
					resp=Response("event:received\nretry:1000\ndata:"+" ".join(film)+"\n\n")
					resp.headers["Content-type"]="text/event-stream"
					return resp
					#return Response("event:received\nretry:1000\ndata:"+" ".join(film)+"\n\n",mimetype="text/event-stream")
			i+=1
					
				
				

@app.route('/buy/<files>/<name>/Submitting',methods = ['POST'])
def Register(files,name):
	r=csv.reader(open(files+".csv"))
	lines=[l for l in r]
	row=0
	print lines
	for i in xrange(len(lines)):
		if lines[i][0]==name:
			row=i
			break
	if lines[row][2]<=0:
		return "Already Houseful"
	lines[row][2]=str(int(lines[row][2])-int(request.form["NoCD"]))
	print lines
	writer=csv.writer(open(files+".csv","w"))
	writer.writerows(lines)
	return "Accepted"

@app.route('/buy/<files>/<Name>')
def CDbuy(files,Name):
	names={}
	names['movieName']=Name
	names['fromFile']=files
	return render_template('buyit.html', name = names)
	
@app.route('/Chcekavb.php/<Name>/<files>')
def value(Name,files):
	f1=open(files+".csv","r")
	for i in csv.reader(f1):
		if(i[0]==Name):
			if(i[2]>0):
				return Name+":Available"
			break
	return Name+":Not Available"
	
@app.route("/buy/<files>/present/<name>")
def buyit(files,name):
	print name,files
	f1=open(files+".csv","r")
	for i in csv.reader(f1):
		if(i[0]==name):
			if(i[2]>0):
				return i[2]
			else:
				return "HouseFul"

@app.route('/login',methods = ['POST', 'GET'])
def login():
    print "Hi"
    if request.method == 'POST':
        filter1 = request.form['filter-1']
        filter2 = request.form['filter-2']
        filter3 = request.form['filter-3']
        c,u=function(filter1,filter2,filter3)
        dict={}
        if len(c)<3:
            dict[filter1]=u[0]
            dict[filter2]=u[1]
            dict[filter3]=u[2]
            return render_template('login.html', name = dict)
        else:
            dict[filter1]=c[0]
            dict[filter2]=c[1]
            dict[filter3]=c[2]
            return render_template('login.html', name = dict)
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

def function(x,y,z):
    print x,y,z
    file1=str(x)+".csv"
    f1=open(file1)
    file2=str(y)+".csv"
    f2=open(file2)
    file3=str(z)+".csv"
    f3=open(file3)
    fi1=[]
    fi2=[]
    fi3=[]
    for i in csv.reader(f1):
        fi1.append(i[0])
    for j in csv.reader(f2):
        fi2.append(j[0])
    for k in csv.reader(f3):
        fi3.append(k[0])
    common=set(fi1) & set(fi2) & set(fi3)
    common=list(common)
    uncommon=[fi1[0],fi2[0],fi3[0]]
    return common,uncommon

if __name__ == '__main__':
    app.run(debug = True)
