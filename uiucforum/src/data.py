import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm


csv_file = r'C:\Users\Mirza\Downloads\course-catalog.csv'
def extract(csv_file):
    subject_number_set = set()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)


        for row in reader:
            subject_number_set.add((row['Subject'], row['Number'], row['Name']))

    return subject_number_set

unique = extract(csv_file)
uniquesort = sorted(unique)


def convert_set_to_csv(grok_set, output_file):
    fieldnames = ['Class', 'Number', 'Name']
    
    # Open CSV file for writing
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(fieldnames)
        
        for row in grok_set:
            writer.writerow(row[:3])

output_csv_file = 'class_data.csv'
convert_set_to_csv(uniquesort, output_csv_file)

Base = declarative_base()

engine = create_engine('sqlite:///database.db', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()

session.commit()

results = session.query(User).all()

print(results)


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max = 30)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max = 30)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max = 30)])
    remember = BooleanField('Remember me')
    submit = SubmitField('login')