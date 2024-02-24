# stocks.csv contains stock price, earnings per share and book value.
# You are writing a stock market application that will process this file and create a
# new file with financial metrics such as pe ratio and price to book ratio.

# These are calculated as,
# pe ratio = price / earnings per-share
# price to book ratio = price / book value


# Your input format (stocks.csv) is,
# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572


# Output.csv should look like this,
# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68

with open("stocks.csv", "r") as f1:
    with open("new-stock.csv", "w") as f2:
        f2.write("Company Name, PE Ratio, PB Ratio\n")
        f1.readline()
        for entry in f1:
            line = entry.split(",")
            name = line[0]
            price = float(line[1])
            eps = float(line[2])
            bv = float(line[3])
            f2.write(f"{name}, {price/eps}, {price/bv}\n")
