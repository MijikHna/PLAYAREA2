CREATE USER admin WITH PASSWORD 'password';
CREATE DATABASE playarea_db;uu
GRANT ALL PRIVILEGES ON DATABASE playarea_db TO admin;
/*
SELECT 'CREATE DATABASE playarea_db' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'playarea_db')\gexec

--CREATE DATABASE playarea_db;
CREATE USER playarea_admin WITH PASSWORD 'playarea-password';

ALTER ROLE playarea_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE playarea_admin SET client_encoding TO 'utf8';
ALTER ROLE playarea_admin SET timezone TO 'UTC';

\c playarea_db


create table IF NOT EXISTS "GAMEDAY_user" (id serial PRIMARY KEY, "userName" varchar(30) NOT NULL, "userPassword" varchar(30) NOT NULL);

insert into "GAMEDAY_user" ("userName", "userPassword")  values('Admin', 'i82B[;\DRp;z,\g)');
insert into "GAMEDAY_user" ("userName", "userPassword")  values('Jackson', 'iI-gOd]1gbfXRTKW');
insert into "GAMEDAY_user" ("userName", "userPassword")  values('Rebecca', '*ss;2Wh.8]vhk"1W');

create table IF NOT EXISTS "GAMEDAY_node" (id serial PRIMARY KEY, "nodeName" varchar(30) NOT NULL, "nodeUser" varchar(30) NOT NULL, "nodeSSHPort" varchar(5) NOT NULL);

insert into "GAMEDAY_node" ("nodeName", "nodeUser", "nodeSSHPort")  values('nginx', 'jackson', '2222');
insert into "GAMEDAY_node" ("nodeName", "nodeUser", "nodeSSHPort")  values('django', 'guiseppe', '22');
insert into "GAMEDAY_node" ("nodeName", "nodeUser", "nodeSSHPort")  values('mongo', 'lorenzo', '22');
insert into "GAMEDAY_node" ("nodeName", "nodeUser", "nodeSSHPort")  values('postgres', 'rebecca', '22');
insert into "GAMEDAY_node" ("nodeName", "nodeUser", "nodeSSHPort")  values('flag', '####', '');

create table IF NOT EXISTS "GAMEDAY_flag" (id serial PRIMARY KEY, "flag" varchar(30) NOT NULL);

insert into "GAMEDAY_flag" ("flag")  values( 'FLAG_SEHT84');

GRANT ALL PRIVILEGES ON DATABASE playarea_db TO postgres;
GRANT ALL PRIVILEGES ON DATABASE playarea_db TO playarea_admin;

GRANT ALL ON ALL TABLES IN SCHEMA public to playarea_admin;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to playarea_admin;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to playarea_admin;
*/