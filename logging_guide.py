import logging

# Use logging to see what is going on with your code

logging.basicConfig(filename="trial.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
#logging.basicConfig(level=logging.INFO)
log_check = logging.getLogger(__name__)
# Levels:NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
# can only see log of levels after level will be logged.
# creating a file which logs, everything
# Use format to write what we want to save and how.


# create a handler to add logs to a file
#handler = logging.FileHandler("Testing.log")
#handler.setLevel(logging.INFO)
# Can change the format of the file
#format_test = handler.formatter("%(asctime)s:%(levelname)s:%(message)s")
#handler.setFormatter(format_test)
# need to add this handle to the lof file log_check
#log_check.addHandler(handler)



class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        log_check.info("Pizza created: {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        log_check.debug("Made {} {} pizza(s)".format(quantity, self.name))


pizza_01 = Pizza("artichoke", 15)
pizza_01.make()

pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
