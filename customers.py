"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
    
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def __repr__(self):
        return (f"Name:{self.first_name} {self.last_name}, email: {self.email}, password: {self.password}")
    # TODO: need to implement this 
    
    def get_by_email(self, email):
        return email

