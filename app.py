from flask import Flask,render_template,request,jsonify 

#step 1: Create the flask app instance
app = Flask(__name__)
#step 2: Dummy data for photographers (simulating database)
photographers = [
    {"id":"p1","name": "Amit Lensman","skills": ["Wedding","portrait"],"image":"amit.jpg"},
    {"id":"p2","name": "Sana Clickz","skills": ["Fashion","Event"],"image":"sana.jpg"},
    {"id":"p3","name": "David","skills": ["Fashion"],"image":"david.jpg"},
    {"id":"p4","name": "John doe","skills": ["portrait"],"image":"john.jpg"},
]
#step 3:Dummy availability data mapped by by photographer ID
availability_data = {
    "p1":["2025-06-20", "2026-06-23"],
    "p2":["2025-06-19", "2026-06-22"],
    "p3":["2025-06-20", "2027-06-23"],
    "p4":["2025-06-20", "2028-06-23"],
    
}
#Home page
@app.route('/')
def home():
    return render_template('home.html')
#Booking from routs
@app.route('/book',methods=['GET','POST'])
def book():
    if request.method =='POST':
        photographer_id = request.form.get('photographer_id')
        user_id = request.form.get('user_id')
        date = request.form.get('date')
        
        
        return f"<h2 style='color:green'>Booking confirmed! For {photographer_id} on {date}.</h2>"
        
    return render_template('book.html')
#Display photogrhers
@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers,  availability_data=availability_data)

if __name__ =='__main__':
    app.run(debug=True)