CREATE schema account_service;

CREATE TABLE account_service.users  (
    user_id Serial,
    name character varying,
    phone character varying
);
