create view "dbo"."my_second_dbt_model" as -- Use the `ref` function to select from other models

select *
from "WH_test"."dbo"."my_first_dbt_model"
where id = 1;