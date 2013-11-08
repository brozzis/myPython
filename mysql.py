#!/usr/local/bin/python
import MySQLdb


class myMy:

    def __init__(self, host="localhost", user="ste", passwd="ste", name="ste"):

		try:
		    db = MySQLdb.connect(host="localhost", # your host, usually localhost
		                     user="ste", # your username
		                      passwd="ste", # your password
		                      db="crm") # name of the data base

		except:
		    print "cannot connect to db"
		    return

		self.cur = db.cursor() 


    def getVersion(self):
            self.cursor.execute ("SELECT VERSION()")
            row = cursor.fetchone()
            print "server version:", row[0]


    def getRow(self, sql):

            self.cur.execute(sql)

            return self.cur.fetchone()

    def getRows(self, sql):
            # Use all the SQL you like
            self.cur.execute(sql)

            return self.cur.fetchall()


    def query(self, sql):
            self.cur.execute(sql)
            pass

    def disconnect(self):
            self.cur.close ()
            self.db.close ()
	

# Main must be outside the table class
def main():

	x = myMy()

	rows = x.getRows("SELECT * FROM comuni limit 5")

	for row in  rows:
	    print row[3]


if __name__ == '__main__':
    main()


