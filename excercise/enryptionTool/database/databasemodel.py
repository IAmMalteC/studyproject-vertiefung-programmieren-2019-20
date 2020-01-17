from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User_TB(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    user_password = Column(String(160), nullable=False)
    user_encrypted_string = relationship("EncodedString_TB", back_populates="encoded_string_userstr")

    def __init__(self, name: str, password: str):
        self.user_name = name
        self.user_password = password

    def __init__(self, name: str):
        self.user_name = name
        self.user_password = "default"

    # def __getitem__(self, user_name):
    #     user_name = self.user_name

    def __repr__(self):
        return "User [ID: {0}, name: {1}]".format(self.user_id, self.user_name)


class EncodedString_TB(Base):
    __tablename__ = 'encrypted_string'
    encoded_string_id = Column(Integer, primary_key=True)
    encoded_string_string = Column(String(256), nullable=False)
    encoded_string_user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    encoded_string_userstr = relationship("User_TB", back_populates="user_encrypted_string")
    encoded_string_encryption_type_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), nullable=False)
    encoded_string_typerelation = relationship("EncryptionType_TB", back_populates="encryption_type_typerelation")

    def __init__(self, string: str, user: int, encryption_type: int):
        self.encoded_string_string = string
        self.encoded_string_user_id = user
        self.encoded_string_encryption_type_id = encryption_type

    def __repr__(self):
        return "Encoded string [ID: {0}, String: {1}]".format(self.encoded_string_id, self.encoded_string_string)


class EncryptionType_TB(Base):
    __tablename__ = 'encryption_type'
    encryption_type_id = Column(Integer, primary_key=True)
    encryption_type_type = Column(String(30), nullable=False)
    encryption_type_typerelation = relationship("EncodedString_TB", back_populates="encoded_string_typerelation")

    def __init__(self, type: str):
        self.encryption_type_type = type

    def __repr__(self):
        return "Type of Encryption [ID: {0}, Type: {1}]".format(self.encryption_type_id, self.encryption_type_type)


class Cesar_TB(EncryptionType_TB):
    __tablename__ = 'cesar'
    cesar_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), primary_key=True)
    cesar_offset = Column(Integer)

    def __init__(self, offset: int):
        self.cesar_offset = offset
        self.encryption_type_type = "cesar"

    def __repr__(self):
        return "Cesar:[ID: {0}, Offset: {1}]".format(self.cesar_id, self.cesar_offset)


class MonoAlphabeticSubstitution_TB(EncryptionType_TB):
    __tablename__ = 'mono_alphabetic_substitution'
    mono_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), primary_key=True)

    def __init__(self):
        self.encryption_type_type = "monoalphabeticsubstitution"

    def __repr__(self):
        return "MonoAlphabetic: [ID: {0}]".format(self.mono_id)