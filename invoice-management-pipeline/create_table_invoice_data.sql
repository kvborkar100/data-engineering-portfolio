CREATE TABLE invoice_data (
    invoice_id        NUMBER(10)
        GENERATED BY DEFAULT ON NULL AS IDENTITY
    PRIMARY KEY,
    invoice_number    VARCHAR2(20),
    invoice_date      DATE,
    payment_terms     NUMBER(3),
    invoice_currency  VARCHAR(10),
    company_name      VARCHAR2(50),
    line_number       NUMBER(3),
    item_name         VARCHAR2(50),
    quantity          NUMBER(3),
    amount            NUMBER(10),
    total_amount      NUMBER(10),
    vat               NUMBER(2),
    invoice_amount    NUMBER(10)
);