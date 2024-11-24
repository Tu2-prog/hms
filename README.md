# HMS - Coding Challenge
This is the code repository for the coding challenge sent by HMS for me to solve. The challenge was to
implement a Transform class that transforms an int into a palindrome. Unfortunately not all parts could have
been implemented fully.
___
# Prerequisites
This project is implemented in Python 3.11.10. For the necessary packages use the **requirements.txt** file provided
in this repository in a separate Python environment, i.e. using **conda** or **venv**.

Black was used for code reformatting.

```bash
pip install -r requirements.txt
```
___

# Quickstart
## Running the app
To run the app, first run the models.py directly to create the database, which you only need to do once (unless changes were made to the models).
```bash
python src/models.py
```
After that, please run this command to run the Flask application.
```bash
python src/app.py
```
___
# Testing
This project makes use of the **unittest** test framework for unittests that can be found in the directory *src/test*
___

# Acknowledgements
The Flask and Flask_SQLAlchemy infrastructure was inspired by the following GitHub template: https://github.com/jennielees/flask-sqlalchemy-example 
as well as the help of geeksforgeeks https://www.geeksforgeeks.org/python-program-to-check-if-number-is-palindrome-one-liner/.

ChatGPT was used to do some refactoring of the code.
___