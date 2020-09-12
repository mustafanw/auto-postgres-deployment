--
-- Incident staging table
--
CREATE TABLE public.incident_staging_tbl_new  (
    incident_id character varying,
    input_data character varying,
    inserted_at bigint,
    source character varying
);

