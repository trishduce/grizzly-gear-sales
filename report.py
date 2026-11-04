# Grizzly Gear - Simple Sales Report
# Reads sales.csv and prints total revenue and revenue by region.

def load_sales(filename):
    sales = []
    file = open(filename, "r")
    file.readline()  # skip the header row
    for line in file:
        date, region, product, units, price = line.strip().split(",")
        sale = {"region": region, "product": product,
                "units": int(units), "price": float(price)}
        sales.append(sale)
    file.close()
    return sales

def total_revenue(sales):
    total = 0
    for sale in sales:
        total = total + sale["units"] * sale["price"]
    return total

def revenue_by_region(sales):
    totals = {}
    for sale in sales:
        region = sale["region"]
        revenue = sale["units"] * sale["price"]
        if region in totals:
            totals[region] = totals[region] + revenue
        else:
            totals[region] = revenue
    return totals

sales = load_sales("sales.csv")
print("=== Grizzly Gear Sales Report ===")
print("Total revenue: $" + format(total_revenue(sales), ",.2f"))
print()
print("Revenue by region:")
for region, amount in revenue_by_region(sales).items():
    print("  " + region + ": $" + format(amount, ",.2f"))
