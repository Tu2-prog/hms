from crypt import methods

from flask import render_template, request, redirect, url_for
from models import Palindrome, create_palindrome
from palindrome.transform import Transform
from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    """
    The first route the web application leads to.
    :return: The index html that renders a form to input a number to be transformed.
    """
    if request.method == "GET":
        return render_template("index.html")

    # For a POST request, process the form data
    palindrome_transform = Transform()

    # Get the number from the form
    palindrome_number = int(request.form.get("number_field"))
    computed_palindrome, num_cycles = palindrome_transform.palindrome(palindrome_number)
    palindrome = create_palindrome(palindrome_number, computed_palindrome, num_cycles)
    return render_template("index.html", palindrome=palindrome)


@app.route("/table")
def table():
    # Query all palindrome records from the database
    palindromes = Palindrome.query.all()

    # Render them in table.html
    return render_template("table.html", palindromes=palindromes)
