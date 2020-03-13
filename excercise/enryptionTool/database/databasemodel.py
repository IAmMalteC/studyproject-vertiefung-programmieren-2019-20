from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserTB(Base):
    """ Defines the UserTB for the database"""
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    user_password = Column(String(160))
    # Creates a relationship to the EncodedStringTB
    user_encrypted_string = relationship("EncodedStringTB", back_populates="encoded_string_userstr")

    def __init__(self, name: str, password: str = None):
        self.user_name = name
        self.user_password = password

    def __repr__(self):
        return "User [ID: {0}, name: {1}]".format(self.user_id, self.user_name)


class EncodedStringTB(Base):
    """ Defines the EncodedStringTB for the database"""
    __tablename__ = 'encrypted_string'
    encoded_string_id = Column(Integer, primary_key=True)
    encoded_string_string = Column(String(256), nullable=False)
    # Creates a relationship to the UserTB
    encoded_string_user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    encoded_string_userstr = relationship("UserTB", back_populates="user_encrypted_string")
    # Creates a relationshipl to the EncryptionTypeTB
    encoded_string_encryption_type_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), nullable=False)
    encoded_string_typerelation = relationship("EncryptionTypeTB", back_populates="encryption_type_typerelation")

    def __init__(self, string: str, user: int, encryption_type: int):
        self.encoded_string_string = string
        self.encoded_string_user_id = user
        self.encoded_string_encryption_type_id = encryption_type

    def __repr__(self):
        return "Encoded string [ID: {0}, String: {1}]".format(self.encoded_string_id, self.encoded_string_string)


class EncryptionTypeTB(Base):
    """ Defines the EncryptionTypeTB for the database"""
    __tablename__ = 'encryption_type'
    encryption_type_id = Column(Integer, primary_key=True)
    encryption_type_type = Column(String(30), nullable=False)
    # Creates a relationship to the EncodedStringTB
    encryption_type_typerelation = relationship("EncodedStringTB", back_populates="encoded_string_typerelation")

    def __init__(self, encryption_type: str):
        self.encryption_type_type = encryption_type

    def __repr__(self):
        return "Type of Encryption [ID: {0}, Type: {1}]".format(self.encryption_type_id, self.encryption_type_type)


class CesarTB(EncryptionTypeTB):
    """ Defines the CesarTB for the database,
    is an extension of EncryptionTypeTB
    """
    __tablename__ = 'cesar'
    cesar_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), primary_key=True)
    cesar_offset = Column(Integer)

    def __init__(self, offset: int):
        self.cesar_offset = offset
        self.encryption_type_type = "cesar"

    def __repr__(self):
        return "Cesar:[ID: {0}, Offset: {1}]".format(self.cesar_id, self.cesar_offset)


class MonoAlphabeticSubstitutionTB(EncryptionTypeTB):
    """ Defines the Mono...TB for the database,
    is an extension of EncryptionTypeTB
    """
    __tablename__ = 'mono_alphabetic_substitution'
    mono_id = Column(Integer, ForeignKey('encryption_type.encryption_type_id'), primary_key=True)

    def __init__(self):
        self.encryption_type_type = "monoalphabeticsubstitution"

    def __repr__(self):
        return "MonoAlphabetic: [ID: {0}]".format(self.mono_id)
