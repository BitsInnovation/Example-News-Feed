# News Feed Example

## Steps to Run Example:

### Step 1: Create a virtual environment

I included a "requirements.txt" file that you can use to install all the dependencies for running the app.

__NOTE:__ if you already have Django 1.9+ installed, you can probably skip this step.


Simply run:

```bash
$ virtualenv venv
$ source venv/bin/activate
$ cd news_feed
$ pip install -r requirements.txt
```

### Step 2: Run the Django app

I also included a very light weight Sqlite Database. No need to 'migrate' anything.

Go into the Django app and run:

```bash
$ python manage.py runserver
```

### Step 3: Try out different URLs

There is NO authentication in this system, all you have to do is change the URL
to see a different News Feed.

Here are the URLs you can try:

(http://localhost:8000/feed/christy/)[http://localhost:8000/feed/christy/]
(http://localhost:8000/feed/bob/)[http://localhost:8000/feed/bob/]
(http://localhost:8000/feed/dorthy/)[http://localhost:8000/feed/dorthy/]

There is also an Admin site that you can use to change the data:

(http://localhost:8000/admin)[http://localhost:8000/admin]

To access the admin site:

Username: admin
Password: adminadmin

Hope you find this valuable.
