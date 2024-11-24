from app import db, app


class Palindrome(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.

    # We always need an id
    id = db.Column(db.Integer, primary_key=True)

    # A dessert has a name, a price and some calories:
    number = db.Column(db.Integer)
    result = db.Column(db.Float)
    num_cycles = db.Column(db.Integer)

    def __init__(self, number, result, num_cycles):
        self.number = number
        self.result = result
        self.num_cycles = num_cycles


def create_palindrome(new_number, new_result, new_num_cycles):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    palindrome = Palindrome(new_number, new_result, new_num_cycles)

    # Actually add this dessert to the database
    db.session.add(palindrome)

    # Save all pending changes to the database
    db.session.commit()

    return palindrome


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    with app.app_context():
        db.create_all()
    print("Done!")
