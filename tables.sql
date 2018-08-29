CREATE TABLE Product
(
    ID_Product INTEGER NOT NULL,
    ASIN TEXT NOT NULL,
    Salesrank INTEGER,
    AVG_Rating FLOAT,
    title TEXT,
    PRIMARY KEY (ID_Product)
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
  ID_Costumer INTEGER NOT NULL,
  PRIMARY KEY(ID_Costumer)
);
CREATE TABLE SimilarByProduct (
    ID_SimilarByProduct INTEGER NOT NULL,
    ID_PRODUCT INTEGER ,
    ID_ProductSIMILAR INTEGER,
    FOREIGN KEY (ID_PRODUCT) references Product (ID_Product),
    PRIMARY KEY(ID_SimilarByProduct)
);
