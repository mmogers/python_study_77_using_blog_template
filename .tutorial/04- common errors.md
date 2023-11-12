# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Common Error 1

👉 What's the problem here?

```python
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
redirect("https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")
```

<details> <summary> 👀 Answer </summary>

I've missed the `return` before `redirect` which will create a TypeError.

```python
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
  return redirect("https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")
```

</details>

## Common Error 2

👉 What's the problem here?
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
  page.replace("a", link)
  return page
```

<details> <summary> 👀 Answer </summary>

The problem is with the last `replace`. It will replace every instance of 'a' in the page with the stored hyperlink. This is because I've not used the curly braces.

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
  page.replace("{a}", link)
  return page
```