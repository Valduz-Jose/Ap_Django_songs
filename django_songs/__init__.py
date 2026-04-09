import pymysql

# 1. Registrar PyMySQL como si fuera MySQLdb
pymysql.install_as_MySQLdb()

# 2. Engañar a Django para que crea que tenemos una versión compatible (2.2.1+)
# Esto evita el error "mysqlclient 2.2.1 or newer is required"
pymysql.version_info = (2, 2, 1, "final", 0)