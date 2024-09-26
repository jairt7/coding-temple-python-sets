# 2. Set Operations in Data Analysis
# These aren't usually this easy

def duplicate_entries_cleanup(customer_ids):
    ids = set(customer_ids)
    print("Customer IDs:")
    print(sorted(ids))

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

duplicate_entries_cleanup(customer_ids)