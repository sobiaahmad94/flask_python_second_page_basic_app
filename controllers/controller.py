from app import app

@app.route('/')
def index():
    return "Troy and Abed in the morning!"

@app.route('/<name>')
def greet(name): 
    return f"Hello {name}!"

# http://localhost:5000/Sobia - displays Hello Sobia!
# http://localhost:5000/Spider-Man - displays Hello Spider-Man!

