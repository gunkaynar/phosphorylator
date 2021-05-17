from flask import Flask, request, render_template
app = Flask(__name__ ,static_url_path = "", static_folder = "static")
import sqlite3


@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home')
def homebutton():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/phos_last', methods =['GET','POST'])
def form_example():
    conn = sqlite3.connect('phosphorylator.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        protein= request.form.get('protein')
        if protein =='':
            return render_template('phos_last_error.html',error='Please write a protein')
        else:
            try:
                protein=protein.upper()
                cursor.execute("SELECT * FROM records WHERE mouse=? ",(protein,));
                row = cursor.fetchone();
                return render_template('result_phos_last.html', protein=row[0], human_n=row[2], both=row[3], only=row[4])
            except TypeError:
                return render_template('phos_last_error.html',error='Could not find the protein')
    return render_template('phos_last.html')
           
     
@app.route('/newdic',methods=['GET','POST'])
def form_example3():
    conn = sqlite3.connect('phosphorylator2.db')
    cursor = conn.cursor()
    if request.method =='POST':
        protein3=request.form.get('protein3')
        distance=request.form.get('distance')
        if protein3=='' and not distance=='':
            return render_template('newdic_error.html',error='Please write a protein')
        elif  distance=='' and not protein3=='':
            return render_template('newdic_error.html',error='Please write a range')
        elif distance=='' and protein3=='':
            return render_template('newdic_error.html',error='Please write a protein and a range')
        else:
            try:
                protein3 = protein3.upper()
                protein3= protein3.replace(' ','')
                cursor.execute("SELECT * FROM records WHERE mouse=? ORDER BY abs(dif) ",(protein3,));
                rows = cursor.fetchall()
                rowr=[]
                for row in rows:
                    if abs(int(row[1]))<=int(distance):
                        rowr.append(row)
                if rowr == []:
                    return render_template('newdic_error.html',error='Could not find')
                else:
                    return render_template('result_newdic.html',rows=rowr)
            except TypeError:
                return render_template('newdic_error.html',error='Could not find')
            except ValueError:
                return render_template('newdic_error.html',error='Please write a integer for range')
 
    return render_template('newdic.html')

if __name__ == '__main__':
    app.run(debug=False, port=5000)