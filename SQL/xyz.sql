drop database if exists testdb;

create database testdb;

use testdb;

create table product(pid int,pname varchar(10),price int);

insert into product
	values(1,'mouse',300),(2,'Pendrive',600),(3,'moniter',14000);

select * from product;
