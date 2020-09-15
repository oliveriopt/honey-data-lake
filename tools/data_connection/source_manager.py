#!/usr/bin/env python3
import logging
import sys
import psycopg2

logger = logging.getLogger()
#warnings.filterwarnings("ignore", category=psycopg2.Warning)


class Connector:

    def __init__(self, user: str, pw: str, host: str, port:str, database: str):
        assert user, "Database <user> is not set."
        assert host, "Database <host> is not set."
        assert port, "Database <port> is not set."

        self.__host = host
        self.__user = user
        self.__port = int(port)
        self.__password = pw
        self.__database = database
        self.__conn = None

    def close_connection(self):
        """
        Close connection to the database
        :return:
        """
        if self.__conn is not None:
            self.__conn.close()

    def open_connection(self) -> None:
        """
        Open a connection to MySQL server
        :return:
        """
        try:
            if self.__database:
                self.__conn = psycopg2.connect(host=self.__host, port=self.__port,
                                               user=self.__user, password=self.__password, dbname=self.__database)
            else:
                self.__conn = psycopg2.connect(host=self.__host, port=self.__port,
                                               user=self.__user, password=self.__password)
            print("Connection to server successful!")
            logger.info(msg="Connection to server successful!")
        except Exception as e:
            logger.error(msg="Error connecting to database:  %s" % e)
            sys.exit(1)

    def select_query(self, query: str) -> tuple:
        """
        Executes a SELECT query
        :return: object containing results from SELECT
        """
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
                self.__conn.commit()
                result = cursor.fetchall()

        except Exception as e:
            logger.error(msg="Error executing select query: %s" % e)
            raise Exception('Not able to execute the select query %s : %s' % (query, e))

        return result

    def insert_query(self, query: str) -> int:
        """
        Executes a INSERT query
        :param query:
        :return: affected rows
        """
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(query)
                self.__conn.commit()
                return cursor.rowcount

        except Exception as e:
            logger.error(msg="Error executing insert query: %s" % e)
            raise Exception('Not able to execute the select query %s : %s' % (query, e))
