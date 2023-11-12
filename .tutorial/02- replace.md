# fStrings and Replacing

Using fStrings and the `.replace()` string manipulation technique from many lessons ago lets us customize the webpage for our user. Here's how:


👉 First, I've put a placeholder for a name in my **portfolio.html** file.

```html
<body>

  <h1>{name}'s Portfolio</h1>
```

👉 Now in the Flask code, I can use the `replace()` function.  Note that I've done this **before the return command.**

```python
@app.route('/')
def index():
  myName = "Katie"
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{name}", myName) # Replace all instances of {name} with the contents of the 'myName' variable
  
  return page
```
I can reuse this technique to make multiple changes to a page.

👉 Let's look at some example code where I've done this to create a generic page that can be customised by the user:

```html
<body>

  <h1>{name}'s Portfolio</h1>
  <h2>{title}</h2>
  <p>{text}</p>
<a href="{link}"><img src="static/images/{image}" width="500px"></a>
```

👉 Now in my main code, all I have to do is store the information in variables and use multiple `replace`.

```python
def index():
  myName = "Katie"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "56.png"
  link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"
  
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page.replace("{name}", myName)
  page.replace("{title}", title)
  page.replace("{text}", text)
  page.replace("{image}", image)
  page.replace("{link}", link)
  return page
```

I've just recreated the same page here, but I've done it in a way that makes it **much easier** to use as a template.

👉 For example, I could create Day 56 as its own `app.route` like this:

```python
@app.route('/56')
def fiftySix():
  myName = "Dave"
  title = "Day 56 Solution"
  text = "So, day 56 was all about using csv reading and file and folder manipulation to make 100 files in dozens of folders. This was tricky because the names of the folders and files were based on the top 100 streaming songs and so weren't simple to encode."
  image = "56.png"
  link = "https://replit.com/@DavidAtReplit/Day-056-Solution#main.py"
  
  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page.replace("{name}", myName)
  page.replace("{title}", title)
  page.replace("{text}", text)
  page.replace("{image}", image)
  page.replace("{link}", link)
  return page
 
```
To create day 57, I'd just write another `app.route` with a subroutine, but it would **reuse the portfolio.html** file as a template.  I'd only need to create that html file **once**. Nice!

### Try it out!