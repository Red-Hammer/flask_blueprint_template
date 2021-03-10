# Application Factory Blueprint Template for Flask Apps

## Getting Started:
- Open a terminal in the project directory and type the command `python3 -m venv .venv`
- Then enter the virtual environment with `source .venv/bin/activat` (`.venv\Scripts\activate` on Windows)
- To get all the packages, run `pip install -r requirements.txt`
- Create a `.env` file in your base directory and add in:
  

    SECRET_KEY=your-secret-key-here
    
    FLASK_APP=app.py
    
- Test your new app by running `flask run` and typing `http://localhost:5000/` into your browser of choice. You should 
see the 'Hello World!' message.


## Running Migrations with Flask-Migrate (Alembic):
- To initialize your local sqllite db, run `flask db init`
- Then to run your first migration and set the db up, run `flask db migrate`
- A migration versions folder should now be located at `your_base_dir/migrations/versions`
- Check the alembic commands, and if everything looks right, run `flask db upgrade` to create your first tables
- You can run `flask db downgrade` to undo any and all migrations. 
- Migration up/downgrades will be run in the sequence they were created.

