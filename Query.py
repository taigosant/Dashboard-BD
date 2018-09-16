

class Query(object):
    CREATE_DATABASE_SCHEMA = """
    drop table if exists review;
    drop table if exists categoriesbyproduct;
    drop table if exists similarbyproduct;
    drop table if exists category;
    drop table if exists costumer;
    drop table if exists product;
    drop table if exists groupproducts;
    
    CREATE TABLE Product
(
    ID_Product INTEGER PRIMARY KEY,
    ASIN TEXT NOT NULL,
    Salesrank INTEGER,
    title TEXT,
    groupId INTEGER,
    UNIQUE(ASIN)
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
);

CREATE TABLE Review(
    ID_Review SERIAL PRIMARY KEY,
    R_Date DATE,
    Votes INTEGER, 
    Rating INTEGER,
    Helpful INTEGER,
    Prod_Id INTEGER, 
    ID_Costumer TEXT
);
CREATE TABLE CategoriesByProduct(
  ID_CategoriesByProduct SERIAL PRIMARY KEY ,
  ID_Prod Integer,
  ID_Cat Integer
);
    """

    A_QUERY = """
        (select * 
        from review natural join product  
        where asin = '{asin}' order by rating desc, helpful desc limit 5) 
        union all 
        (select * 
        from review natural join product 
        where asin = '{asin1}' order by rating, helpful desc limit 5);
    """

    B_QUERY = """
    select  p2.id_product, p2.asin, p2.title, p2.salesrank 
    from product p, similarbyproduct, product p2 
    where p.asin = asin_product and p2.asin = asin_productsimilar and p.salesrank <= p2.salesrank and p2.salesrank > 0 and p.asin='{ASIN}';
    """
    C_QUERY = """
    select r_date, avg(rating) from product join review r on prod_id = id_product where asin ='{asin}' group by r_date order by r_date;
    """

    D_QUERY = """
    SELECT *  FROM (
        SELECT *, 
        rank() OVER (
            PARTITION BY id_group
            ORDER BY salesrank ASC
        )
        FROM (select * from groupproducts join product p on p.groupid = groupproducts.id_group where p.salesrank > 0) as subaux
    ) rank_filter where rank <= 10;
    """

    E_QUERY = """
    select title, avg(rating) as rating_avg, avg(helpful) as helpful_avg 
    from review join product p on prod_id = p.id_product
    group by p.id_product, p.title order by rating_avg desc, helpful_avg desc limit 10
    """

    F_QUERY = """
        SELECT title, AVG(helpful) as AVG_helpful
        FROM (category JOIN (
	          categoriesbyproduct JOIN 
	            (SELECT prod_id,helpful from review) AS produto_avaliacoes on id_prod = prod_id
	            ) as seila on id_category = id_cat
              ) AS avaliacoes_categoria
        GROUP BY title
        ORDER BY AVG_helpful DESC LIMIT 5;
    """

    G_QUERY = """
        SELECT *  FROM (
        SELECT *, 
        rank() OVER (
            PARTITION BY id_group
            ORDER BY c DESC
        )
        FROM (  select groupproducts.title, id_costumer,id_group, count(*) as c from product
        join review on prod_id = id_product
        join groupproducts on groupid = id_group
        natural join costumer
        group by id_costumer, id_group
        order by c desc) as did
    ) rank_filter
    natural join costumer
    where rank <= 10
    order by id_group, rank;

    """
    REMOVE_SIMILAR_INCONSISTENCES= """
        delete from similarbyproduct where id_similarbyproduct 
        in (select id_similarbyproduct from product p1 join similarbyproduct on p1.asin = asin_product left join product p2 on p2.asin = asin_productsimilar where p2.asin is null);
    """
    ADD_PROD_GROUP_FK = """
        alter table product add constraint fk_prod_group foreign key(groupId) references GroupProducts(ID_Group);
    """

    ADD_SIMILAR_PROD_FKS = """
        alter table similarbyproduct add constraint fk_prod foreign key(asin_product) references product(asin), add constraint fk_sim_prod foreign key(asin_productsimilar) references product(asin);
    """

    ADD_REVIEW_COSTUMER_FK = """
        alter table review add constraint fk_costumer foreign key(id_costumer) references costumer(id_costumer);
    """

    ADD_CATEGORY_BY_PROD_FKS = """
        alter table categoriesbyproduct add constraint fk_prod foreign key(id_prod) references product(id_product), add constraint fk_cat foreign key(id_cat) references category(id_category);
    """
