# Uniswap V2 Liquidity Pool Interaction

This project involves interacting with a Uniswap V2 liquidity pool (USDC/ETH Pair) to fetch and analyze data using Ethereum blockchain. The tasks include retrieving current reserves, token addresses, calculating price ratios, and analyzing swap events from the last 100 blocks.

## Prerequisites
Python version 3.8 or higher.

## How to run
Run print_pool_info_main.

## Expected output format

Reserves: XXXX USDC, XXXX ETH  
Price: 1 ETH = XXXX USDC
Total Swapped: XXXX USDC, XXXX ETH  
Largest Swap: XXXX USDC (0xXXX)

### Example output
Reserves: 34672121.110025 USDC, 9646.2449416231 ETH 
1 ETH = 3594.3645760451727 USDC
Total swapped: 153469.00347300002 USDC, 42.667389321321245 ETH
Largest swap: a swap of 25000.0$ by 0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD