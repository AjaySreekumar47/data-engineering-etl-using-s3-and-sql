-- Building fact and dimension tables. Here, grain is taken as the orders from the dataset
create or replace table dim_users as (
    select user_id from orders
);

create or replace table dim_products as (
    select product_id, product_name from products
);

create or replace table dim_aisles as (
    select aisle_id, aisle from aisles
);

create or replace table dim_departments as (
    select department_id, department from departments
);

create or replace table dim_orders as (
    select order_id, order_number, order_dow, order_hour_of_day, days_since_prior_order
    from orders
);

-- Fact table creation
CREATE TABLE fact_order_products AS (
  SELECT
    op.order_id,
    op.product_id,
    o.user_id,
    p.department_id,
    p.aisle_id,
    op.add_to_cart_order,
    op.reordered
  FROM
    order_products op
  JOIN
    orders o ON op.order_id = o.order_id
  JOIN
    products p ON op.product_id = p.product_id
);