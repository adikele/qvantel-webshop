# Qvantel Webshop Assignment

This is a base for a programming assignment from Qvantel.

The following features mentioned in the assignment have been executed:

Webpage stores the following details of an item in the cart to a database:	
(i) Item ID
(ii) Item name 
(iii) Item price
(iv) Country name for VAT purposes 
(v) Item identifier, a combination of Item ID and Item name

additional details stored:
(i) Timestamp

# Active Paths: 
http://127.0.0.1:5000/item_details Link to the web page for storing details of an item

# Special Instructions for installation:
Create a database with the following name before running the program:
qvantel

# APIs:
GET http://127.0.0.1:5000/get_item_by_identifier_API

Query Parameters
Parameter: identifier
Type: string
Default: n/a
Description: Identifies a uniques item saved in the database

Example query
http://127.0.0.1:5000/get_item_by_identifier_API?identifier=11a

