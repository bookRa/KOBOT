@dataclass
class YmlConfigParam(object):
    name: str
    type: str
    required: bool = False
    default: (str|float|bool) = None
    description: str

    def greet(self) -> str:
        return f" Parameter **{self.name}** is of type **{self.type}** and is **{self.default}**. {self.description}"

exchange	string		Enter your maker spot connector
market	string		Enter the token trading pair you would like to trade on [exchange]

exchange = YmlConfigParam(
    name='exchange',
    type='string',
    required=True,
    

bid_spread = YmlConfigParam(
    name='bid_spread',
    type='decimal',
    required=True,
    description='How far away from the mid price do you want to place the first bid order?'
)

ask_spread = YmlConfigParam(
    name='ask_spread',
    type='decimal',
    required=True,
    description='How far away from the mid price do you want to place the first ask order?'
)

minimum_spread = YmlConfigParam(
    name='minimum_spread',
    type='decimal',
    required=False,
    description='At what minimum spread should the bot automatically cancel orders?'
)

order_refresh_time = YmlConfigParam(
    name='order_refresh_time',
    type='float',
    required=True,
    description='How often do you want to cancel and replace bids and asks (in seconds)?'
)

order_amount	 = YmlConfigParam(
    name='order_amount',
    type='decimal',
    required=True,
    description='What is the amount of [base_asset] per order?'
)

bid_order_level_spreads = YmlConfigParam(
    name='bid_order_level_spreads',
    type='decimal',
    required=True,
    description='Enter the spreads (as percentage) for all bid spreads e.g 1,2,3,4 to represent 1%,2%,3%,4%. The number of levels set will be equal to minimum lengths of bid_order_level_spreads and bid_order_level_amounts'
)


ask_order_level_spreads = YmlConfigParam(
    name='ask_order_level_spreads',
    type='decimal',
    required=True,
    description='Enter the spreads (as percentage) for all ask spreads e.g 1,2,3,4 to represent 1%,2%,3%,4%. The number of levels set will be equal to minimum lengths of ask_order_level_spreads and ask_order_level_amounts'
)
bid_order_level_amounts = YmlConfigParam(
    name='bid_order_level_amounts',
    type='decimal',
    required=True,
    description='Enter the amount for all bid amounts. The number of levels set will be equal to the minimum length of bid_order_level_spreads and bid_order_level_amounts'
)

ask_order_level_amounts = YmlConfigParam(
    name='ask_order_level_amounts',
    type='decimal',
    required=True,
    description='Enter the amount for all ask amounts. The number of levels set will be equal to the minimum length of ask_order_level_spreads and ask_order_level_amounts'
)


























