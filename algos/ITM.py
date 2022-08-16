def models_itm(option_type, stock_price, strike_price):
    error_message = 'An Error has occurred with the ITM Algorithm.'
    if option_type is None or stock_price is None or strike_price is None:
        return error_message

    option_types = {
        'LC': 'Long Call',
        'LP': 'Long Put',
        'SC': 'Short Call',
        'SP': 'Short Put'
    }

    option_result = {
        'IN': 'in-the-money',
        'OUT': 'out-of-the-money',
        'AT': 'at-the-money',
    }

    def get_result():
        if option_types[option_type] is None:
            return f'{error_message} the option type needs to be either LC || LP || SC || SP.'

        if option_type == 'LC':  # Long Call
            if stock_price > strike_price:
                return 'IN'
            if stock_price < strike_price:
                return 'OUT'
            if stock_price == strike_price:
                return 'AT'

        if option_type == 'LP':  # Long Put
            if stock_price > strike_price:
                return 'OUT'
            if stock_price < strike_price:
                return 'IN'
            if stock_price == strike_price:
                return 'AT'

        if option_type == 'SC':  # Short Call
            if stock_price > strike_price:
                return 'OUT'
            if stock_price < strike_price:
                return 'IN'
            if stock_price == strike_price:
                return 'AT'

        if option_type == 'SP':  # Short Put
            if stock_price > strike_price:
                return 'IN'
            if stock_price < strike_price:
                return 'OUT'
            if stock_price == strike_price:
                return 'AT'

    prefix = f'The {option_types[option_type]} option is'
    result = option_result[get_result()]

    return f'{prefix} {result}'
