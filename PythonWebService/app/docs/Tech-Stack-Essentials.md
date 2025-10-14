# What

This is a template project combining **Flask** (with **Jinja2 templates**) and **FastAPI**. The documentation is intended for:

- Users starting with this combination of frameworks for the first time.
- More experienced users returning to Python and Flask/FastAPI after some time.

This file covers some basic principles for the following topics:

1. Jinja2
1. Flask
1. FastAPI

There is also a ***Architecture.md*** document that describes the core, yes architecture of the template project folders and files

<br>

---

## 1 Jinja2

**Jinja2** is a modern, designer-friendly templating language for Python. It is used to generate HTML and other text-based formats, allowing you to separate your application's logic from its presentation. Jinja2 is a standalone templating engine that Flask uses by default, and it gets installed automatically when you install Flask.

1. **Template Inheritance**: Build a base "skeleton" template containing common elements of your site, with blocks that child templates can override.
1. **Template Variables**: Pass variables from Python code to the template to dynamically generate content.
1. **Control Structures**: Supports conditionals and loops to control the flow of template rendering.
1. **Filters**: Transform the output of variables using filters, similar to functions.
1. **Macros**: Reusable template snippets that accept arguments and can be included in multiple templates.

### 1.1 Template Variables

*Sample: base.html*
{% raw %}
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <h1>Hello {{ name }}!</h1>

    {% block content %}     <!-- This block can be overriden by child template!  -->
    {% endblock %}
    
</body>
</html>
```
{% endraw %}

> Python Call : `return render_template('base.html', name=pyVarName,title= pyVarTitle)`

### 1.2 Template Inheritance (Template Extensions)

Using the the same  *base.html* together with the *second.html*

*Sample: second.html*
{% raw %}
``` html
{% extends "base.html" %}

{% block title %}Home - My Website{% endblock %}

{% block content %}
    <h2>Welcome to the Home Page</h2>
    <p>This is the content of the home page.</p>    
{% endblock %}

{{content2Data}}    <!-- This has nothing to do  with block content, just data replacement! -->
```
{% endraw %}

> Python Call :  
>> `return render_template('base.html', name=pyVarName, title=pyVarTitle)`  
>> `return render_template('second.html', title=pyTitle, name=pyName, content2Data=pyContent)`  
>>
>>  \# This is the same, and generally used, if your variables are named like that.  
>> `return render_template('second.html', title=title, name=name, content2Data= content2Data)`
 
><details>  
>  <summary class="clickable-summary">
>  <span  class="summary-icon"></span>
> &nbsp;&nbsp;&nbsp;&nbsp;<b>Note:</b> is twice too much? 
>  </summary>
>I use variable names like `pyTitle` and `pyName` to make it explicit that these are **Python variables** being passed into the template.  
>Most tutorials simplify it and just write:
>> `return render_template('base.html', name=name, title=title)`
>
>But that always made me wonder: why write the same thing twice?  
>It almost looks like you should be able to just write:
>> `return render_template('base.html', name, title)`
>
>(of course you can’t — Flask requires keyword arguments).  
>So yes, `name=name` is a bit redundant. Using `pyVarName` makes the distinction between Python variables and Jinja2 template variables clearer for beginners.
>
</details>

### 1.3 Control Structures & 1.4 filters

Regarding Control Structures the following example
{% raw %}
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Control Structures Example</title>
</head>
<body>
    <h1>Control Structures in Jinja2</h1>

    {% set numbers = [1, 2, 3, 4, 5] %}
    {% set user = {'name': 'Alice', 'age': 30} %}
    {% set messages = ['Hello', 'World', 'Jinja2'] %}

    <h2>For Loop</h2>   <!-- 1. For loop -->
    <ul>
        {% for number in numbers %}
            <li>{{ number }}</li>
        {% endfor %}
    </ul>

    <h2>If-Else</h2>    <!-- 2. If/else -->
    <p>{{ user.name }} is {{ user.age }} years old.</p>
    {% if user.age >= 18 %}
        <p>{{ user.name }} is an adult.</p>
    {% else %}
        <p>{{ user.name }} is not an adult.</p>
    {% endif %}

    <h2>Switch-Case (ternary operator)</h2>     <!-- 3. Ternary 'Switch'  -->
    <p>The first message is: {{ messages[0] }}</p>
    <p>The second message is: {{ messages[1] if len(messages) > 1 else 'No second message' }}</p>

    <h2>Set</h2>
    <p>The value of x is: {{ x | default('undefined') }}</p>    <!--4. Default value -->

    <h2>Length</h2>
    <p>The number of messages is: {{ messages | length }}</p>   <!-- 5. Number of elements      -->
                                                <!-- length is filter others like:               -->
                                                <!-- lower, upper, ... your own contextfilter   --> 
    <h2>Join</h2>
    <p>Messages joined by comma: {{ messages | join(', ') }}</p><!-- 6. Str conversion with, separator -->

    <h2>Loop Else</h2>
    <ul>
        {% for number in numbers %}     <!-- 7. Loop Else  -->
            <li>{{ number }}</li>
        {% else %}
            <li>No numbers found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```
{% endraw %}

