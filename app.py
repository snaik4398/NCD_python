### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
# welcome page
@app.route('/')
def welcome():
    return render_template('signup.html')
# when we tap to the back button it will go to the index.html page 
@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('signup.html')


def home():
    #Moving forward code
    return redirect(url_for('welcome'))

@app.route('/success/<int:score>')
def success(score):
    res=""
    print(score)
    if score>=4:
        res="NEED TO CHECHK UP"
    else:
        res="NO NEED TO CHECHK UP"

    return render_template('result.html',result=res,sc=score)


@app.route('/fail/<string:s>')
def fail(s):
    return s+"     please enter the valid input as written in the webpage"

# ### Result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result=""
#     if marks<50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))

### Result checker submit html page
@app.route('/signup',methods=['POST','GET'])
def signup():
    nm =" "
    # age=""
    email=" "
    gen1=" "
    pin=" "
    dob= " "

    
    if request.method=='POST':
        nm=request.form['fname']
        nm+=" "
        nm+= request.form['lname']

        gen1=request.form['gender']
        dob=request.form['birthday']
        email=request.form['email']
        pin=request.form['pincode']


    
    return render_template('index.html',nm=nm,gen=gen1,pin=pin,dob=dob,email=email)


@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    c=0
    if request.method=='POST':
        a1=int(request.form['age'])
        if (a1>3 or a1<0):
            return redirect(url_for('fail',s="invalid input"))
              

         
        p2=int(request.form['2pp'])
        if (p2>2 or p2<0):
            return redirect(url_for('fail',s="invalid input"))
       
        p3=int(request.form['3pp'])
        if (p3>1 or p3<0):
            return redirect(url_for('fail',s="invalid input"))
        p4=int(request.form['4pp'])
        if (p4>3 or p4<0):
            return redirect(url_for('fail',s="invalid input"))
        p5=int(request.form['5pp'])
        if (p5>2 or p5<0):
            return redirect(url_for('fail',s="invalid input"))
        p6=int(request.form['6pp'])
        if (p6>2 or p6<0):
            return redirect(url_for('fail',s="invalid input"))
    
        total_score=(c+p2+p3+p4+p5+p6)
        
      
    res=""
    return redirect(url_for('success',score=total_score))

    



if __name__=='__main__':
    app.run(debug=True,port=4398)