-- Tabla original

CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin TEXT,
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

INSERT INTO vehicles (vin, make, model, year, color, owner_id, owner_name, owner_phone, insurance_company, insurance_policy) VALUES
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 101, 'Alice', '123-456-7890', 'ABC Insurance', 'Fire & Theft'),
('1HGCM82633A', 'Honda', 'Accord', 2003, 'Silver', 102, 'Bob', '987-654-3210', 'XYZ Insurance', 'Full Cover'),
('5J6RM4H79EL', 'Honda', 'CR-V', 2014, 'Blue', 103, 'Claire', '555-123-4567', 'DEF Insurance', 'Collision'),
('1G1RA6EH1FU', 'Chevrolet', 'Volt', 2015, 'Red', 104, 'Dave', '111-222-3333', 'GHI Insurance', 'Basic Legal');


-- Normalizacion


-- Creamos la tabla de owners para separar esos datos
Create TABLE Owners (
    id INTEGER,
    name TEXT,
    phone TEXT
);

-- Creamos la tabla de cars para no repetir autos 
CREATE TABLE Cars (
    vin TEXT,
    make TEXT,
    model TEXT,
    year INT,
    color TEXT
);



-- Tabla cruz para decir de quien es cada carro y enlazar aquellos que tienen mas de un propietario
CREATE TABLE Owned_cars (
    owner_id INT PRIMARY KEY,
    car_vin TEXT,
    FOREIGN KEY (owner_id) REFERENCES Owners(id),
    FOREIGN KEY (car_vin) REFERENCES Cars(car_vin)
);

-- Tabla para separar la informacion del seguro
CREATE TABLE Insurance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    policy TEXT,
    car_vin TEXT,
    FOREIGN KEY (car_vin) REFERENCES Cars(vin)
);

-- Insertamos la informacion correspondiente a cada tabla

INSERT into Owners (id,name,phone) VALUES
(101,'Alice','123-456-7890'),
(102,'Bob','987-654-3210'),
(103,'Claire','555-123-4567'),
(104,'Dave','111-222-3333');


INSERT INTO Cars (vin,make,model,year,color) VALUES
('1HGCM82633A','Honda','Accord',2003,'Silver'),
('5J6RM4H79EL','Honda','CR-V',2014,'Blue'),
('1G1RA6EH1FU','Chevrolet','Volt',2015,'Red');

INSERT INTO Owned_cars (owner_id,car_vin) VALUES
(101,'1HGCM82633A'),
(102,'1HGCM82633A'),
(103,'5J6RM4H79EL'),
(104,'1G1RA6EH1FU');

INSERT INTO Insurance (company,policy,car_vin) VALUES
('ABC Insurance','Fire & Theft','1HGCM82633A'),
('XYZ Insurance','Full Cover','1HGCM82633A'),
('DEF Insurance','Collision','5J6RM4H79EL'),
('GHI Insurance','Basic Legal','1G1RA6EH1FU');


-- Selects de prueba

-- Seleccionar todo de Cars
SELECT *
FROM Cars;


-- Mostar que modelo tiene cada Owner
SELECT 
    Owners.name as Owner,
    Cars.model as model
FROM 
    Owners
JOIN Owned_cars
    ON Owned_cars.owner_id = Owners.id
JOIN Cars
    ON Owned_cars.car_vin = Cars.vin;

