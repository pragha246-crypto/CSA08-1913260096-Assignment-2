"""Q5: Mutable default argument bug, parameter styles, return values and scope."""
PRICE = {"Tea": 10, "Vada": 12, "Dosa": 40, "Coffee": 15, "Samosa": 8}
orders_today = 0

def add_item_buggy(item, order=[]):
    order.append(item)
    return order

def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order

def price_of(item, qty=1):
    return PRICE[item] * qty

def bill(order, gst_rate=0.05):
    subtotal = sum(PRICE[item] for item in order)
    gst = subtotal * gst_rate
    return subtotal, gst, subtotal + gst

def local_demo():
    orders_today = 100
    return orders_today

def global_update():
    global orders_today
    orders_today += 1
    return orders_today

def make_token_counter():
    token = 0
    def next_token():
        nonlocal token
        token += 1
        return token
    return next_token

def main():
    print("Q5 - Functions, Parameters and Scope")
    buggy = add_item_buggy("Tea")
    print("buggy calls:", buggy, add_item_buggy("Vada"))
    print("buggy shared object:", add_item_buggy.__defaults__[0])
    first = add_item("Tea")
    second = add_item("Vada")
    print("correct independent lists:", first, second, first is second)
    print("price positional / keyword:", price_of("Vada", 3), price_of(qty=3, item="Vada"))
    print("bill tuple:", bill(["Tea", "Vada"]))
    print("local vs global:", local_demo(), orders_today, global_update(), global_update())
    counter = make_token_counter()
    print("nonlocal tokens:", counter(), counter(), counter())

if __name__ == "__main__":
    main()
