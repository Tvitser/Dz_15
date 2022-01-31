import sqlite3
from flask import Flask
app=Flask(__name__)

@app.route("/<item_id>")
def search_by_item_id(item_id):
    with sqlite3.connect("test.db") as conn:
        conn.row_factory=sqlite3.Row
        result=conn.execute(f"""
        SELECT * FROM animals a 
        join animal_type at2
        join animal_breed
        join animal_outcome_type
        join animals_outcome_subtype
        WHERE a."index" = '{item_id}'
        """).fetchall()
        for row in result:
            return dict(row)
app.run()