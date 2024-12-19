from collections import namedtuple

from uniswap_v2_pool_singleton import CreatePoolSingelton
from uniswap_v2_utils import usdc_decimal_amount_to_token_count, eth_decimal_amount_to_token_count

EventData = namedtuple("EventData", ["swapped_eth", "swapped_usdc", "sender_address"])


def _events_info(events, usdc_token_index, eth_token_index):
    for event in events:
        usdc_amount_in = event['args'][f'amount{usdc_token_index}In']
        usdc_amount_out = event['args'][f'amount{usdc_token_index}Out']
        eth_amount_in = event['args'][f'amount{eth_token_index}In']
        eth_amount_out = event['args'][f'amount{eth_token_index}Out']
        swapped_amount_usdc = usdc_amount_in if usdc_amount_in > 0 else usdc_amount_out
        swapped_amount_eth = eth_amount_in if eth_amount_in > 0 else eth_amount_out
        yield EventData(eth_decimal_amount_to_token_count(swapped_amount_eth),
                        usdc_decimal_amount_to_token_count(swapped_amount_usdc), event['args']['sender'])


def main():
    pool = CreatePoolSingelton()
    # Get reserves and price
    reserves = pool.contract.functions.getReserves().call()
    reserve_usdc = usdc_decimal_amount_to_token_count(reserves[pool.usdc_token_index])
    reserve_eth = eth_decimal_amount_to_token_count(reserves[pool.eth_token_index])
    eth_price = (reserve_usdc / reserve_eth)
    print(f"Reserves: {reserve_usdc} USDC, {reserve_eth} ETH ")
    print(f"1 ETH = {eth_price} USDC")

    # Get latest events data
    HISTORY_WINDOW_SIZE = 100  # TODO: should this be a flag,
    swap_events = pool.contract.events.Swap.create_filter(from_block=pool.latest_block_number - HISTORY_WINDOW_SIZE,
                                                               to_block='latest').get_all_entries()
    swap_events_info = list(_events_info(swap_events, pool.usdc_token_index, pool.eth_token_index))
    largest_swap = max(swap_events_info, key=lambda e: e.swapped_usdc)
    total_usdc = sum(e.swapped_usdc for e in swap_events_info)
    total_eth = sum(e.swapped_eth for e in swap_events_info)
    print(f"Total swapped: {total_usdc} USDC, {total_eth} ETH")
    print(f"Largest swap: a swap of {largest_swap.swapped_usdc}$ by {largest_swap.sender_address}")

if __name__ == "__main__":
  main()