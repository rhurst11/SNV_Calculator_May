# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    # SECRET_KEY = config('SECRET_KEY'  , default='S#perS3crEt_007')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

    # SQLALCHEMY_DATABASE_URI = 'postgresql://vaxlquiurzpxoy:32aba92d92139e94020a5bbfe0710ef44b225c9534f059772f8aa2bd1dc5f5e4@ec2-44-207-133-100.compute-1.amazonaws.com:5432/df1c3ejse989jg'

    # current URL listed on heroku

    # URL keeps randomly changing on heroku and I need to understand why. Breaks the app without me having done anything
    SQLALCHEMY_DATABASE_URI = "postgresql://mrihnzxvwbhdyx:6307ba4ebdff413fc7fb37e4e6f78ab14d74698482b039f2841349f3f04c0a8f@ec2-3-217-251-77.compute-1.amazonaws.com:5432/dblpgevgpm3qbr"



    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Assets Management
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')    
    
class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    # SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
    #     os.getenv('DB_ENGINE'   , 'mysql'),
    #     os.getenv('DB_USERNAME' , 'appseed_db_usr'),
    #     os.getenv('DB_PASS'     , 'pass'),
    #     os.getenv('DB_HOST'     , 'localhost'),
    #     os.getenv('DB_PORT'     , 3306),
    #     os.getenv('DB_NAME'     , 'appseed_db')
    # ) 


# heroku postgres URI for calcmvpalpha
# postgres://hruvndtctrrpyk:6ecaaf643d58173ec973e3002c28d138a0c7b7fa2747169599a05d785492cd3a@ec2-34-199-68-114.compute-1.amazonaws.com:5432/da8a58r96bip0j
    3
class DebugConfig(Config):
    DEBUG = False


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
