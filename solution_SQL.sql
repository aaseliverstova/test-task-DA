# Задание 1

select
    id,
    scores,
    dense_rank() over (order by scores desc) as rating_position
from examination;

# Задание 3

select a.client_id
from account a
join transaction t
  on t.account_id = a.id
where t.type = 'buy'
  and t.transaction_date >= current_date - interval '1 month'
group by a.client_id
having sum(t.amount) < 5000;
