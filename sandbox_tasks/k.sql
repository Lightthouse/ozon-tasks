select id, name from users
where id in (select user_id from orders )
order by name, id