<small>

1. For Loop: Iterates over a list of numbers and displays them as list items.
1. If-Else: Checks if a user is an adult based on their age.
1. Switch-Case (ternary operator): Uses a conditional expression to display the second message or a default message.
1. Set: Sets a variable x and uses the default filter to provide a default value if x is undefined.
1. Length: Calculates the length of the messages list.
1. Join: Joins the messages list into a single string separated by commas.
1. Loop Else: Provides an alternative display when the loop doesn't find any items.
</small>

### 1.5 Marcos

A Marco is a kind of **substitution function**, it turns a number of parameters into a more advanced output structure, using the parameters
{% raw %}
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Macro Example</title>
</head>
<body>
    <h1>Macro Example</h1>

    {% macro person(name, age) %}
        <p>{{ name }} is {{ age }} years old.</p>
    {% endmacro %}

    <div>
        {{ person('Alice', 30) }}   <!--Applies the Marco, result: "Alice is 30 years old." -->
        {{ person('Bob', 25) }}
    </div>
</body>
</html>
```
{% endraw %}
---

<br>

## 2 Flask

Flask is a lightweight web framework for Python that provides a simple and flexible way to build web applications. It is designed to be easy to use and customize, allowing developers to create a wide range of applications, from simple static websites to complex dynamic web services. Flask is based on the WSGI (Web Server Gateway Interface) standard and supports a variety of extensions to add functionality, such as authentication, form validation, and database integration. 

We can distinct the following main sections

### 2.1 Core Features of Flask

Always included :

1. **Routing** → Maps URLs to Python functions (view functions), enabling clean and structured web endpoints.
1. **Templates** → Uses the Jinja2 templating engine for rendering dynamic HTML pages with reusable layout

**Common extensions** (not built-in but widely used)

Use **pip** to add these optional **extensions**:

3. **Forms** → Via Flask-WTF, which adds form handling and validation.  
`pip show flask-wtf`
4. **Database integration** → Via extensions like Flask-SQLAlchemy (or direct use of SQLAlchemy), supporting SQLite,MySQL, PostgreSQL, etc.  
`pip show flask-sqlalchemy  # ORM`
5. **Authentication, email**, etc. → **Extensions** like Flask-Login, Flask-Mail, and many more add higher-level features. Examples:  
`pip show flask-login`  
`pip show flask-mail`

### 2.1 Project WorkFlow Architecture Overview (Flask / Jinja2)

How Jinja2 and Flask work together is summarized below.  
For detailed *template project* architecture see the separated document: ***Architecture.md***

**Request Flow (Step by Step):**

1. **Template Generation**: Jinja2 template functions like `{{ url_for('rt_login') }}` generate dynamic **Flask URL routes** (e.g., `/login`)
2. **User Interaction**: User clicks link or submits form to the generated route
3. **Route Handling**: Flask routes the request to the appropriate method in the **AppRoutes** class
4. **Processing**: The `AppRoutes.rt_login()` method processes the request data
5. **Response**: Method calls Jinja2 `render_template()` to substitute variables and generate HTML
6. **Delivery**: The resulting HTML is sent to the browser

**Practical Example:**

```html
<!-- In template: generates /login URL -->
<form action="{{ url_for('rt_login') }}" method="post">
    <input name="nm" type="text" placeholder="Name">
    <button type="submit">Login</button>
</form>
```

```python
# In routes.py: handles the /login route
def rt_login(self):
    if request.method == 'POST':
        user = request.form['nm']
    return self.view.vw_login(self.hostname, user)
```

> **Key Components:**
>
> - **Routes**: `src/routes/app/routes.py` (AppRoutes class) - URL handling
> - **Views**: `src/view/app_view.py` (AppView class) - Template rendering logic  
> - **Templates**: `templates/` directory - HTML with Jinja2 syntax
> - **Logic**: `src/logic/` - Business logic and data processing

---

<br>

## 3 Redis

Redis is an in-memory data structure store that serves as a database, cache, and message broker.

### 3.1 Key Characteristics

1. In-memory: All data stored in RAM for ultra-fast access (microsecond latency)
1. Persistent: **Optional** disk persistence to survive restarts (NOT enabled by default - must be configured)

    - Configure in: `/etc/redis/redis.conf`

      ``` text
        save 900 1      # 1      key saved in 15 min
        save 300 10     # 10     keys saved in 5 min
        save 60 10000   # 10000  keys saved in 1 min

        # Save location: `/var/lib/redis/dump.rdb`
      ```

