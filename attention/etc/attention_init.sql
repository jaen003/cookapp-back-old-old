CREATE DATABASE IF NOT EXISTS cookapp_attention;

USE cookapp_attention;

CREATE TABLE Food_Order_Item (
	ord_item_id          VARCHAR( 40 ) NOT NULL,
	ord_item_price       INT UNSIGNED NOT NULL,
    ord_item_start_date  DATETIME NOT NULL,
    ord_item_end_date    DATETIME DEFAULT NULL,
    ord_item_amount      TINYINT UNSIGNED NOT NULL,
    ord_item_description VARCHAR( 200 ) NOT NULL,
	ord_item_status      TINYINT UNSIGNED NOT NULL,
    prod_id              VARCHAR( 40 ) NOT NULL,
	ord_id               VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( ord_item_id )
);

CREATE TABLE Product (
	prod_id          VARCHAR( 40 ) NOT NULL,
	prod_name        VARCHAR(40) NOT NULL,
	prod_price       INT UNSIGNED NOT NULL,
	prod_description VARCHAR( 40 ) NOT NULL,
	prod_status      TINYINT UNSIGNED NOT NULL,
	rest_id          VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( prod_id )
);

CREATE TABLE Food_Order (
	ord_id     VARCHAR( 40 ) NOT NULL,
	ord_price  INT UNSIGNED NOT NULL,
	ord_status TINYINT UNSIGNED NOT NULL,
	tab_id     VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( ord_id )
);

CREATE TABLE Dining_Table (
	tab_id     VARCHAR( 40 ) NOT NULL,
	tab_number TINYINT UNSIGNED NOT NULL,
	tab_status TINYINT UNSIGNED NOT NULL,
	rest_id    VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( tab_id )
);

ALTER TABLE Food_Order      ADD CONSTRAINT FK_Order_Table FOREIGN KEY ( tab_id ) REFERENCES Dining_Table( tab_id );
ALTER TABLE Food_Order_Item ADD CONSTRAINT FK_Order_Order_Item FOREIGN KEY ( ord_id ) REFERENCES Food_Order( ord_id );
ALTER TABLE Food_Order_Item ADD CONSTRAINT FK_Order_Product FOREIGN KEY ( prod_id ) REFERENCES Product( prod_id );