CREATE DATABASE IF NOT EXISTS cookapp_backoffice;

USE cookapp_backoffice;

DROP TABLE IF EXISTS Product;

CREATE TABLE Product (
	prod_id VARCHAR( 40 ) NOT NULL,
	prod_name VARCHAR(40) NOT NULL,
	prod_price INT UNSIGNED NOT NULL,
	prod_description VARCHAR( 40 ) NOT NULL,
	prod_status TINYINT UNSIGNED NOT NULL,
	rest_id VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( prod_id )
);

DROP TABLE IF EXISTS Restaurant;

CREATE TABLE Restaurant (
	rest_id VARCHAR( 40 ) NOT NULL,
	rest_name VARCHAR( 40 ) DEFAULT NULL,
	rest_status TINYINT UNSIGNED NOT NULL,
	PRIMARY KEY( rest_id )
);

DROP TABLE IF EXISTS User;

CREATE TABLE User (
	user_email VARCHAR( 60 ) NOT NULL,
	user_name VARCHAR( 40 ) NOT NULL,
	user_password VARCHAR( 150 ) NOT NULL,
	user_role TINYINT UNSIGNED NOT NULL,
	user_status TINYINT UNSIGNED NOT NULL,
	rest_id VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( user_email )
);

CREATE TABLE Dining_Table (
	tab_id VARCHAR( 40 ) NOT NULL,
	tab_number TINYINT UNSIGNED NOT NULL,
	tab_description VARCHAR( 40 ) NOT NULL,
	tab_status TINYINT UNSIGNED NOT NULL,
	rest_id VARCHAR( 40 ) NOT NULL,
	PRIMARY KEY( tab_id )
);

ALTER TABLE Product ADD CONSTRAINT FK_Product_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );
ALTER TABLE User ADD CONSTRAINT FK_User_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );
ALTER TABLE Dining_Table ADD CONSTRAINT FK_Dining_Table_Restaurant FOREIGN KEY ( rest_id ) REFERENCES Restaurant( rest_id );