1. Key-value: Data organized as key-value pairs
1. Data structures: Supports strings, lists, sets, hashes, streams, and more
1. Single-threaded: Uses event loop for high performance without locks
1. Network accessible: Multiple clients can connect simultaneously
1. Primary Use Cases:

- Caching - Store frequently accessed data for fast retrieval
- Session storage - Web application user sessions
- Real-time analytics - Counters, leaderboards, metrics (like your hit counter)
- Message queues - Pub/sub messaging between services
- Rate limiting - Track API usage, login attempts

### 3.2 Commands

| Redis CLI Command | Python redis-py Method | Description |
|------------------|------------------------|-------------|
| `SET key value` | `redis_client.set('key', 'value')` | Set key to hold string value |
| `GET key` | `redis_client.get('key')` | Get the value of key |
| `DEL key` | `redis_client.delete('key')` | Delete a key |
| `EXISTS key` | `redis_client.exists('key')` | Check if key exists |
| `KEYS *` | `redis_client.keys('*')` | Find all keys matching pattern |
| `FLUSHALL` | `redis_client.flushall()` | Remove all keys from all databases |
| `TTL key` | `redis_client.ttl('key')` | Get time to live for key |
| `EXPIRE key seconds` | `redis_client.expire('key', seconds)` | Set timeout on key |
| `SETEX key seconds value` | `redis_client.setex('key', seconds, 'value')` | Set key with expiration |
| `INCR key` | `redis_client.incr('key')` | Increment integer value of key by 1 |
| `DECR key` | `redis_client.decr('key')` | Decrement integer value of key by 1 |
| `LPUSH key value` | `redis_client.lpush('key', 'value')` | Prepend value to list |
| `RPUSH key value` | `redis_client.rpush('key', 'value')` | Append value to list |
| `LRANGE key start stop` | `redis_client.lrange('key', start, stop)` | Get range of elements from list |
| `LPOP key` | `redis_client.lpop('key')` | Remove and return first element |
| `RPOP key` | `redis_client.rpop('key')` | Remove and return last element |
| `SADD key member` | `redis_client.sadd('key', 'member')` | Add member to set |
| `SMEMBERS key` | `redis_client.smembers('key')` | Get all members of set |
| `SREM key member` | `redis_client.srem('key', 'member')` | Remove member from set |
| `HSET key field value` | `redis_client.hset('key', 'field', 'value')` | Set field in hash |
| `HGET key field` | `redis_client.hget('key', 'field')` | Get field value from hash |
| `HGETALL key` | `redis_client.hgetall('key')` | Get all fields and values from hash |
| `HDEL key field` | `redis_client.hdel('key', 'field')` | Delete field from hash |
| `HEXISTS key field` | `redis_client.hexists('key', 'field')` | Check if field exists in hash |

### 3.3 Advanced Commands

