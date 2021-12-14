from flask import Flask,render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


from datetime import datetime
app = Flask(__name__)
#config
#remember to change the DB filename
app.config['SECRET_KEY'] = "secret Admirer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///survey8.db'
db = SQLAlchemy(app)

class Data(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    sv = db.Column(db.String(100), nullable=False)
    #date = db.Column(db.Date, default=datetime.now)
    date = db.Column(db.DateTime, default=datetime.now)
    
    student = db.Column(db.String(100), nullable=False)
    desig = db.Column(db.String(100), nullable=False)
    a1 = db.Column(db.String(2), nullable=False)
    a2 = db.Column(db.String(2), nullable=False)
    b1 = db.Column(db.String(2), nullable=False)
    b2 = db.Column(db.String(2), nullable=False)
    b3 = db.Column(db.String(2), nullable=False)
    c1 = db.Column(db.String(2), nullable=False)
    c2 = db.Column(db.String(2), nullable=False)
    c3 = db.Column(db.String(2), nullable=False)
    c4 = db.Column(db.String(2), nullable=False)
    c5 = db.Column(db.String(2), nullable=False)
    c6 = db.Column(db.String(2), nullable=False)
    c7 = db.Column(db.String(2), nullable=False)
    comment = db.Column(db.Text, nullable=False)

#create constructor
def __init__(self, sv,student,desig,comment, a1, a2, b1, b2, b3, c1, c2, c3, c4, c5, c6, c7):
    self.sv = sv
    self.student = student
    self.desig = desig
    self.a1 - a1
    self.a2 - a2
    self.b1 - b1
    self.b2 - b2
    self.b3 - b3
    self.c1 - c1
    self.c2 - c2
    self.c3 - c3
    self.c4 - c4
    self.c5 - c5
    self.c6 - c6
    self.c7 - c7
    self.comment = comment

@app.route('/thanku')
def thanku():
	
	return render_template("thanku.html")

@app.route('/')
def index():
	
	student = [
	'ABIGAYLE ALYSHIA ANAK JOSEPH',
	'AGNES AREN PERIDDIE',
	'ALEXANDER HEE CHUN FU',
	'ALISA BINTI MOHAMAD NOR',
	'ALLYSHA BINTI JEFFRIY',
	'ALVIN HAWKINS ANAK MENTRI',
	'ANJELICA MARY ANAK HICTSON',
	'ASMA ARIFAH BINTI BERAWI',
	'ASMIRA SHAZLEENA BINTI ISMAWI',
	'AZNEESHA BINTI AZIZ',
	'BECKHAM GILBERT JUING ANAK BENSON JELANG',
	'BEROLIN ANAK TINDIN',
	'CANDELINI ANAK MICHAEL TIO',
	'CARL ISAAC ANAK KELBIN',
	'CHAI SIAW HUNG',
	'DIANA TRIN ANAK SUDOK @ REGGIE',
	'ELIZEBETH SOUTHWELL PETERUS',
	'FATIN NAZIRAH BINTI SAPUANI',
	'FERDINAND ALEX ANAK ATANG',
	'FERNANDEZ SUNG',
	'FRANCISCCA ANAK UBIN',
	'FREDERICK JACK ANAK UMIN',
	'GENNEVY GILL ANAK MACKENZIE',
	'GRACE ANAK LIMAN',
	'GWENDOLYN RIA FAM',
	'HAIFA SYATIRAH BINTI JAMIL',
	'HAXXEL D`HEWITTS LIAW ANAK HENRY',
	'HAZWANI BINTI ALFIAN',
	'IJAZ DYLAN AHMED BIN ZAINAL ABIDIN', 
	'IVY CHELSY ANAK MICHAEL ELTON',
	'JONG JIA CHEE',
	'JONG THIAN FU',
	'LEE SHAN YUNG',
	'MARRIANE CARRIE JURANI',
	'MICHELIA AMBAK ANAK MONG',
	'MILLENNIA ANAK SAWING',
	'MOHD RUZAINI BIN ABU BAKAR',
	'MUHAMAD AUDI BIN PASHA',
	'MUHAMMAD HAYYQAL BIN JEFFRY',
	'MUHAMMAD NUR AIMAN HAQIMI BIN ROMAINOOR',
	'MUHAMMAD RABANI BIN DRAHMAN',
	'NATASHIEA ANAK BALA',
	'NICOLE VIVIENNE VOO',
	'NUQMAN HAKEM BIN YUSUP',
	'NUR AFIQAH BINTI HABA',
	'NUR ASSHIMA BINTI SUKARDI',
	'NUR FATIHA BINTI BURAHIM',
	'NURIN NAZIHAH BINTI ZULKANAIN',
	'NURUL ERANAZIERA SHAMIMI BINTI SAMRA',
	'NURUL IBTISYAM BIN SUHARDI',
	'OLIVIA HUSSEY AK JIMMY',
	'PEGGIE ANGGAN ANAK PUSO',
	'SAIDATUL NORASIKIN BINTI MD. ZAINAL',
	'SHAROL NAZREN BIN SARKAWI',
	'SHAWN FUM JUN XUAN',
	'SITI NURAISYAH ABDULLAH',
	'VANESSA ANAK RICHARD',
	'WIMVEN CHU WEI FENG',
	'YAP ZUO YIN',
	'ZULHELMI BIN BOLHI'
	]
	

	return render_template("main.html", student = student)

@app.route('/submit', methods = ['POST','GET'])
def submit():
	
	if request.method == 'POST':
		sv = request.form['sv']
		student = request.form['student']
		desig = request.form['desig']
		a1 = request.form['a1']
		a2 = request.form['a2']
		b1 = request.form['b1']
		b2 = request.form['b2']
		b3 = request.form['b3']
		c1 = request.form['c1']
		c2 = request.form['c2']
		c3 = request.form['c3']
		c4 = request.form['c4']
		c5 = request.form['c5']
		c6 = request.form['c6']
		c7 = request.form['c7']
		comment = request.form['comment']
		my_data = Data(sv=sv, student = student, desig=desig, a1=a1, a2=a2, b1=b1, b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, comment=comment )
		db.session.add(my_data)
		db.session.commit()
		
	return redirect(url_for("thanku"))
	



if __name__ == '__main__':
	db.create_all()
	app.run()
