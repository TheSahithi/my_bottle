from bottle import route, run, Bottle, template, request
import math
app=Bottle()
@app.route('/')
def calc():
    return template('calc_final')


@app.post('/display')
def display():
    num1=request.forms.get('num1')
    num2=request.forms.get('num2')
    select1=request.forms.get('select1')
    select2=request.forms.get('select2')
    f = open("history.txt","a")       
    
    num4=request.forms.get('func')
    if num4=='ar':
        if select1=='+':
            num3=int(num1)+int(num2)
        elif select1=='*':
            num3=int(num1)*int(num2)
        elif select1=='-':
            num3=int(num1)-int(num2)
        else:
            if float(num2)<>0:
                num3=float(num1)/float(num2)
    else:
        if select2=='sin':
            num3=math.sin(float(num1)*(math.pi/180))
        elif select2=='cos':
            num3=math.cos(float(num1)*(math.pi/180))
        elif select2=='tan':
            num3=math.tan(float(num1)*(math.pi/180))
        elif select2=='x2':
            num3=int(num1)**2
        elif select2=='sqrt':
            num3=math.sqrt(float(num1))
        else:
            num3=math.exp(float(num1))
        
    if num4=='ar':    
        contents1 = num1+select1+num2+"="+str(num3)+"\n"
        f.write(contents1)
    else:
        contents2 = select2+"("+num1+")"+"="+str(num3)+"\n"
        f.write(contents2)
    f.close()
    return template('display_final', num3=num3) 

@app.post('/show')
def show():
    fr = open("history.txt","r")   
    history=""
    for line in fr:
        history+= line
    fr.close()
    return template('show',history=history)

run(app, host='172.16.3.158', port=7777, debug=True), Bottle, template, request 
