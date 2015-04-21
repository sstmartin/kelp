CREATE TABLE businesses (
business_id varchar(25) NOT NULL PRIMARY KEY,
full_address varchar(125),
hours varchar(500),
is_open varchar(10),
categories varchar(250),
city varchar(50),
review_count int,
business_name varchar(100),
neighborhoods varchar(250),
longitude double precision,
latitude double precision,
state varchar(20),
stars decimal,
attributes varchar(3000),
item_type varchar(10)
);

CREATE TABLE users (
yelping_since char(7),
votes varchar(100),
review_count int,
user_name varchar(100),
user_id varchar(25) NOT NULL PRIMARY KEY,
fans varchar(300),
average_stars decimal,
item_type char(4),
compliments varchar(200),
elite varchar(100)
);

CREATE TABLE reviews (
votes   varchar(100),
user_id varchar(25) NOT NULL,
review_id varchar(25) NOT NULL PRIMARY KEY,
stars decimal,
review_date DATE,
text varchar(15000),
item_type char(6),
business_id varchar(25) 
);

copy businesses from 's3://yelp.datasets/yelp_academic_dataset_business.bsv'
credentials 'aws_access_key_id=xxx;aws_secret_access_key=xxx';

copy users from 's3://yelp.datasets/yelp_academic_dataset_user.bsv'
credentials 'aws_access_key_id=xxx;aws_secret_access_key=xxx';

copy reviews from 's3://yelp.datasets/yelp_academic_dataset_review.bsv'
credentials 'aws_access_key_id=xxx;aws_secret_access_key=xxx';


