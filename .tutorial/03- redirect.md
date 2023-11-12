# Redirecting

Redirecting is useful when you want to send a user to another web address, but that address is really long.

It requires another import at the top of the `main.py` file:
```python
from flask import Flask, redirect
```

👉 Now I'll add an app route.  In this example, I want to redirect users to my page for Day 77.  All I put in the subroutine is a `return redirect("")` with the URL in the quotes.

```python
from flask import Flask, redirect

@app.route('/77')
def seventySeven():
  return redirect("https://replit.com/@DavidAtReplit/Day-077-Solution#main.py")
  
  return page
```
This is really powerful. You've effectively created your own link shortener. All the user has to do is add `/77` to the end of the home page URL.

### Try it out!