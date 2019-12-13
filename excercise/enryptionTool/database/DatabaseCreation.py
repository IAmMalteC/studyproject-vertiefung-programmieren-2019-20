from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# relationship is used to connect the FK
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    # meta.create_all(engine)
    # Creates the relationships with the foreignkey
    User.encoded_string = relationship("EncodedString", order_by=EncodedString.id, back_populates="userstr")
    EncodingType.encoded_string = relationship("EncodedString", order_by=EncodedString.id,
                                               back_populates="encodingtypestr")
    EncodingType.cesar = relationship("Cesar", order_by=Cesar.id, back_populates="encoding_typec")
    EncodingType.mono_alphabetic_substitution = relationship("MonoAlphabeticSubstitution",
                                                             order_by=MonoAlphabeticSubstitution.id,
                                                             back_populates="encoding_typem")
    Base.metadata.create_all(engine)
    return engine


def open_session(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "User [ID: {0}, name: {1}]".format(self.id, self.name)


class EncodingType(Base):
    __tablename__ = 'encoding_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False, unique=True)

    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return "Type of Encryption [ID: {0}, Type: {1}]".format(self.id, self.type)


class EncodedString(Base):
    __tablename__ = 'encoded_string'
    id = Column(Integer, primary_key=True)
    string = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    userstr = relationship("User", back_populates="encoded_string")
    encoding_type_id = Column(Integer, ForeignKey('encoding_type.id'), nullable=False)
    encodingtypestr = relationship("EncodingType", back_populates="encoded_string")

    def __init__(self, string: str, user: int, encoding_type: int):
        self.string = string
        self.user_id = user
        self.encoding_type_id = encoding_type

    def __repr__(self):
        return "Encoded string [ID: {0}, String: {1}]".format(self.id, self.string)


class Cesar(Base):
    __tablename__ = 'cesar'
    id = Column(Integer, primary_key=True)
    offset = Column(Integer)
    encoding_type_id = Column(Integer, ForeignKey('encoding_type.id'), nullable=False)
    encoding_typec = relationship("EncodingType", back_populates="cesar")

    def __init__(self, offset: int, encodingtype: int):
        self.offset = offset
        self.encoding_type_id = encodingtype

    def __repr__(self):
        return "Cesar:[ID: {0}, Offset: {1}]".format(self.id, self.offset)


class MonoAlphabeticSubstitution(Base):
    __tablename__ = 'mono_alphabetic_substitution'
    id = Column(Integer, primary_key=True)
    encoding_type_id = Column(Integer, ForeignKey('encoding_type.id'), nullable=False)
    encoding_typem = relationship("EncodingType", back_populates="mono_alphabetic_substitution")

    def __init__(self, encodingtype: int):
        self.encoding_type_id = encodingtype


    def __repr__(self):
        return "MonoAlphabetic: [ID: {0}]".format(self.id)
