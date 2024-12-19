def eth_decimal_amount_to_token_count(amount: int) -> float:
    """
    Converts an Ethereum amount represented in decimal to the equivalent token count.
    """
    return amount / pow(10, 18)


def usdc_decimal_amount_to_token_count(amount: int) -> float:
    """
     Converts a USDC amount represented in decimal to the equivalent token count
    """
    return amount / pow(10, 6)
