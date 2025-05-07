SELECT log_time, dag_id, task_id, execution_date, try_number, status, message
FROM nbu.etl_logs;




log_time               |dag_id                  |task_id              |execution_date         |try_number|status |message
-----------------------+------------------------+---------------------+-----------------------+----------+-------+-----------------------------------
2025-05-07 06:06:31.932|nbu_exchange_rates_to_db|create_etl_logs_table|2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:33.088|nbu_exchange_rates_to_db|check_nbu_api        |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:34.068|nbu_exchange_rates_to_db|fetch_nbu_data       |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:36.014|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:37.010|nbu_exchange_rates_to_db|init_db_table        |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:54.434|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:56.067|nbu_exchange_rates_to_db|insert_to_postgres   |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-07 06:06:56.706|nbu_exchange_rates_to_db|init_db_table        |2025-05-07 06:06:30.769|         2|success|http://localhost:8080/log?execution
2025-05-06 07:04:15.837|nbu_exchange_rates_to_db|init_db_table        |2025-05-05 00:00:00.000|         2|success|http://localhost:8080/log?execution
2025-05-05 18:59:25.203|nbu_exchange_rates_to_db|fetch_nbu_data       |2025-05-05 13:58:33.458|         4|success|
2025-05-05 19:44:27.655|nbu_exchange_rates_to_db|create_etl_logs_table|2025-05-05 19:16:24.919|         4|success|Log file not found: /opt/airflow/lo
2025-05-07 06:02:14.485|nbu_exchange_rates_to_db|test_fail            |2025-05-06 00:00:00.000|         4|failure|http://localhost:8080/log?execution
2025-05-06 13:41:51.079|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-06 13:39:39.042|         4|failure|http://localhost:8080/log?execution
2025-05-06 13:44:45.200|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-06 13:42:33.516|         4|failure|http://localhost:8080/log?execution
2025-05-06 14:56:10.908|nbu_exchange_rates_to_db|insert_to_postgres   |2025-05-06 14:53:47.926|         4|failure|http://localhost:8080/log?execution
2025-05-06 15:03:49.728|nbu_exchange_rates_to_db|insert_to_postgres   |2025-05-06 15:01:27.725|         4|failure|http://localhost:8080/log?execution
2025-05-06 15:08:46.559|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-06 15:07:28.301|         2|success|http://localhost:8080/log?execution
2025-05-06 17:29:09.436|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-06 17:28:42.013|         2|success|http://localhost:8080/log?execution
2025-05-06 17:59:27.357|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-06 17:43:33.865|         4|success|http://localhost:8080/log?execution
2025-05-06 18:00:17.199|nbu_exchange_rates_to_db|init_db_table        |2025-05-06 18:00:08.816|         2|success|http://localhost:8080/log?execution
2025-05-06 18:56:48.860|nbu_exchange_rates_to_db|init_db_table        |2025-05-06 18:56:38.669|         2|success|http://localhost:8080/log?execution
2025-05-06 19:40:37.069|nbu_exchange_rates_to_db|test_fail            |2025-05-06 19:27:56.835|         4|failure|http://localhost:8080/log?execution
2025-05-05 19:18:17.718|test_log_etl_callback   |say_hello            |2025-05-04 00:00:00.000|         2|success|
2025-05-06 07:04:12.514|test_log_etl_callback   |say_hello            |2025-05-05 00:00:00.000|         2|success|http://localhost:8080/log?execution
2025-05-05 19:36:54.619|test_log_etl_callback   |say_hello            |2025-05-05 19:18:16.297|         4|success|Log file not found: /opt/airflow/lo
2025-05-07 05:59:09.260|test_log_etl_callback   |say_hello            |2025-05-06 00:00:00.000|         2|failure|http://localhost:8080/log?execution
2025-05-06 07:04:38.155|test_log_etl_callback   |say_hello            |2025-05-06 07:04:36.941|         2|success|http://localhost:8080/log?execution
2025-05-06 07:07:07.979|test_log_etl_callback   |say_hello            |2025-05-06 07:07:06.867|         2|failure|http://localhost:8080/log?execution
2025-05-07 07:12:19.900|nbu_exchange_rates_to_db|create_etl_logs_table|2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:12:21.399|nbu_exchange_rates_to_db|check_nbu_api        |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:12:23.014|nbu_exchange_rates_to_db|fetch_nbu_data       |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:12:24.233|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:12:26.224|nbu_exchange_rates_to_db|init_db_table        |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:12:43.683|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:14:13.747|nbu_exchange_rates_to_db|insert_to_postgres   |2025-05-07 07:12:18.001|         4|success|http://localhost:8080/log?execution
2025-05-07 07:14:15.071|nbu_exchange_rates_to_db|fetch_nbu_data       |2025-05-07 07:12:18.001|         2|success|http://localhost:8080/log?execution
2025-05-07 07:58:49.172|nbu_exchange_rates_to_db|create_etl_logs_table|2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:58:50.971|nbu_exchange_rates_to_db|check_nbu_api        |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:58:53.110|nbu_exchange_rates_to_db|fetch_nbu_data       |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:58:54.168|nbu_exchange_rates_to_db|send_to_kafka        |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:58:55.799|nbu_exchange_rates_to_db|init_db_table        |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:59:13.167|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:59:14.201|nbu_exchange_rates_to_db|insert_to_postgres   |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution
2025-05-07 07:59:15.566|nbu_exchange_rates_to_db|consume_from_kafka   |2025-05-07 07:58:47.902|         2|success|http://localhost:8080/log?execution