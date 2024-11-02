--Посчитать число первых платежей за дату 16 января в таблице finance Не забудьте отфильтровать по полю is_test

with
payments_data as (
	select *,
		toDate(event_time) as date,
		row_number() over(partition by uid) as payment
	from finance f
)
select count(uid) as count_uid
from payments_data
where payment = 1
	and date = '2023-01-16'
	and is_test = 0


-- В какую из недель была максимальная выручка в таблице finance Не забудьте отфильтровать по полю is_test

select toStartOfWeek(event_time, 1) as week,
	sumIf(revenue_usd, is_test = 0) as sum_revenue_usd
from finance f
group by week
order by sum_revenue_usd desc