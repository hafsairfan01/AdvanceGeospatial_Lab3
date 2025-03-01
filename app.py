from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Render our template which contains the Leaflet map
    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True)
