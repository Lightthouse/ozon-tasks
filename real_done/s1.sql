select * from problems
where id in (select problem_id from submissions
where success
group by problem_id
having(count(distinct(user_id)) > 1)
)

