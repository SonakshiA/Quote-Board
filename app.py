import os
from flask import Flask, render_template, request;
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = Flask(__name__)
quote=""
author=""

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit",methods=["POST"])
def get_data():
    if request.method=='POST' and 'b1' in request.form:
        quote=request.form['quote']
        quote= '"' + quote + '"'
        author=request.form['author']
        print("Data: " ,quote,author)
        insert_response = (
            supabase.table("Quotes")
            .insert({"Quote":quote,"Author":author})
            .execute()
        )
        fetch_response = supabase.table("Quotes").select("*").execute()
        return render_template("notes.html",results=fetch_response.data)
    if request.method=='POST' and 'b2' in request.form:
        fetch_response = supabase.table("Quotes").select("*").execute()
        return render_template("notes.html",results=fetch_response.data)


if __name__=='__main__':
    app.run()
