from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

   
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def username(self):
        return self.name
    
    @username.setter
    def username(self, name):
        self.name = name
        
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }
        
    
    
      