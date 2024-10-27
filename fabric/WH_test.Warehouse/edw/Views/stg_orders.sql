create view "edw"."stg_orders" as with source as (
    select * from "WH_test"."edw"."raw_orders"

),

renamed as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

)

select * from renamed;