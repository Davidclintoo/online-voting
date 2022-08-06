from ast import Return
from cProfile import label
from enum import unique
from unicodedata import name
from flask import Flask, flash ,render_template, request ,redirect, url_for ,session, flash

import psycopg2
import psycopg2.extras
import os
import secrets
import re


app=Flask(__name__)

app.config['SECRET_KEY'] = 'clintoo333david0001'
#conn=psycopg2.connect("dbname='duka' user='postgres' host='localhost' password='5132'")
conn=psycopg2.connect("dbname='d1m8odf2nbe0jt' user='idlxsyofckzrsu' port='5432 ' host='ec2-52-30-133-191.eu-west-1.compute.amazonaws.com' password='377cc0aab4454edd009635c4786b072f4e75ef0d07fc222ff7020a6c6d950a4a'")


@app.route("/home")

@app.route("/" ,methods=["GET", "POST"])
def index():
    msg=''
    if request.method=="POST" and 'first_name' in request.form and 'last_name' in request.form and 'chair' in request.form and 'vice_chair' in request.form and 'sec' in request.form and 'treasurer' in request.form and 'e_officer' in request.form and 'p_leader' in request.form and 'd_p_leader' in request.form and 'm_officer' in request.form: 
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        first_name=request.form["first_name"]
        last_name=request.form["last_name"],
        chair=request.form["chair"],
        vice_chair=request.form["vice_chair"],
        sec=request.form["sec"],
        org_sec=request.form["org_sec"],
        treasurer=request.form["treasurer"],
        e_officer=request.form["e_officer"],
        p_leader=request.form["p_leader"],
        d_p_leader=request.form["d_p_leader"],
        m_officer=request.form["m_officer"]
        

        rows=(first_name, last_name, chair, vice_chair, sec, org_sec, treasurer, e_officer, p_leader, d_p_leader, m_officer)
        query=("INSERT INTO public.votes( first_name, last_name, chair, vice_chair, sec, org_sec, treasurer, e_officer, p_leader, d_p_leader, m_officer)VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cur.execute(query,rows )
        conn.commit()
        return redirect("/thank")


    return render_template('index.html', msg = msg)


@app.route("/thank")
def thank():

        session['loggedin'] = True
        

        return render_template('thank.html')
            
             
    
    

    



app.run(debug=True)