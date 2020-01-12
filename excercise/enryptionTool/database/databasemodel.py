from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User_TB(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "User [ID: {0}, name: {1}]".format(self.id, self.name)


class EncodedString_TB(Base):
    __tablename__ = 'encrypted_string'
    id = Column(Integer, primary_key=True)
    string = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    userstr = relationship("User", back_populates="encrypted_string")
    encryption_type_id = Column(Integer, ForeignKey('encryption_type.id'), nullable=False)
    encryptiontyperelation = relationship("EncryptionType", back_populates="type_relation")

    def __init__(self, string: str, user: int, encryption_type: int):
        self.string = string
        self.user_id = user
        self.encryption_type_id = encryption_type

    def __repr__(self):
        return "Encoded string [ID: {0}, String: {1}]".format(self.id, self.string)


class EncryptionType_TB(Base):
    __tablename__ = 'encryption_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)
    type_relation = relationship("EncodedString", back_populates="encryptiontyperelation")

    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return "Type of Encryption [ID: {0}, Type: {1}]".format(self.id, self.type)


class Cesar_TB(EncryptionType_TB):
    __tablename__ = 'cesar'
    id = Column(Integer, ForeignKey('encryption_type.id'), primary_key=True)
    offset = Column(Integer)

    def __init__(self, offset: int):
        self.offset = offset
        self.type = "cesar"

    def __repr__(self):
        return "Cesar:[ID: {0}, Offset: {1}]".format(self.id, self.offset)


class MonoAlphabeticSubstitution_TB(EncryptionType_TB):
    __tablename__ = 'mono_alphabetic_substitution'
    id = Column(Integer, ForeignKey('encryption_type.id'), primary_key=True)

    def __init__(self):
        self.type = "monoalphabeticsubstitution"

    def __repr__(self):
        return "MonoAlphabetic: [ID: {0}]".format(self.id)