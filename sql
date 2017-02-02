CREATE DATABASE blog DEFAULT CHARACTER SET utf8;
USE blog;
CREATE TABLE blog(
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  /*文章id*/
`title` VARCHAR(100) NOT NULL,  /*文章标题*/
`date` DATE NOT NULL DEFAULT '1996-02-01',  /*文章日期*/
`identity` VARCHAR(50) DEFAULT 'other',  /*类别*/
`essay` MEDIUMTEXT, /*文章内容*/
`view` INT NOT NULL DEFAULT 0  /*文件浏览数*/
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


'SELECT DISTINCT identity FROM blog;'   /*只查询重复数据*/

mysql> select identity, count(*) from blog group by identity;   /*显示重复数据及多少*/
+----------+----------+
| identity | count(*) |
+----------+----------+
| game     |        1 |
| other    |        9 |
+----------+----------+
2 rows in set (0.00 sec)

mysql> SELECT date, count(*) FROM blog group by date;
+------------+----------+
| date       | count(*) |
+------------+----------+
| 0000-00-00 |        2 |
| 2012-03-03 |        1 |
| 2013-03-03 |        2 |
| 2013-03-05 |        3 |
| 2013-03-07 |        1 |
| 2017-01-02 |        1 |
+------------+----------+
6 rows in set, 4 warnings (0.00 sec)

UPDATE blog SET title='NUM', essay='fuck you' WHERE id=4;