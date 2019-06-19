#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'


# query_one: 1. What are the most popular three articles of all time?

query_one = """SELECT articles.title, count (*) as num
                FROM articles, log
                WHERE log.status = '200 OK'
                AND articles.slug = substring(log.path, 10)
                GROUP BY articles.title
                ORDER BY num desc
                LIMIT 3;"""

# query_two: Who are the most popular article authors of all time?

query_two = """SELECT authors.name, count(*) as num
                FROM authors, log, articles
                WHERE log.status = '200 OK'
                AND authors.id = articles.author
                AND articles.slug = substring(log.path, 10)
                GROUP BY authors.name
                ORDER BY num desc;"""

# On which days did more than 1% of requests lead to errors?

query_three = """SELECT errorcount.date, round(100.0*errors/logscount,2) as percent
                FROM logs, errorcount
                WHERE logs.date = errorcount.date
                AND errors > logscount/100;"""


# Connect to the database to extract the SQL query results

def connect(query):
        # Connect to the 'news' database 
        db = psycopg2.connect(database=DBNAME)
        # Set a python cursor to select specific information within the database
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results



def popular_articles():
        results = connect(query_one)
        print('What are the most popular three articles of all time?\n')
        for item in results:
                print(str(item[0]) + ' | ' + str(item[1]) + ' views') 
        
    

def popular_authors():
        results = connect(query_two)
        print('\n\nWho are the most popular article authors of all time? \n')
        for item in results:
                print(str(item[0]) + ' | ' + str(item[1]) + ' views')



def error_check():
        results = connect(query_three)
        print('\n\nOn which days did more than 1% of requests lead to errors?')
        for item in results:
                print('\n' + str(item[0]) + ' | ' + str(item[1]) + '% errors')



if __name__ == '__main__':
        popular_articles()
        popular_authors()
        error_check()
