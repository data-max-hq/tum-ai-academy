# tum-ai-academy
Deploy AI Models - Making AI models accessible to users.

## How-to
To get started with making ML applications reachable to users:

### Step 1: Clone this repo

1. Click `<>Code`
2. Copy the link from `HTTPS`
3. Open your IDE
4. Start a new repo from VCS
5. Paste the link copied in Step 2

### Step 2: Install Requirements

For `PyCharm`/`IntelliJ` users:
1. On the lower left-hand side, click `Python Packages`
2. Search for `fastapi`
3. On the right-hand side, click `Install package`
4. Repeat Steps 2 and 3 for `uvicorn`, `torch` and `transformers`

For `VSCode` users:
1. Go to `Python` on the left-hand side
2. At `Workspace Environment`, go to `Packages`
3. Click on the search icon
4. Search for `fastapi` and click on the first item
5. Repeat Step 4 for `uvicorn`, `torch` and `transformers`

For terminal users:
```commandline
pip install -r requirements.txt
```

### Step 3: Run `hello-world`

1. Open `ex1.py`
2. Right-click and go to `Run ex1.py`
3. Follow this link: [http://localhost:8000/](http://localhost:8000/)

### Step 4: Run Classification Model

1. Open `ex2.py`
2. Right-click and go to `Run ex2.py`
3. Follow this link: [http://localhost:8000/analysis?query=I am very happy with the purchase](http://localhost:8000/analysis?query=I%20am%20very%20happy%20with%20the%20purchase)

### Step 5: Run Generative Model

1. Open `ex3.py`
2. Right-click and go to `Run ex3.py`
3. Follow this link: [http://localhost:8000/generate?prompt=translate English to German That is good](http://localhost:8000/generate?prompt=translate%20English%20to%20German%20That%20is%20good)

### Step 6: Clean Up

1. Open `cleanup.py`
2. Right-click and go to `Run cleanup.py`
