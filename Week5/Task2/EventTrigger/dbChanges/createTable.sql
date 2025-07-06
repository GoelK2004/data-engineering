CREATE TABLE pr.category_audits(
    change_id INT IDENTITY PRIMARY KEY,
    category_id INT NOT NULL,
    category_name VARCHAR(255) NOT NULL,
    updated_at DATETIME NOT NULL,
    operation CHAR(3) NOT NULL,
    CHECK(operation = 'INS' or operation='DEL')
);