| Redis CLI Command | Python redis-py Method | Description |
|------------------|------------------------|-------------|
| `MSET key1 val1 key2 val2` | `redis_client.mset({'key1': 'val1', 'key2': 'val2'})` | Set multiple keys at once |
| `MGET key1 key2` | `redis_client.mget(['key1', 'key2'])` | Get multiple keys at once |
| `INCRBY key amount` | `redis_client.incrby('key', amount)` | Increment by specific amount |
| `DECRBY key amount` | `redis_client.decrby('key', amount)` | Decrement by specific amount |
| `INCRBYFLOAT key amount` | `redis_client.incrbyfloat('key', amount)` | Increment by float amount |
| `APPEND key value` | `redis_client.append('key', 'value')` | Append value to existing string |
| `STRLEN key` | `redis_client.strlen('key')` | Get length of string value |
| `SETRANGE key offset value` | `redis_client.setrange('key', offset, 'value')` | Overwrite part of string at offset |
| `GETRANGE key start end` | `redis_client.getrange('key', start, end)` | Get substring by range |
| `SETNX key value` | `redis_client.setnx('key', 'value')` | Set only if key doesn't exist |
| `GETSET key value` | `redis_client.getset('key', 'value')` | Set key and return old value |
| `LLEN key` | `redis_client.llen('key')` | Get length of list |
| `LINDEX key index` | `redis_client.lindex('key', index)` | Get element at index in list |
| `LSET key index value` | `redis_client.lset('key', index, 'value')` | Set element at index in list |
| `LTRIM key start stop` | `redis_client.ltrim('key', start, stop)` | Trim list to specified range |
| `SCARD key` | `redis_client.scard('key')` | Get number of members in set |
| `SINTER key1 key2` | `redis_client.sinter(['key1', 'key2'])` | Intersection of sets |
| `SUNION key1 key2` | `redis_client.sunion(['key1', 'key2'])` | Union of sets |
| `SDIFF key1 key2` | `redis_client.sdiff(['key1', 'key2'])` | Difference of sets |
| `SISMEMBER key member` | `redis_client.sismember('key', 'member')` | Check if member exists in set |
| `HLEN key` | `redis_client.hlen('key')` | Get number of fields in hash |
| `HKEYS key` | `redis_client.hkeys('key')` | Get all field names in hash |
| `HVALS key` | `redis_client.hvals('key')` | Get all values in hash |
| `HINCRBY key field amount` | `redis_client.hincrby('key', 'field', amount)` | Increment hash field by amount |
| `ZSCORE key member` | `redis_client.zscore('key', 'member')` | Get score of member in sorted set |
| `ZRANGE key start stop` | `redis_client.zrange('key', start, stop)` | Get range from sorted set |
| `ZRANK key member` | `redis_client.zrank('key', 'member')` | Get rank of member in sorted set |
| `ZADD key score member` | `redis_client.zadd('key', {'member': score})` | Add member to sorted set with score |
| `PUBLISH channel message` | `redis_client.publish('channel', 'message')` | Publish message to channel |
| `SUBSCRIBE channel` | `redis_client.pubsub().subscribe('channel')` | Subscribe to channel |
| `EVAL script numkeys key` | `redis_client.eval('script', numkeys, 'key')` | Execute Lua script |
| `SCAN cursor` | `redis_client.scan(cursor)` | Iterate over keys incrementally |
| `HSCAN key cursor` | `redis_client.hscan('key', cursor)` | Iterate over hash fields |
| `SSCAN key cursor` | `redis_client.sscan('key', cursor)` | Iterate over set members |
| `ZSCAN key cursor` | `redis_client.zscan('key', cursor)` | Iterate over sorted set members |
| `MONITOR` | `redis_client.monitor()` | Monitor all commands in real-time |
| `INFO` | `redis_client.info()` | Get server information and statistics |
| `CONFIG GET parameter` | `redis_client.config_get('parameter')` | Get configuration parameter |
| `FLUSHDB` | `redis_client.flushdb()` | Remove all keys from current database |

---

<br>

## 4 Fast-API

**FastAPI** is a modern, high-performance web framework for building APIs with Python based on standard Python type hints. It's designed to be fast (comparable to NodeJS and Go), easy to use, and automatically generates interactive API documentation.

**Key Features:**

- **Fast performance** - One of the fastest Python frameworks available
- **Type safety** - Uses Python type hints for automatic data validation and serialization
- **Auto-documentation** - Generates interactive API docs (Swagger UI) automatically
- **Modern Python** - Built for Python 3.7+ with full async/await support
- **Standards-based** - Based on OpenAPI and JSON Schema standards

*Note: FastAPI integration is planned for this template but not yet implemented.*

### 4.1 Use Cases & characteristics

1. **RESTful APIs**: FastAPI is commonly used to build **RESTful APIs** due to its support for **standard HTTP methods** (GET, POST, PUT, DELETE) and its ability to handle different types of request bodies (JSON, form data, etc.).

1. **OpenAPI** and **GraphQL**: In addition to REST, FastAPI supports OpenAPI (formerly known as *Swagger*) for API documentation and interactive API testing. It also supports **GraphQL*, allowing you to create APIs that can serve both REST and GraphQL requests.

1. **Performance**: FastAPI is designed to be fast and efficient, making it suitable for building high-performance APIs.

1. **Asynchronous Support**: FastAPI supports asynchronous request handling, which can be beneficial for I/O-bound operations like database queries or external API calls.

1. **Automatic Documentation**: FastAPI automatically generates interactive API documentation using OpenAPI and JSON Schema, making it easier for developers to understand and test the API.

1. **Type Checking**: FastAPI leverages Python type hints for input validation and serialization, reducing the need for manual data validation and making the code more robust.

---

<br>

## 5 Python, a few general recommandations

This section covers key Python concepts used in this Flask/FastAPI template. For comprehensive Python documentation, see the [official Python docs](https://docs.python.org/3/) and [Real Python tutorials](https://realpython.com/).

### 5.1 Imports

Python's import system allows you to use code from other modules and packages. Here are the common patterns used in this template:

**1. Basic imports:**

``` python
import os              # Standard library module
import time            # Another standard library module
```

**2. From imports (selective):**

```python
from flask import Flask, render_template, request
# Imports specific classes/functions from Flask

from config.app_system import app
# Import specific items from local modules
```

**3. Module imports with qualification:**

```python
import config.app_system
# Import whole module. Access with: config.app_system.app

import config.app_system as app_sys
# Import whole module with alias. Access with: app_sys.app
```

<br> <br>
---