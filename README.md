# MVS Architecture

![Screen Shot 2020-09-15 at 2 27 27 AM](https://user-images.githubusercontent.com/64725210/93179181-eefc7200-f6fa-11ea-8c3e-f028dfc54b3d.png)

# Corporate Insider API

The Corporate Insider API is built with Django and PostgreSQL. The database is made up of four models, Review, User (Custom made), Company and Rating. The Ratings and Review Models are linked to the Company and User models with one-to-many relationships.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
You need python version 3 on your machine and you need to install pipenv ( your virtual environment)

```

### Installing

1. Fork and clone this repository.
1. Change into the new directory and create a development branch to work on.

On your terminal,

```
run pipenv install
run pipenv shell to launch your virtual environment
start the server by running python3 manage.py runserver
```

To make sure postgres is running

```
run brew services list to check the status of postgres
```

#### Endpoint to fetch the data of all movies in the database



## API

Sample API Response for a specific company, this endpoind requires an API key

https://corporate-db.herokuapp.com/companies/id/API_KEY

```json
{
        "id": 1,
        "name": "Amazon",
        "domain": "amazon.com",
        "logo": "https://logo.clearbit.com/amazon.com",
        "ratings": [
            {
                "id": 1,
                "rating": 5,
                "user_id": 1,
                "company": "https://corporate-db.herokuapp.com/companies/1/9093388",
                "company_id": 1
            }
        ],
        "reviews": [
            {
                "id": 3,
                "review": "It was great working at amazon, my coworkers were pretty chill.",
                "user_id": 1,
                "company": "https://corporate-db.herokuapp.com/companies/1/9093388",
                "company_id": 1
            },
            {
                "id": 4,
                "review": "Not only is the pay at amazon great, the schedules were fairly flexible, I sure know I enjoyed working there.",
                "user_id": 1,
                "company": "https://corporate-db.herokuapp.com/companies/1/9093388",
                "company_id": 1
            }
        ]
    }
```

## Table of Routes
![Table of Routes](https://user-images.githubusercontent.com/64725210/93184210-967ca300-f701-11ea-8dbb-ab87bfdd04f2.png)


## Deployment

This app is currently running on heroku.

## Contributing

If you want to contribute to this project, you can [submit an issue](https://github.com/Corporate-Insider/corporate_django/issues/) on this repository.

## Versioning

We use [Github](http://github.com) for versioning.

## Acknowledgments

- Materian UI - Edit and Delete Icons
- [Medium](https://medium.com/)
