create view "edw"."stg_customers" as with source as (
    select * from "WH_test"."edw"."raw_customers"

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed;