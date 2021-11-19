from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    age = db.Column(db.SmallInteger, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    pray_requests = db.relationship(
        "PrayRequest", back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
    )

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __eq__(self, other):
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return NotImplemented

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }

    def __repr__(self):
        return f'User #{self.id}: {self.first_name} {self.last_name}'


class PrayRequest(db.Model):
    __tablename__ = 'pray_requests'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))
    message = db.Column(db.Text)
    is_show = db.Column(db.Boolean, default=True)

    user = db.relationship('User', back_populates="pray_requests")

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'is_show': self.is_show,
        }

    def __repr__(self):
        return f'PrayRequest #{self.id}: {self.message}'