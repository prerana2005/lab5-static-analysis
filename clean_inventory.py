"""
Inventory Management System - Clean Version
Implements safe, readable, and secure operations for managing stock data.
"""

import json
from datetime import datetime


def add_item(stock_data, item="default", qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid input. Item must be string and qty must be number.")
        return stock_data, logs

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return stock_data, logs


def remove_item(stock_data, item, qty):
    """Remove a specific quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")
    except TypeError:
        print("Invalid quantity type.")
    return stock_data


def get_qty(stock_data, item):
    """Get the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_name="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Starting with an empty inventory.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format. Starting fresh.")
        return {}


def save_data(stock_data, file_name="inventory.json"):
    """Save stock data to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=4)


def print_data(stock_data):
    """Print a formatted report of all items and their quantities."""
    print("Items Report:")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items that are below the threshold quantity."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution function for inventory management."""
    stock_data = {}
    logs = []

    stock_data, logs = add_item(stock_data, "apple", 10, logs)
    stock_data, logs = add_item(stock_data, "banana", 3, logs)
    stock_data, logs = add_item(stock_data, "orange", 0, logs)

    stock_data = remove_item(stock_data, "apple", 3)
    stock_data = remove_item(stock_data, "grape", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")

    save_data(stock_data)
    loaded_data = load_data()
    print_data(loaded_data)


if __name__ == "__main__":
    main()
