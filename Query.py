

class Query(object):
    CREATE_DATABASE_SCHEMA = """
    drop table if exists review;
    drop table if exists categoriesbyproduct;
    drop table if exists similarbyproduct;
    drop table if exists groupproducts;
    drop table if exists category;
    drop table if exists product;
    drop table if exists costumer;
    
    CREATE TABLE Product
(
    ID_Product INTEGER PRIMARY KEY,
    ASIN TEXT NOT NULL,
    Salesrank INTEGER,
    title TEXT,
    groupId INTEGER
);

CREATE TABLE Category(
    ID_Category INTEGER,
    Title TEXT,
    PRIMARY KEY (ID_Category)
);

CREATE TABLE GroupProducts(
    ID_Group INTEGER NOT NULL,
    Title Text,
    PRIMARY KEY(ID_Group)
);

CREATE TABLE Costumer(
  ID_Costumer TEXT NOT NULL,
  PRIMARY KEY(ID_Costumer)
);

CREATE TABLE SimilarByProduct (
    ID_SimilarByProduct SERIAL PRIMARY KEY,
    ASIN_PRODUCT TEXT,
    ASIN_ProductSIMILAR TEXT
 -- FOREIGN KEY (ID_PRODUCT) references Product (ID_Product),
);

CREATE TABLE Review(
    ID_Review SERIAL PRIMARY KEY,
    R_Date DATE,
    Votes INTEGER, 
    Rating INTEGER,
    Helpful INTEGER,
    Prod_Id INTEGER, 
    ID_Costumer TEXT
--     FOREIGN KEY (ID_Costumer) references Costumer (ID_Costumer),
);
CREATE TABLE CategoriesByProduct(
  ID_CategoriesByProduct SERIAL PRIMARY KEY ,
  ID_Prod Integer,
  ID_Cat Integer
-- FOREIGN KEY (ID_Prod) REFERENCES Product (ID_Product),
-- FOREIGN KEY (ID_Cat) REFERENCES Category (ID_Category)
);
    """