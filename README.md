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

### Example shell script

    #/usr/bin/env python
    
    import jaiku
    
    j = jaiku.API(consumer_key = "4879279a7e98779b030290a99b00e39a", consumer_secret = "976a4e97649649d9764d9674dd946f17")
    
    auth_url = j.request_token(url=True, perms="read")
    
    print "Please visit %s to authorize." % auth_url
    
    while True:
        answer = raw_input("Have you authorized via the URL above? [y/n] ")
        if answer.strip() == 'y':
            break
    
    j.oauth_token()
    
    print "\nAccess token\n============\nOAuth token: %s\nOAuth token secret: %s\n" % ( j.access_token["oauth_token"], j.access_token["oauth_token_secret"] )
