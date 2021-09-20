# listings_and_reviews
To set up an environment and run scripts you should have:
1. Python 3.8
2. Installed pip and virtualenv.
3. Installed and working PostgreSQL 10 server.

Then you should:
1. Open in console directory with this repository.
2. Write in console "virtualenv venv", to create virtual environment.
3. Open venv by comand "source venv/bin/activate" in Linux or "source venv/Scripts/activate" in Windows.
4. Download all dependencies by command  "pip install -r requirements.txt".
5. Go to the .env file in that directory and write "DB_CREDENTIALS=dialect+driver://username:password@host:port/database".
   Driver, username, username, host, port, database - is information about postges server. 
   It should looks like this - "DB_CREDENTIALS=postgresql://scott:tiger@localhost:5432/mydatabase". Then save this file.
 
 It's all about the environment.
 
 For run the script you should open from console directory with this repository and write "python main.py".
 Script have console interface. 
 To create new tables you should press "3" when menu was printed in console.
 Then choose name for tables thet was created from files listings.csv and reviews_detailed.csv, I recomend names "listings" and "reviews".
 After that choose path to csv files. If you dropped files to working directory you can write jast name of files. In other ways you should write full path,
 like this "C:/Users/User/Desktop/csvs/reviews_detailed.csv", use only "/" for path separating.
 Then tables will be created and you will going to meny.
 In key 1 you can receive suggestions for the neighbourhood.
 In key 2 you can receive listings from the neighbourhood with reviews for the listings.
 In key 4 you can choose tables if you already create it.
