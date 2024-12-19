# Uniswap V2 Liquidity Pool Interaction

This project involves interacting with a Uniswap V2 liquidity pool (USDC/ETH Pair) to fetch and analyze data using Ethereum blockchain. The tasks include retrieving current reserves, token addresses, calculating price ratios, and analyzing swap events from the last 100 blocks.

## Prerequisites
Python version 3.8 or higher.

## How to run
Open a terminal in the project's directory.

Run 
```
pip install -r requirements.txt
python -m print_pool_info_main
```


## Output Format

The script outputs several key pieces of information related to the Uniswap V2 USDC/ETH pair at pool 0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc. 

### 1. Current Reserves
- **Description**: Displays the current amount of USDC and ETH held in the liquidity reserves of the USDC/ETH pair.
- **Format**: `Reserves: {USDC_amount} USDC, {ETH_amount} ETH`
- **Example**: `Reserves: 34,672,121.110025 USDC, 9646.2449416231 ETH`

### 2. Price of ETH in USDC
- **Description**: Shows the current market rate of 1 ETH expressed in USDC, based on the liquidity pool's reserves.
- **Format**: `1 ETH = {price} USDC`
- **Example**: `1 ETH = 3594.3645760451727 USDC`

### 3. Total Swap Volume Over the Last 100 Blocks
- **Description**: Summarizes the total volume of USDC and ETH that has been swapped in the last 100 blocks.
- **Format**: `Total swapped: {USDC_swapped} USDC, {ETH_swapped} ETH`
- **Example**: `Total swapped: 153,469.00347300002 USDC, 42.667389321321245 ETH`

### 4. Largest Swap Transaction
- **Description**: Identifies the largest swap transaction by value in USDC during the last 100 blocks and provides the Ethereum address of the transaction sender.
- **Format**: `Largest swap: a swap of ${value} by {address}`
- **Example**: `Largest swap: a swap of 25,000.0$ by 0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD`

These outputs provide a snapshot of current and recent activity in the Uniswap V2 USDC/ETH pool, enabling monitoring of liquidity, price movements, and trading volumes in real-time. This information is crucial for traders and analysts looking to make informed decisions.


### Condensed Example for output
Reserves: 34672121.110025 USDC, 9646.2449416231 ETH    \
1 ETH = 3594.3645760451727 USDC  \
Total swapped: 153469.00347300002 USDC, 42.667389321321245 ETH   \
Largest swap: a swap of 25000.0$ by 0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD