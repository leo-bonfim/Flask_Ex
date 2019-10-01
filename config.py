class Config:
    SECRET_KEY = b'\xed\xf4\x83\xac\x92\x948\x10\xed\x04r\x94\x90\x058\xec\xf5\x84\x8bV\xfe\xceb\xea'
    SQLALCHEMY_DATABASE_URI = "mysql://root:kukabr123@localhost/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    Debug=True


class Testing(Config):
    pass


config = {
    "development": Development,
    "testing": Testing
}