-- Tabla original sin normalizacion

CREATE TABLE Original_Table (
    order_id TEXT,
    customer_name TEXT,
    phone TEXT,
    address TEXT,
    item_id INTEGER,
    item_name TEXT,
    price REAL,
    quantity INTEGER,
    special_request TEXT,
    delivery_time TEXT
);

INSERT INTO Original_Table (order_id, customer_name, phone, address, item_id, item_name, price, quantity, special_request, delivery_time) VALUES
('001', 'Alice', '123-456-7890', '123 Main St', 101, 'Cheeseburger', 8.0, 2, 'No onions', '6:00 PM'),
('001', 'Alice', '123-456-7890', '123 Main St', 102, 'Fries', 3.0, 1, 'Extra ketchup', '6:00 PM'),
('002', 'Bob', '987-654-3210', '456 Elm St', 103, 'Pizza', 12.0, 1, 'Extra cheese', '7:30 PM'),
('002', 'Bob', '987-654-3210', '4th Avenue', 102, 'Fries', 3.0, 2, 'None', '7:30 PM'),
('003', 'Claire', '555-123-4567', '789 Oak St', 105, 'Salad', 6.0, 1, 'No croutons', '12:00 PM'),
('004', 'Claire', '555-123-4567', '464 Georgia St', 106, 'Water', 1.0, 1, 'None', '5:00 PM');



--Normalizacion:


-- Al mover la informacion de los clientes a otra tabla, eso nos 'quita' 3 columnas de la tabla original
CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
);


-- Como hay customers con diferentes addresses, hay otra tabla para eso
CREATE TABLE Customer_addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INT,
    address TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

--Movi la informacion de Items a otra tabla y quite otras 3 columnas de la tabla original
CREATE TABLE Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
);

--Cree esta tabla cruz para relacionar items y orders, puse el special request aqui porque es por orden
CREATE TABLE Order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT,
    item_id INT,
    special_request TEXT,
    FOREIGN KEY (item_id) REFERENCES Items(id),
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);

--Esta tabla conecta el delivery con el customer
CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INT,
    delivery_time TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
);

--Datos para rellenar estas tablas

INSERT INTO Customers (name,phone) 
VALUES ('Alice','123-456-7890'),
    ('Bob','987-654-3210'),
    ('Claire','555-123-4567');


INSERT Into Customer_addresses (customer_id,address) VALUES
(1, '123 Main St'),
(2,'456 Elm St'),
(2,'4th Avenue'),
(3,'789 Oak St'),
(3,'464 Georgia St');

INSERT Into Items (name,price) VALUES
('Cheeseburger',8),
('Fries',3),
('Pizza',12),
('Salad',6),
('Water',1);

INSERT into Orders (customer_id,delivery_time) VALUES
(1, '6:00 PM'),
(2, '7:30 PM'),
(3, '12:00 PM'),
(3, '5:00 PM');

INSERT into Order_items (order_id,item_id,special_request) VALUES
(1,1,'No onions'),
(1,2,'Extra ketchup'),
(2,3,'Extra cheese'),
(2,2,'None'),
(3,4,'No croutons'),
(4,5,'None');

-- Algunos select para probar esta nueva estrctura

-- Seleccionar todo de Customers
SELECT *
FROM Customers;

-- Selecionar nombres de Customers

Select name
FROM Customers;

-- Ver los addresses con los nombres de los customers
Select 
    Customers.name,
    Customer_addresses.address
from Customers
JOIN Customer_addresses ON Customers.id = Customer_addresses.customer_id;

-- Ver una orden especifica

Select
    name,
    price
from Order_items
join items on Order_items.item_id = items.id
where Order_items.order_id = 1; -- Orden de Alice

--Ver que ordeno cada cliente y su precio
Select
    Orders.id as Order_Id,
    Customers.name as Customer_Name,
    Items.name as Item,
    Items.price as Price 
FROM Orders
JOIN Customers
    ON Orders.customer_id = Customers.id
JOIN Order_items
    ON Orders.id = Order_items.order_id
JOIN Items
    ON Order_items.item_id = Items.id;


-- Ver el total de cada orden y de quien
SELECT
    Orders.id as Order_ID,
    Customers.name as Customer,
    sum(Items.price) as Price
FROM Orders
Join Order_items
    ON Orders.id = Order_items.order_id
Join Items
    ON Order_items.item_id = Items.id
Join Customers
    On Orders.customer_id = Customers.id
Group by Orders.id;

