import csv  # Get Pythons toolbox to read csv files

total_revenue = 0  #starts our total at zero
products = {}  # empty dictionary
daily_revenue = {} # empty dictionary for tracking daily revenue

with open("sales_data.csv", "r")as file: # open file and "read"
    reader = csv.DictReader(file) # use column headings for info

    for row in reader: # go through sales, one at a time
        product = row["product"]
        date = row["date"] # get date of the sale

        if product not in products:
            products[product] = {"quantity": 0, "revenue": 0}

        quantity = int(row["quantity"]) # convert quantity to integer
        price = float(row["price"])  # get price and convert from string to decimal

        revenue = quantity * price
        total_revenue += revenue # add this amount to the total
        
        products[product]["quantity"] += quantity #find this box
        products[product]["revenue"] += revenue

        if date not in daily_revenue:
            daily_revenue[date] = 0

        daily_revenue[date] += revenue

        print(f"{row['product']}: ${revenue:.2f}")

print(f"Total revenue: ${total_revenue:,.2f}")
print(products)

print(daily_revenue)

best_day = None

for date in daily_revenue:
    if best_day is None or daily_revenue[date] > daily_revenue[best_day]:
        best_day = date

print(f"Highest revenue day: {best_day}")
print(f"Revenue that day: ${daily_revenue[best_day]:,.2f}")

with open("sales_report.txt", "w") as report:
    report.write("SALES REPORT\n")
    report.write("=============\n")
    report.write(f"Total revenue: ${total_revenue:,.2f}\n\n")

    for product, totals in products.items():
        report.write(f"Product: {product}\n")
        report.write(f"Quantity: {totals['quantity']}\n")
        report.write(f"Revenue: ${totals['revenue']:,.2f}\n\n")

    report.write(f"Highest revenue day: {best_day}\n")
    report.write(f"Revenue that day: ${daily_revenue[best_day]:,.2f}\n")

with open("product_summary.csv", "w", newline="") as file:
    writer = csv.DictWriter(  # writes dictionaries in CSV rows
        file,
        fieldnames=["product", "total_quantity", "total_revenue"] #labels column headers
    )

    writer.writeheader()

    for product, totals in products.items():
        writer.writerow({
            "product": product,
            "total_quantity": totals["quantity"],
            "total_revenue": f"{totals['revenue']:.2f}"
        })