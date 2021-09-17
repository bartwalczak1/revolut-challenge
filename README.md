# Revolut assignment

## SQL challenge

### Write down a query that gives us a breakdown of spend in GBP by each user. Use the exchange rate with the largest timestamp. 
```
SELECT transactions.user_id, SUM(transactions.amount * exchange_rates.rate) as amount
FROM transactions, exchange_rates
WHERE exchange_rates.to_currency = 'GBP' and exchange_rates.ts = (SELECT MAX(ts) FROM exchange_rates)
GROUP BY transactions.user_id
ORDER BY transactions.user_id;
```

### (If you consider yourself senior) Write down the same query, but this time, use the latest exchange rate smaller or equal than the transaction timestamp. Solution should have the two columns: user_id, total_spent_gbp, ordered by user_id
```
SELECT t.user_id, SUM(t.amount * e.rate) as total_spent_gbp
FROM transactions t
JOIN lateral (SELECT *
          	FROM exchange_rates er
          	WHERE t.currency = er.from_currency
          	and er.ts <= t.ts
          	ORDER BY ts DESC
          	LIMIT 1) e ON true
GROUP BY t.user_id
ORDER BY t.user_id;
```

## Code challenge

### Run
```
docker-compose up --build
```

### Debug
```
virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app/api.py
```

## Test
```
virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -vvv /test
```

