# DukaanAI — Retail Store Inventory Data Dictionary

This document defines the fields present in `retail_store_inventory.csv`.

| Field Name | Data Type | Description |
|---|---|---|
| `Date` | Datetime / String | The date of the recorded inventory and sales transaction. |
| `Store ID` | String | Unique identifier for each retail store branch. |
| `Product ID` | String | Unique identifier for each product item. |
| `Category` | String | Product category (e.g., Groceries, Toys, Electronics, Furniture, Clothing). |
| `Region` | String | Geographic region of the store (North, South, East, West). |
| `Inventory Level` | Integer | Current stock units available in the store. |
| `Units Sold` | Integer | Total units sold on that specific date. |
| `Units Ordered` | Integer | Units ordered for replenishment on that date. |
| `Demand Forecast` | Float | Model-predicted or estimated demand (cleaned to $\ge 0$). |
| `Price` | Float | Selling price per unit of the product. |
| `Discount` | Integer / Float | Percentage or absolute discount applied on the product. |
| `Weather Condition` | String | Weather on that day (Sunny, Rainy, Cloudy, Snowy, etc.). |
| `Holiday/Promotion` | Integer | Binary flag indicating a holiday or active promotion (0 = No, 1 = Yes). |
| `Competitor Pricing` | Float | Average pricing of the same or similar product at competing stores. |
| `Seasonality` | String | Season associated with the date (Spring, Summer, Autumn, Winter). |