from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InfoModel( db.Model ):
    __tablename__ = 'info'
    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String( 80 ) )
    email = db.Column( db.String( 120 ) )

    def __init__( self, name, email ):
        self.name = name
        self.email = email

    def __repr__( self ):
        return '<Name %r>' % self.name # for compatibility with sqlalchemy
     
    def serialize( self ):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
          
        
    
     