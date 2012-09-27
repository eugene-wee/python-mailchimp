import urllib2
try:
    import simplejson as json
    assert json  # Silence potential warnings from static analysis tools
except ImportError:
    import json


class MailChimpError(Exception):
    def __init__(self, error, code=None):
        self.error = error
        self.code = code
        if self.code is not None:
            try:
                self.code = int(self.code)
            except ValueError:
                pass

    def __unicode__(self):
        if self.code is None:
            message = self.error
        else:
            message = u"{error} ({code})".format(error=self.error,
                                                 code=self.code)
        return u"MailChimpError({message})".format(message=message)

    def __str__(self):
        return unicode(self).encode("utf8")

    def __repr__(self):
        return str(self)


class MailChimp(object):
    def __init__(self, apikey='', extra_params={}):
        """
            Cache API key and address.
        """
        self.apikey = apikey

        self.default_params = {"apikey": apikey}
        self.default_params.update(extra_params)

        dc = "us1"
        if "-" in self.apikey:
            dc = self.apikey.split('-')[1]
        self.base_api_url = "https://%s.api.mailchimp.com/1.3/?method=" % dc

    def call(self, method, params={}):
        url = self.base_api_url + method
        all_params = self.default_params.copy()
        all_params.update(params)

        post_data = urllib2.quote(json.dumps(all_params))
        headers = {"Content-Type": "application/json"}
        try:
            request = urllib2.Request(url, post_data, headers)
            response = urllib2.urlopen(request)
            response_content = response.read()
        except urllib2.HTTPError as e:
            raise MailChimpError("HTTP {code}".format(code=e.code))

        result = json.loads(response_content)
        if isinstance(result, dict) and "code" in result and "error" in result:
            raise MailChimpError(error=result["error"], code=result["code"])
        return result

    def __getattr__(self, method_name):

        def get(self, *args, **kwargs):
            params = dict((i, j) for (i, j) in enumerate(args))
            params.update(kwargs)
            return self.call(method_name, params)

        return get.__get__(self)
