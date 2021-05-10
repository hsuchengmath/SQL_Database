# SQL_Database

## Syntax
a. Basic
```
SELECT (*column) FROM (*table) WHERE (*rule)
```
b. Order by
```
SELECT (*column) FROM (*table) WHERE (*rule) ORDER BY (*target-column ASC/DESC) *echo
```
Ref : [https://www.fooish.com/sql/order-by.html]

c. Group by <agg() => count(), sum(), avg(), max(), min()>
```
SELECT (*agg(*agged-column)) FROM (*table) WHERE (*rule) GROUP BY (*target-column)
```
Ref : [https://www.fooish.com/sql/group-by.htm]

d. Join <INNER:intersection | LEFT/RIGHT :left/right record will be expressed all time | FULL : all record will be expressed all time.>
```
SELECT (*column) FROM (*table-1) (INNER/LEFT/RIGHT/FULL) JOIN *table-2 on (*rule)
```
Ref : [https://www.fooish.com/sql/join.html]

e. Dense_rank over(...) : select dense_rank over(order by *column ASC/DESC)
```
SELECT (*column), DENSE_RANK() OVER(ORDER BY *target-column ASC/DESC)
```
Ref : [https://www.yiibai.com/sqlserver/sql-server-dense_rank-function.html]
