CREATE SCHEMA IF NOT EXISTS rides;

CREATE TABLE IF NOT exists rides.ride_data (
    vendor_id integer,
    pickup_datetime timestamp,
    dropoff_datetime timestamp,
    passenger_count integer,
    trip_distance double precision,
    rate_code_id integer,
    store_and_fwd_flag varchar(2),
    pickup_location_id integer,
    dropoff_location_id integer,
    payment_type integer,
    fare_amount double precision,
    extra double precision,
    mta_tax double precision,
    tip_amount double precision,
    tolls_amount double precision,
    improvement_surcharge double precision,
    total_amount double precision,
    congestion_surcharge double precision
);

DELETE FROM rides.ride_data where pickup_datetime >= '2019-02-01';