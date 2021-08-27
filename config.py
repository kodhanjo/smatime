import os
class Config:
   SECRET_KEY='DFGJKL.,MN'
   SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://mwashe:github2122@localhost/employes'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    
    DEBUG=True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}