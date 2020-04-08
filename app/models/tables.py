from app import db

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String,unique=True)



    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__="posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String)
    title = db.Column(db.String)
    date_posted = db.Column(db.DateTime)
    owner = db.relationship('User', foreign_keys=user_id)


    def __init__(self, user_id, content, title, date_posted, owner):
        self.user_id = user_id
        self.content = content
        self.title = title
        self.date_posted = date_posted
        self.owner = owner

    def __repr__(self):
        return '<Post %r>' % self.id

class Follow(db.Model):
    __tablename__ = "follow"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
