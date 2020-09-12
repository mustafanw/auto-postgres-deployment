---Service Version 1.0
CREATE schema shipping_service;

CREATE TABLE shipping_services.Orders  (
    order_id character varying,
    address character varying,
    status character varying
);