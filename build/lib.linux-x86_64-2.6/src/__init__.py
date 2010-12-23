class API:
  
  consumer_key = ''
  consumer_secret = ''
  request_token = ''
  access_token = ''
  client = ''
  consumer = ''
  request_token_url = 'http://api.jaiku.com/request_token'
  access_token_url = 'http://api.jaiku.com/access_token'
  authorize_url = 'http://jaiku.com/api/authorize'
  
  def __init__(self, consumer_key, consumer_secret):
    import urlparse
    try:
      import oauth2 as oauth
    except ImportError:
      raise Exception("Install oauth2 from https://github.com/simplegeo/python-oauth2.")
      
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    
    self.consumer = oauth.Consumer(self.consumer_key,
                                   self.consumer_secret)
    self.client = oauth.Client(self.consumer)
  
  def request_token(self, url=None, perms=None, callback=""):
    # Please only use this once per class instance. Otherwise, 
    # a TypeError will occour.
    import urlparse
    import oauth2 as oauth
    
    if perms is None:
      perms = "read"
      print "Choose either read, write or delete for permissions. Using 'read'."
    
    # Get temporary request token
    resp, content = self.client.request(self.request_token_url, "GET")
    if resp['status'] != '200':
      raise Exception("Invalid response %s. Is %s down?" % (resp['status'], self.request_token_url) )
    
    self.request_token = dict( urlparse.parse_qsl(content) )
    
    try:
      if url is None:
        return { "request_token"        : self.request_token['oauth_token'],
                 "request_token_secret" : self.request_token['oauth_token_secret'] }
      else:
        return "%s?oauth_token=%s&perms=delete&oauth_callback=%s&perms=%s" % (self.authorize_url,
                                                                              self.request_token['oauth_token'],
                                                                              callback,
                                                                              perms)
    except KeyError:
      raise Exception("Request tokens not properly set. Is probably due to invalid consumer keys.")
  
  def oauth_token(self, req_token="", req_secret=""):
    import urlparse
    import oauth2 as oauth
    
    # Request the access token
    try:
      token = oauth.Token(self.request_token['oauth_token'] or req_token,
                          self.request_token['oauth_token_secret'] or req_secret)
      self.client = oauth.Client(self.consumer, token)
    except TypeError:
      raise Exception("Invalid request tokens.\nPlease set request tokens (request_token) first, or pass as arguments.")
    
    resp, content = self.client.request(self.access_token_url, "POST")
    self.access_token = dict(urlparse.parse_qsl(content))
    try:
      return { "oauth_token"        : self.access_token['oauth_token'],
               "oauth_token_secret" : self.access_token['oauth_token_secret'] }
    except KeyError:
      raise Exception("OAuth tokens not properly set. Have you authenticated with the Jaiku API?")
  
  def request(self, method, params=None, username=None):
    import urllib2
    from oauth import oauth
    
    if username is None:
      username = self.username or ""
    
    access_token = oauth.OAuthToken(self.access_token["oauth_token"], self.access_token["oauth_token_secret"])
    parameters = {'nick': username, 'method': method}
    
    if params is not None:
      parameters.update(params)
    
    request = oauth.OAuthRequest.from_consumer_and_token(
      oauth_consumer=self.consumer,
      token=access_token,
      http_url='http://api.jaiku.com/json',
      http_method='POST',
       parameters=parameters)
    request.sign_request(
      oauth.OAuthSignatureMethod_HMAC_SHA1(),
      self.consumer,
      access_token)
    result = urllib2.urlopen(urllib2.Request(
      'http://api.jaiku.com/json',
       request.to_postdata()))
    
    return result.read()
    result.close()