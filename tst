CHEKWASY_MYSQL_USER=chekwasy_dev CHEKWASY_MYSQL_PWD=CHEKWASY_dev_pwd_001 CHEKWASY_MYSQL_HOST=localhost CHEKWASY_MYSQL_DB=bincomphptest CHEKWASY_TYPE_STORAGE=db CHEKWASY_API_HOST=0.0.0.0 CHEKWASY_API_PORT=5001 python3 -m api.v1.app

curl -X GET http://0.0.0.0:5001/api/v1/employees/abc

curl -X PUT http://0.0.0.0:5001/api/v1/employees/abc/521a55f4-7d82-47d9-b54c-a76916479545 -H "Content-Type: application/json" -d '{"dept": "Customer service"}'

curl -X DELETE http://0.0.0.0:5001/api/v1/employees/abc/521a55f4-7d82-47d9-b54c-a76916479545