from flask import Flask, render_template, request, session, redirect, url_for
from flask_migrate import Migrate
from models import db, User

app = Flask( __name__ )

app.config[ 'SQLALCHEMY_DATABASE_URI' ] = "postgresql://ericpeltzman:Theboys36@localhost:5432/budget_buddy" #
app.config[ 'SQLALCHEMY_TRACK_MODIFICATIONS' ] = False
db.init_app( app )
migrate = Migrate( app, db )

@app.route( '/form' )
def form():
    return render_template( 'form.html' )

@app.route( '/submit' , methods = [ 'POST' ] )
def submit():
    if request.method == 'POST':
        name = request.form[ 'name' ]
        email = request.form[ 'email' ]
        print( name, email )
        data = User( name, email )
        db.session.add( data )
        db.session.commit()
        return redirect( url = 'http://localhost:5000/form' )
    
@app.route( '/users' ) 
def users():
    users = User.query.all()
    return render_template( 'users.html' , users = users )

if __name__ == '__main__':
    app.run( debug = True )