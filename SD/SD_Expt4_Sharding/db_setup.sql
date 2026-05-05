CREATE DATABASE company_main;
USE company_main;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);

CREATE DATABASE shard_hr;
USE shard_hr;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);

CREATE DATABASE shard_it;
USE shard_it;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);

CREATE DATABASE shard_engineering;
USE shard_engineering;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);

CREATE DATABASE odd_shard;
USE odd_shard;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);

CREATE DATABASE even_shard;
USE even_shard;
CREATE TABLE users (
    id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    joining_date DATE,
    dob DATE,
    age INT,
    role VARCHAR(50),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    login_id VARCHAR(50),
    password VARCHAR(64)
);