![](https://img.shields.io/badge/version-v0.7.3-gold)  
![](https://img.shields.io/badge/python-v3.10.1-blue)
![](https://img.shields.io/badge/Flask-v2.1.2-pink)
![](https://img.shields.io/badge/Docker-v20.10.17-orange)
![](https://img.shields.io/badge/flake8-v5.0.4-purple)

![](https://img.shields.io/badge/pytest-v7.1.2-black)
![](https://img.shields.io/badge/passed_tests-14-brightgreen)
![](https://img.shields.io/badge/failed_tests-0-red)

![](https://img.shields.io/badge/coverage-100%25-brightgreen)

### Click here to acess the [Deployed Application](http://salatiel6.pythonanywhere.com/docs)

---

- [The Challenge](#the-challenge)
- [The Vowel Count Feature](#the-vowel-count-feature)
- [The Sort Feature](#the-sort-feature)
- [How To Run Locally](#how-to-run-locally)
- [How To Run With Docker](#how-to-run-with-docker)
- [Documentation](#documentation)

# The Challenge
The challenge was to build an API which could receive a list of words, return either the number of vowels of each word, and a sorted list in ascending or descending order.

The whole solution was built with `Flask`, linted with `flake8`, tested with `pytest`, documented on swagger with `flask-restx`, and deployed at `PythonAnywhere`.

## The Vowel Count Feature
For counting the vowels of each word, I chose to use `re` library, and assert the vowels count with a regular expression:
```
result = {}

words = self.request_data["words"]
for word in words:
    vowels = len(re.findall("[aeiouAEIOU]", word))
    result[word] = vowels

return result
```
As you can see, for each word on the list, the vowels are counted and stored as a value on a dictionary that has the current word as a key.

## The Sort Feature
For sorting the words, I chose to use the built-in function `sort()`. Which sorts the list in alphabetical order.   
That's how the code works, for sorting ascending:
```
words = self.request_data["words"]
result = {"result": sorted(words)}

return result
```
As you can see, the `sorted()` function, gets the words list and does the job.  

For sorting descending, I only add the python list manipulation `[::-1]` after the list. So after sorting on ascending order, it turns the list from back to front:
```
words = self.request_data["words"]
result = {"result": sorted(words)[::-1]}

return result
```

## How To Run Locally
Requirements:
- [Git](https://git-scm.com/downloads)
- [Python3.10](https://www.python.org/downloads/)

1. Clone the repository  
`https://github.com/salatiel6/pilar_challenge.git`


2.  Create virtual environment (recommended)  
`python -m venv ./venv`


3. Activate virtual environment (recommended)  
Windows: `venv\Scripts\activate`  
Linux/Mac: `source venv/bin/activate`


4. Open the challenge directory  
Widows/Linux:`cd shape_challenge`  
Mac: `open shape_challenge`


5. Install every dependencies  
`pip install -r requirements.txt`


6. Open the source directory  
Windows/Linux: `cd src`  
Mac: `open src`


7. Run tests  
Without coverage: `pytest`  
With coverage: `pytest -vv --cov=. --cov-report=term-missing --cov-config=.coveragerc`


8. Run the application  
`python run.py`


11. Check the API [Documentation](#documentation)

## How To Run With Docker
This application was developed in a Windows OS. So I'm not sure if Linux or Mac could run the container.

Requirements:
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/)

1. Clone the repository  
`https://github.com/salatiel6/pilar_challenge.git`


2. Open the challenge directory  
Widows/Linux:`cd shape_challenge`  
Mac: `open shape_challenge`


3. Build docker image  
`docker-compose build`


4. Start docker container  
`docker-compose up -d`


5. Check the API [Documentation](#documentation)

## Documentation
The both endpoints are documented on a `swagger UI`, built with `flask-restx`.

If you got directly for the deployed application on PythonAnywhere acess `http://salatiel6.pythonanywhere.com/docs`.

If you run the application locally access `http://localhost:4670/docs` to check it out.  
**OBS**: Remember to check if your browser is not forcing `http` to `https`. If it happens you won't be able to access the swagger.