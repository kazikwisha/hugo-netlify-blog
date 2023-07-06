---
title: JSON Function - json_build_object
date: 2020-11-18
tags: [sql]
description: an example query  of how to use json_build_object function
draft: false
---

### Explanation(TODO:10)

```sql
SELECT
  o.id,o.total_cost,o.managed_by,
  CASE WHEN count(ox) = 0 THEN ARRAY[]::json[] ELSE array_agg(ox.order_item) END AS order_items
FROM fasiba.orders o
  LEFT OUTER JOIN
  (
    SELECT oid2.orders_id, json_build_object('input_name',i.name,'quantity',oid2.quantity,'unit_cost',oid2.unit_cost,'total_cost',oid2.total_cost) as order_item
    FROM fasiba.orders_input_detail oid2
    left join fasiba.input i on i.id = oid2.input_pack_detail_id
    ORDER BY oid2.input_pack_id
  ) ox
    ON o.id = ox.orders_id
WHERE o.status ='DELIVERED'
GROUP BY o.id
limit 10
```


### REFERENCE

For a more elaborative example have a look at the link below.

- https://foxypanda.me/returning-an-array-of-json-objects-in-postgresql/


