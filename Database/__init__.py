import mysql.connector
import random


def connectToDatabase(config):  # returns scary mysql database class
    return mysql.connector.connect(user=config['DataBase']['login'],
                                   password=config['DataBase']['password'],
                                   host=config['DataBase']['host'],
                                   database=config['DataBase']['dataBaseName'],
                                   auth_plugin='mysql_native_password')


def generateRandomValues(config, database, numberOfRows) -> None:
    cursor = database.cursor()
    for i in range(numberOfRows):
        data = "INSERT INTO {} (latitude, longitude, comment) VALUES (%s, %s, %s)".format(
            config['DataBase']['tableName'])
        
        cursor.execute(data, (random.randint(10 ** 7, 4 * 10 ** 7) / 10 ** 6,
                              random.randint(10 ** 7, 7 * 10 ** 7) / 10 ** 6,
                              "piece of random comment"))
        database.commit()


def getInformationFromDatabase(config, database) -> list:
    cursor = database.cursor()
    cursor.execute("SELECT * FROM {}".format(config['DataBase']['tableName']))
    return cursor.fetchall()
