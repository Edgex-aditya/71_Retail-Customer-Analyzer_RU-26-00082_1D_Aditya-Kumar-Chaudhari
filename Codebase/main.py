import pandas as pd

df = pd.read_csv("customers.csv")
print(df)

total_spent = df["TotalSpent"]

mean_spend = total_spent.mean()
median_spend = total_spent.median()

highest = df.loc[total_spent.idxmax()]
lowest = df.loc[total_spent.idxmin()]
summary = df.groupby("City")["TotalSpent"].agg(
    Total="sum",
    Average="mean"
)

while True:
    print("\n===== RETAIL CUSTOMER ANALYZER =====")
    print("1. Spending Statistics")
    print("2. High-Value Customers")
    print("3. City-Wise Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Spending Statistics ---")
        print("Mean spend:", mean_spend)
        print("Median spend:", median_spend)
        print("Highest:", highest["Name"], highest["TotalSpent"])
        print("Lowest:", lowest["Name"], lowest["TotalSpent"])

    elif choice == "2":
        try:
            limit = float(input("Enter spending limit: "))

            if limit < 0:
                print("Amount must be 0 or more.")
            else:
                result = df[df["TotalSpent"] >= limit]

                print("High-value customers:", len(result))
                print(result[["CustomerID", "Name", "City", "TotalSpent"]])

        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif choice == "3":
        print("\n--- City-Wise Summary ---")

        for city, row in summary.iterrows():
            print(
                f"{city}: Total Rs. {row['Total']:.2f} | "
                f"Average Rs. {row['Average']:.2f}"
            )

    elif choice == "4":
        print("Thank you for using Retail Customer Analyzer!")
        break

    else:
        print("Invalid choice. Please try again.")
