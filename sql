CREATE DATABASE blog DEFAULT CHARACTER SET utf8;
USE BLOG;
CREATE TABLE blog(
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  /*文章id*/
`title` VARCHAR(100) NOT NULL,  /*文章标题*/
`date` DATE NOT NULL,  /*文章日期*/
`identity` VARCHAR(50) DEFAULT 'other',  /*类别*/
`essay` MEDIUMTEXT, /*文章内容*/
`view` INT NOT NULL DEFAULT 0  /*文件浏览数*/
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
