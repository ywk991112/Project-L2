# Class name must be Strategy
class Strategy():
    # option setting needed
    def __setitem__(self, key, value):
        self.options[key] = value

    # option setting needed
    def __getitem__(self, key):
        return self.options.get(key, '')

    def __init__(self):
        # strategy property needed
        self.subscribedBooks = {
            'Binance': {
                'pairs': ['BTC-USDT'],
            },
        }
        self.period = 10 * 60
        self.options = {}

        # user defined class attribute
        self.buy = 0 


    # called every self.period
    def trade(self, information):
        # for single pair strategy, user can choose which exchange/pair to use when launch, get current exchange/pair from information
        exchange = list(information['candles'])[0]
        pair = list(information['candles'][exchange])[0]
        if self.buy == 0:
            self.buy == 1 
            return [
                {
                    'exchange': exchange,
                    'amount': 1,
                    'price': -1,
                    'type': 'MARKET',
                    'pair': pair,
                },
            ]
        return []
       
    def on_order_state_change(self, order):
        Log("on order state change message: " + str(order) + " order price: " + str(order["price"]))
