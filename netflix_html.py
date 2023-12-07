from flask import Flask , render_template
import sqlite3
import pathlib


netflix_html = Flask(__name__)


base_path = pathlib.Path().cwd()
db_name = "Netflix.db"
File_path = base_path / db_name

@netflix_html.route("/")
def index():
    return render_template("index.html")
    
@netflix_html.route("/about")
def about():
    return render_template("about.html")        
    
@netflix_html.route("/data")
def data():
    con = sqlite3.connect(File_path)
    cursor = con.cursor()
    Net_data = cursor.execute("SELECT * FROM Net_data").fetchall()
    con.close()
    return render_template("data_table_fillin.html", Net_data = Net_data)    
    
    
if __name__=="__main__":
    netflix_html.run(debug = True)    