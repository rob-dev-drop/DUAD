CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Correccion solicitada: corregi los INT por INTEGER y agregue la clausula AUTOINCREMENT para garantizar ids unicos
    code VARCHAR(10) NOT NULL,
    name TEXT,
    price REAL NOT NULL,
    entry_date date,
    brand TEXT,
    stock_available int NOT NULL
);

CREATE TABLE Order_Details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INT NOT NULL,
    invoice_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount decimal,
    FOREIGN KEY (product_id) REFERENCES Products(id),
    FOREIGN KEY (invoice_id) REFERENCES Invoices(id)
);

CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number varchar(20),
    purchase_date date,
    buyer_email text,
    total_amount REAL
);

CREATE TABLE Cart_Items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id int,
    quantity int,
    FOREIGN KEY (product_id) REFERENCES Products(id)
);

CREATE TABLE Shopping_Cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    products int,
    buyer_email TEXT
);


ALTER TABLE Invoices 
    ADD phone_number VARCHAR(8);

ALTER TABLE Invoices 
    ADD cashier_id int;


INSERT INTO Products (ID, code, name, price, entry_date, brand, stock_available)
    VALUES (1, 'A112', 'Router', 30000, '08-11-2017', 'NXXT', 240),
    (2, 'B201', 'Switch 24 Port', 45000, '10-12-2018', 'Cisco', 100),
    (3, 'C302', 'Access Point Pro', 15000, '15-01-2019', 'Ubiquiti', 50),
    (4, 'D403', 'Fiber Modem', 22000, '20-03-2018', 'Huawei', 80),
    (5, 'E504', 'Cat6 Cable 100m', 5000, '01-05-2020', 'Nexans', 500),
    (6, 'F605', 'Patch Cord 3m', 500, '10-06-2020', 'Generic', 1000),
    (7, 'G706', 'Firewall FortiGate', 80000, '12-07-2019', 'Fortinet', 30),
    (8, 'H807', 'Rack Server', 150000, '05-08-2018', 'Dell', 10),
    (9, 'I908', 'NAS Storage', 60000, '20-09-2020', 'Synology', 20),
    (10, 'J009', 'Ethernet Hub', 3000, '15-10-2017', 'TP-Link', 200);

INSERT INTO Invoices (id, invoice_number, purchase_date, buyer_email, total_amount, phone_number, cashier_id)
    VALUES (1, 1001, '08-03-2026', 'juan@gmail.com', 210000,89787123,3022),
    (2, 1002, '09-03-2026', 'maria_garcia@outlook.com', 150000, 98765432, 3025),
    (3, 1003, '10-03-2026', 'pedro_tech@gmail.com', 45000, 87654321, 3022),
    (4, 1004, '11-03-2026', 'ana_sol@yahoo.com', 120000, 99887766, 3028),
    (5, 1005, '12-03-2026', 'carlos_r@gmail.com', 30000, 88776655, 3025),
    (6, 1006, '13-03-2026', 'lucia_m@hotmail.com', 250000, 77665544, 3030),
    (7, 1007, '14-03-2026', 'roberto_v@gmail.com', 80000, 66554433, 3022),
    (8, 1008, '15-03-2026', 'elena_p@outlook.com', 10000, 55443322, 3028),
    (9, 1009, '16-03-2026', 'm_gonzalez@gmail.com', 50000, 44332211, 3030),
    (10, 1010, '17-03-2026', 'santiago_f@yahoo.com', 90000, 33221100, 3025);

INSERT INTO Order_Details (id, product_id,invoice_id,quantity,total_amount)
    VALUES(1, 5, 2, 30, 150000), -- 30 cables
        (2, 1, 1, 1, 30000),    -- 1 router
        (3, 2, 2, 2, 90000),    -- 2 switches
        (4, 3, 3, 3, 45000),    -- 3 access points
        (5, 4, 4, 5, 110000),   -- 5 modems
        (6, 7, 6, 1, 80000),    -- 1 firewall
        (7, 8, 7, 1, 150000),   -- 1 server
        (8, 9, 8, 2, 120000),   -- 2 NAS Storage drives
        (9, 10, 9, 10, 30000),  -- 10 hubs
        (10, 6, 10, 100, 50000),-- 100 patch cords
        (11, 2, 1, 1, 45000),   -- +1 switch on invoice 1
        (12, 3, 2, 5, 75000),   -- access points for invoice 2
        (13, 5, 3, 10, 50000),  -- cables for invocie 3
        (14, 8, 4, 1, 150000),  -- server for invoice 4
        (15, 1, 5, 2, 60000);   -- 2 routers for invoice 5


-- Obtenga todos los productos almacenados 
SELECT name from Products;

-- Obtenga todos los productos que tengan un precio mayor a 50000
SELECT name from Products where price > 50000;

-- Obtenga todas las compras de un mismo producto por id. 
SELECT * from Order_Details where product_id = 2;

-- Obtenga todas las compras agrupadas por producto, donde se muestre el total comprado entre todas las compras.
SELECT product_id, sum(quantity) as cantidad_vendida, sum(total_amount) as total_vendido from Order_Details group by product_id
-- Aprendi que se puede usar AS para nombrar columnas como las que implican sumas o totales que no son columnas propias de la tabla

-- Obtenga todas las facturas realizadas por el mismo comprador
SELECT * FROM Invoices where buyer_email = 'juan@gmail.com';

-- Obtenga todas las facturas ordenadas por monto total de forma descendente
SELECT * from Invoices ORDER BY total_amount DESC;

-- Obtenga una sola factura por número de factura.
Select * from Invoices where invoice_number = 1008;