from stockAPIGetter import stockAPIGetter
from stockCSVDownloader import stockCSVDownloader

"""
basically just starts the api getter, d'know was thinking i hated osterhout
"""
class programRunner:
    def __init__(self, count):
        self.count = count
        print("Program runner initialized")

    def run(self):
        getter = stockAPIGetter(count=self.count)
        getter.run()
