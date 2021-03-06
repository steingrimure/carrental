from models.order import Order
import csv
ORDERNR = 0
LIST_OF_DATES = 1
SSN = 2
NAME = 3
CAR = 4
PRICE = 5
INSURANCE = 6
DISCOUNT = 7


class OrderRepo(object):
    def __init__(self):
        """Kallar í order_dict fallið og gefur self.__orders dictionary."""
        self.__orders = self.order_dict()

    def add_order(self, order_number, order):
        """Bætir við pöntun í dictionary sem unnið er með."""
        self.__orders[order_number] = order

    def remove_order(self, order_number):
        """Notar order_number sem key til að leita í dictionary með pöntunum,
         ef í dict, þá eyðir fallið þeirri pöntun."""
        for ordernr, _ in self.__orders.items():
            if ordernr == order_number:
                print(self.__orders[order_number])
                del self.__orders[order_number]
                return self.__orders
        return False

    def get_order(self, order_number):
        """Tekur við order_number og skilar pöntuninni sem passar
         við það númer"""
        order = self.__orders[order_number]
        return order

    def get_orders(self):
        """Skilar orders dictionary til vinnslu."""
        return self.__orders

    def save_new_orders(self):
        """Vistar upplýsingar úr dictionary í csv skrá sem heldur utan
         um upplýsingarnar."""
        orders_header = "order_number,duration,ssn,car_number,price,insurance,\
discount"
        with open("./data/orders.csv", "w", newline="",
                  encoding="utf-8") as orders_file:
            csv_writer = csv.writer(orders_file)
            csv_writer.writerow(orders_header.split(','))
            for _, info in self.__orders.items():
                order_string = info.__repr__().split(",")
                csv_writer.writerow(order_string)

    def order_dict(self):
        """Tekur við gögnum, upplýsingum um pantanir, úr orders.csv og les inn í
         dictionary. Þá er lykillinn pöntunarnúmerið og gildið er Orders
         klasinn með upplýsingunum."""
        order_dict = {}
        with open("./data/orders.csv", "r",
                  encoding="utf-8") as orders_file:
            csv_reader = csv.reader(orders_file)
            next(csv_reader)
            for order in csv_reader:
                order_class = Order(
                    order[ORDERNR],
                    order[LIST_OF_DATES],
                    order[SSN],
                    order[NAME],
                    order[CAR],
                    order[PRICE],
                    order[INSURANCE],
                    order[DISCOUNT])
                order_number = order[ORDERNR]
                order_dict[order_number] = order_class
        return order_dict
