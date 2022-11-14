from flask import Flask, render_template, request 
from flask_migrate import Migrate
from models import db, InfoModel

app = Flask( __name__ )

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = "postgresql://ericpeltzman:Theboys36@localhost:5432/budget_buddy" #
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False


db.init_app( app )
migrate = Migrate( app, db )

@app.route( '/form' )
def form():
    return render_template( 'form.html' )


@app.route( '/login', methods = [ 'POST', 'GET' ])
def login():
    if request.method == 'GET':
        return "Please submit the form instead."
    elif request.method == 'POST':
        form_data = request.form
        name = form_data[ 'name' ]
        email = form_data[ 'email' ]
        print( name, email )
        info = InfoModel( name = name, email = email )
        db.session.add( info )
        db.session.commit()
        return "Form submitted!"
     
    

     
if __name__ == '__main__':
    app.run(debug=True)   

