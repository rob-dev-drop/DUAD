-- Created original table

CREATE TABLE  orders (
    order_id INTEGER,
    customer_name TEXT,
    customer_phone TEXT,
    address TEXT,
    item_id INTEGER,
    item_name TEXT,
    price REAL,
    quantity INTEGER,
    special_request TEXT,
    delivery_time TEXT
);


INSERT INTO orders (order_id, customer_name, customer_phone, address, item_id, item_name, price, quantity, special_request, delivery_time) VALUES
(1, 'Alice', '123-456-7890', '123 Main St', 101, 'Cheeseburger', 8.0, 2, 'No onions', '6:00 PM'),
(1, 'Alice', '123-456-7890', '123 Main St', 102, 'Fries', 3.0, 1, 'Extra ketchup', '6:00 PM'),
(2, 'Bob', '987-654-3210', '456 Elm St', 103, 'Pizza', 12.0, 1, 'Extra cheese', '7:30 PM'),
(2, 'Bob', '987-654-3210', '456 Elm St', 102, 'Fries', 3.0, 2, 'None', '7:30 PM'),
(3, 'Claire', '555-123-4567', '789 Oak St', 105, 'Salad', 6.0, 1, 'No croutons', '12:00 PM'),
(4, 'Claire', '555-123-4567', '464 Georgia St', 106, 'Water', 1.0, 1, 'None', '5:00 PM');

-- To address 1NF (and 2NF at the same time): every record should have an unique PK. since we have multiple records with the same order ID and some data from the table depend on item_id, we need to normalize it into different tables.

-- First table: Customers: id, name, phone

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
);

INSERT INTO Customers (id, name, phone) VALUES
(1, 'Alice', '123-456-7890'),
(2, 'Bob', '987-654-3210'),
(3, 'Claire', '555-123-4567');


-- Second table: Address: id, address and customer_id

CREATE TABLE Addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

INSERT INTO Addresses (id, address, customer_id) VALUES
(1, '123 Main St', 1),
(2, '456 Elm St', 2),
(3, '789 Oak St', 3),
(4, '464 Georgia St', 3);

-- Third table: Products: id, name and price.

CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
);

INSERT INTO Products (id, name, price) VALUES
(101, 'Cheeseburger', 8.0),
(102, 'Fries', 3.0),
(103, 'Pizza', 12.0),
(105, 'Salad', 6.0),
(106, 'Water', 1.0);

-- Fourth table: Orders: id, customer_id, address_id, delivery_time.

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    address_id INTEGER,
    delivery_time TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id),
    FOREIGN KEY (address_id) REFERENCES Addresses(id)
);

INSERT INTO Orders (id, customer_id, address_id, delivery_time) VALUES
(1, 1, 1, '6:00 PM'),
(2, 2, 2, '7:30 PM'),
(3, 3, 3, '12:00 PM'),
(4, 3, 4, '5:00 PM');

-- After applying the 1NF (and fixing 2NF at the same time) these 4 tables now have their unique PK, however we need to go further to make this work
-- A fifth table need to be created to include prodcuts per order and special requests.
-- Order_items: id, order_id, product_id, quantity and special request

CREATE TABLE Order_Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    special_request TEXT,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
);


INSERT INTO Order_Items (id, order_id, product_id, quantity, special_request) VALUES
(1, 1, 101, 2, 'No onions'),
(2, 1, 102, 1, 'Extra ketchup'),
(3, 2, 103, 1, 'Extra cheese'),
(4, 2, 102, 2, 'None'),
(5, 3, 105, 1, 'No croutons'),
(6, 4, 106, 1, 'None');

-- Since we are already spliting this into their own tables, it automatically addresses 2NF since there wont be parcial dependencies.



-- The tables would comply as well with 3FN since there is no redundancy nor transitive dependencies.
