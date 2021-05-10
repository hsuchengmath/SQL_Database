# SQL_Database

## install
```
SELECT (*column) FROM (*table) WHERE (*rule)
sudo apt-get install mysql-server
```
Ref : [https://docs.rackspace.com/support/how-to/install-mysql-server-on-the-ubuntu-operating-system/]


## create account and give auth
```
CREATE USER 'account_name'@'localhost' IDENTIFIED BY 'account_name';
GRANT ALL PRIVILEGES ON *.* TO 'account_name'@'localhost';
```
Ref : [https://caloskao.org/mariadb-mysql-create-account-and-grant-access-in-cli/]


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
