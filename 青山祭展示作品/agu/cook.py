from crypt import methods
from agu import app
from flask import render_template , request,redirect

@app.route('/')
def home():
    return render_template(
        'home.html'
    )
    

@app.route('/ans',methods=['GET','POST'])
def ans():
    if request.method == 'POST':
        get1 = request.form.get('choose1')
        get2 = request.form.get('choose2')
        get3 = request.form.get('choose3')
        return render_template('ans.html', get1=get1,get2=get2,get3=get3)
    else:
        return render_template('home.html')
    
    
    
