#Objected Oriented Programming practice samples
class ShoppingCart(object):
    items_in_cart = {}
    def __init__(self,customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product]=price
            print product +""+ "Added"
        else:
            print product + "is already in the cart."
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + "removed."
        else:
            print product + "is not in the cart."

my_cart = ShoppingCart("Jeff")
my_cart.add_item("cold pizza",20)

#Class inheritance example
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
    def display_cart(self):
        print "Display contents of your cart"
class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "Im a string"

monty_python = ReturningCustomer("ID: 1235")
monty_python.display_cart()

class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name
class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
ceo.greet(emp)

class Employee(object):

    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

emp = PartTimeEmployee("Jeff")
print emp.calculate_wage(40)
