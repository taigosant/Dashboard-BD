CREATE TABLE Product
(
    ID_Product INTEGER NOT NULL,
    ASIN TEXT NOT NULL,
    Salesrank INTEGER,
    AVG_Rating FLOAT,
    title TEXT,
    PRIMARY KEY (ID_Product)
);