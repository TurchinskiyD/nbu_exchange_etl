-- Створення користувача
CREATE USER nbu_rw WITH PASSWORD 'rw_secure_password';

-- Надання прав на схему
GRANT USAGE ON SCHEMA nbu TO nbu_rw;

-- Надання прав на читання/запис у всі таблиці
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA nbu TO nbu_rw;

-- Автоматичне надання прав на майбутні таблиці
ALTER DEFAULT PRIVILEGES IN SCHEMA nbu
	GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO nbu_rw;


-- Створення користувача
CREATE USER nbu_ro WITH PASSWORD 'ro_secure_password';

-- Доступ до схеми
GRANT USAGE ON SCHEMA nbu TO nbu_ro;

-- Надання прав тільки на читання
GRANT SELECT ON ALL TABLES IN SCHEMA nbu TO nbu_ro;

-- Автоматичне надання прав на майбутні таблиці тільки для читання
ALTER DEFAULT PRIVILEGES IN SCHEMA nbu
  GRANT SELECT ON TABLES TO nbu_ro;


SELECT rolname, rolsuper, rolcreaterole, rolcreatedb, rolcanlogin
FROM pg_roles
WHERE rolcanlogin = true;


rolname|rolsuper|rolcreaterole|rolcreatedb|rolcanlogin|
-------+--------+-------------+-----------+-----------+
airflow|true    |true         |true       |true       |
nbu_rw |false   |false        |false      |true       |
nbu_ro |false   |false        |false      |true       |



SELECT n.nspname AS schema,
       r.rolname AS role,
       has_schema_privilege(r.rolname, n.nspname, 'USAGE') AS usage,
       has_schema_privilege(r.rolname, n.nspname, 'CREATE') AS create
FROM pg_namespace n
JOIN pg_roles r ON r.rolcanlogin = true
WHERE n.nspname = 'nbu';


schema|role   |usage|create|
------+-------+-----+------+
nbu   |airflow|true |true  |
nbu   |nbu_rw |true |false |
nbu   |nbu_ro |true |false |
