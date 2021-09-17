    SELECT rate
    FROM exchange_rates s1
    WHERE ts = (SELECT MAX(ts) FROM exchange_rates) and to_currency='GBP';


highest exchange rate 1.62




*****************

select t.ts, t.user_id, t.amount * e.rate as conv_amount
from   transactions t
join lateral (select *
              from   exchange_rates er
              where  t.currency = er.from_currency
              and    er.ts <= t.ts
              order by ts desc
              limit 1) e on true;

****************

SELECT transactions.user_id, transactions.amount * exchange_rates.rate as conv_amount
FROM transactions
INNER JOIN exchange_rates ON exchange_rates.from_currency=transactions.currency
WHERE exchange_rates.to_currency = 'GBP' and exchange_rates.ts = (SELECT MAX(ts) FROM exchange_rates);