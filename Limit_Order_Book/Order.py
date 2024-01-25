class Order:
    def __init__(self, order_id: int, side: int, order_type: str, time_in_force: str, quantity: float, price: float,
                 time_stamp: int):
        """
        Initialises an instance of the Order class

        :param order_id: Uniquely generated ID for an order
        :param side: Denotes if order is a buy or sell order (1) for buy order and (-1) for sell order
        :param order_type: Denotes if an order is a limit or market order
        :param time_in_force: How long an order will be active for it is executed or expired
        :param quantity: The amount of the asset to be bought or sold
        :param price: The price to buy or sell an asset
        :param time_stamp: The time when the order was submitted
        """
        self.order_id = order_id
        self.side = side
        self.order_type = order_type
        self.time_in_force = time_in_force
        self.quantity = quantity
        self.price = price
        self.time_stamp = time_stamp

    def modify_order(self, order_id: int, new_quantity: float = None, new_price: float = None) -> bool:
        """
        Modifies Order by either changing the price or the quantity or both

        :param order_id: ID for the order being changed
        :param new_quantity: The amount of the asset to be bought or sold
        :param new_price: The price to buy or sell an asset
        :return: Boolean if successful/unsuccessful
        """

        try:
            if self.order_id != order_id:
                raise ValueError("Order ID is not the orders ID")

            if new_quantity is not None:
                    self.quantity = new_quantity
            if new_price is not None:
                    self.price = new_price

            return True

        except Exception as e:
            print("An error occurred: ", e)
            return False
