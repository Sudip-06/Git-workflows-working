from flask import Flask, render_template, request, redirect, flash, url_for
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"
CORS(app)

# Dummy data for dropdowns
services = [{"name": "Plumbing"}, {"name": "Electrician"}, {"name": "Cleaning"}]
cities = [{"city": "Mumbai"}, {"city": "Delhi"}, {"city": "Bangalore"}]

@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
        else:
            flash(f"Signed up successfully as {username}", "success")
            # You can save to DB here
            return redirect(url_for("signup"))

    return render_template("signup2.html", services=services, cities=cities)

if __name__ == "__main__":
    app.run(debug=True)
