-- Crear la tabla original

CREATE TABLE vehicles (
    vin TEXT ,
    make TEXT,
    model TEXT,
    year INTEGER,
    color TEXT,
    owner_id INTEGER,
    owner_name TEXT,
    owner_phone TEXT,
    insurance_company TEXT,
    insurance_policy TEXT
);

INSERT INTO vehicles (vin, make, model, year, color, owner_id, owner_name, owner_phone, insurance_company, insurance_policy) 
VALUES 
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 101, 'Alice', '123-456-7890', 'ABC Insurance', 'Fire & Theft'),
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 102, 'Bob', '987-654-3210', 'XYZ Insurance', 'Full Cover'),
('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue', 103, 'Claire', '555-123-4567', 'DEF Insurance', 'Collision'),
('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red', 104, 'Dave', '111-222-3333', 'GHI Insurance', 'Basic Legal');


-- Check for 1NF: Unique PK is not present for each record. We need to separate cars, owners, insurance companies and insurance policies in their own tables.

Create table Cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin TEXT,
    make TEXT,
    model TEXT,
    year int,
    color TEXT
);

create table Owners (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
);

create table Insurance_companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT
);


create table Insurance_policies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_name TEXT
);

-- This way we have successfully addressed 1NF and 2NF since there is no partial dependencies on each table. 

-- We need to create a couple of tables to correctly "link" all the data


create table car_oweners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INT,
    car_id INT,
    FOREIGN KEY (owner_id) REFERENCES Owners(id),
    FOREIGN KEY (car_id) REFERENCES Cars(id)
);

create table car_insurance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    insurance_company_id INT,
    insurance_policy_id INT,
    car_id INT,
    FOREIGN KEY (car_id) REFERENCES Cars(id),
    FOREIGN KEY (insurance_company_id) REFERENCES Insurance_companies(id),
    FOREIGN KEY (insurance_policy_id) REFERENCES Insurance_policies(id)
);



-- With this 1NF and 2NF are complete covered and functional. 

-- To address 3NF we need to look at the new table cars, specifically make and model, since it is still redundant that we have repeated information across these columns.

-- We need to create a table for car_models

create table Car_models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make text,
    model text
);

--At the same time, we need to correct the Cars table to exclude these extracted columns and include a model_id
drop table Cars;

Create table Cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin TEXT,
    model_id INTEGER,
    year INTEGER,
    color TEXT,
    FOREIGN KEY (model_id) REFERENCES Car_models(id)
);

--Successfully applying 3NF


-- Adding information to the tables: 

INSERT INTO Owners (id, name, phone) VALUES
(101, 'Alice', '123-456-7890'),
(102, 'Bob', '987-654-3210'),
(103, 'Claire', '555-123-4567'),
(104, 'Dave', '111-222-3333');

INSERT INTO Insurance_companies (company_name) VALUES
('ABC Insurance'),
('XYZ Insurance'),
('DEF Insurance'),
('GHI Insurance');

INSERT INTO Insurance_policies (policy_name) VALUES
('Fire & Theft'),
('Full Cover'),
('Collision'),
('Basic Legal');

INSERT INTO Car_models (make, model) VALUES
('Honda', 'Accord'),
('Honda', 'CR-V'),
('Chevrolet', 'Volt');

INSERT INTO Cars (vin, model_id, year, color) VALUES
('1HGCM82633A', 1, 2003, 'Silver'),
('5J6RM4H79EL', 2, 2014, 'Blue'),
('1G1RA6EH1FU', 3, 2015, 'Red');

INSERT INTO car_oweners (owner_id, car_id) VALUES
(101, 1),
(102, 1),
(103, 2),
(104, 3);

INSERT INTO car_insurance 
(insurance_company_id, insurance_policy_id, car_id) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 3);

