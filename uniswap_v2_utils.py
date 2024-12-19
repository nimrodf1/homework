def eth_decimal_amount_to_token_count(amount: int) -> float:
    return amount / pow(10, 18)


def usdc_decimal_amount_to_token_count(amount: int) -> float:
    return amount / pow(10, 6)
