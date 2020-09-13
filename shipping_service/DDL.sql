CREATE schema shipping_service;

CREATE TABLE shipping_service.orders  (
    order_id serial,
    product_name character varying,
    quantity INT,
    price BigINT
);
