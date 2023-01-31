# 🚄URL Shortener
A simple URL Shortener API

I wrote a simple API for short your links.
With this API you can create your own link shortening service.

# ✅ Installing
Install **Python 3.10 [REQUIRED]**

Create a new virtual environment
`python3.10 -m venv venv`

Switch to virtual enironvment that was created before

Install depedencies
`pip install -r requirements.txt`

Configure `config.py`

> Instruction how to configure config below

Run your application
`uvicorn main:app`

# ♻ How to configure `config.py`
Set `mongo_link` to your MongoDB connection link and add at the end "/{your_database}"

Set `domain` to your URL shortening service

# ❗ How it works
Short your link: ![image](https://user-images.githubusercontent.com/94528892/215886232-57b0571a-3f06-408d-a57a-1fe8674e753a.png)
![image](https://user-images.githubusercontent.com/94528892/215886457-c64b7168-c63a-4b84-9517-384abbf21e96.png)


Redirecting from short link to main link:

![image](https://user-images.githubusercontent.com/94528892/215886502-24f9688e-a9e1-457a-b9c5-91dfc3aee2ca.png)

# License
This repository is public, the developer allows the use of this code for commercial and private purposes.
But it is forbidden for the user to impersonate the author of the code if he is not.
It is allowed to impersonate the author of the code only after a complete rewrite of the code. But the developer urges to specify it in the line of authors.
Respect the efforts of others, thank you

Created by `pro0xy`
