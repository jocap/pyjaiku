# py-jaiku

## Usage

### Example

    import jaiku
    
    # Initiate
    j = jaiku.API(consumer_key = "something", consumer_secret = "something")
    
    # Get a request token
    auth_url = j.request_token(url=True, perms="delete") # returns URL to Jaiku with request token to authenticate
    
    # redirect to URL ...
    
    # Later, when authenticated
    j.oauth_token() # Sets OAuth tokens for j
    
    # Rock'n'Roll!
    j.username = "username" # sets username
    j.request(method="post", params={"message": "Hello, World!"}) # posts Hello, World!

## Installation

    (sudo) python setup.py install