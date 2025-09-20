--  create the table unique_id 
CREATE table IF NOT EXISTS unique_id  (
    id INT DEFAULT 1 unique,
    name varchar(256)
);