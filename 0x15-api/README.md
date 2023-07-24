# API - Application Programming Interface

> about: `API`, Microservices, `CSV/JSON` formatting, Scripting etc  
>> Relevant in various differing context where bash scripting may be ineficient e.g. system administration, especially in SRE (Site Reliability Engineering). This emphasizes on you being open to being well-versed in various programming languages, including Python, which allows them to efficiently manage systems and build APIs and to interact with them.


## What an API IS
> One Reason for API necessity, among other things:  
>> shell scripting doesn't have exceptions or decent data structures - shell scripting is ugly; e.g if working on patch-work, and debugging :)

`API` stands for *Application Programming Interface*. It defines a set of rules and protocols that allows different software applications to communicate and interact with each other. One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data


## What a RESTful API IS

***REST (Representational State Transfer)*** is an architectural style used in APIs. It uses standard HTTP methods to perform CRUD (Create, Read, Update, Delete) operations on resources. REST is the most popular API architecture for transferring data over the internet. In a RESTful context, resources are accessible via endpoints, and operations are performed on those resources with standard HTTP methods such as GET, POST, PUT, and DELETE.

### REST principles

```bash
- Uniform Interface: Every rest architecture must have a standardized way of accessing and processing data resources. This includes unique resource identifiers (i.e., unique URLs) and self-descriptive messages in the server response that describe how to process the representation (for instance JSON vs XML) of the data resource.

- Stateless: Every client request is self-contained in that the server doesn't need to store any application data in order to respond to subsequent requests

- Client-Server: There must be both a client and server in the architecture

- Cacheable & Layered System: Caching and layering increases networking efficiency
```


## Microservices

Microservices is an architectural style that structures an application as a collection of loosely coupled services. Each service represents a single piece of functionality, making the application easier to develop and maintain.


## `CSV/JSON` formatting:

*CSV* (Comma-Separated Values) is a simple file format used to store tabular data, where each line represents a row and fields are separated by commas. *JSON* (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write and easy for machines to parse and generate.


---
## API Usage:

### Example 1 - Get Employee Data

```python
import requests

url = "https://api.example.com/employees"
response = requests.get(url)

if response.status_code == 200:
    employee_data = response.json()
    print(employee_data)
else:
    print("Failed to retrieve employee data.")
```

### Example 2 - Interacting With API Endpoints in Command-line

```bash
# DELETE a question using a an ID passed in as a URL parameter '/questions/${id}'
$ curl -X DELETE http://127.0.0.1:5000/questions/27
$
{
  "deleted": 27,
  "success": true
}
$
```

### Example 3 - Export Data to CSV

```python
import csv

employee_data = [
    {"id": 1, "name": "John Doe", "position/Affiliation": "Manager", "salary": 90000},
    {"id": 2, "name": "Levi Ackerman", "position/Affiliation": "Survey Corp", "salary": 65000},
    {"id": 3, "name": "Bob Johnson", "position": "Designer/Affiliation", "salary": 60000}
]

csv_file = 'employee_data.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "position/Affiliation", "salary"])
    writer.writeheader()
    writer.writerows(employee_data)

print("Data exported to CSV successfully.")
```

### References:

> - More information on API - [PokeAPI](https://pokeapi.co/docs/v2) [probably a useful resource]
> - [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api)
> - [Spotify API](https://developer.spotify.com/documentation/web-api)
> - What an API IS - [postman](https://www.postman.com/what-is-an-api/)
> - [Roy Fielding in 2000 - RESTful API architecture](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf)
> - [Stackoverflow - Best practices for REST API design](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
> - [Stackoverflow - What exactly is RESTful programming?](https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)
> - [GitHub REST API](https://docs.github.com/en/rest/quickstart?apiVersion=2022-11-28)
