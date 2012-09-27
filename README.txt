MailChimp Python wrapper for MailChimp API 1.3

[ usage ]
>>> from mailchimp import MailChimp
>>> mailchimp_api = MailChimp('YOUR MAILCHIMP API KEY')
>>> mailchimp_api.ping()
u"Everything's Chimpy!"

[ note ]
API parameters must be passed by name. For example:
>>> mailchimp_api.listMemberInfo(id='YOUR LIST ID', email_address='name@example.com')

Requires Python 2.6 or later.

[ MailChimp API v1.3 documentation ]
http://www.mailchimp.com/api/1.3/
