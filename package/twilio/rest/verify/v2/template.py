# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TemplateList(ListResource):

    def __init__(self, version):
        """
        Initialize the TemplateList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.template.TemplateList
        :rtype: twilio.rest.verify.v2.template.TemplateList
        """
        super(TemplateList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Templates'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams TemplateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: Filter templates using friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(friendly_name=friendly_name, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists TemplateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: Filter templates using friendly name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.template.TemplateInstance]
        """
        return list(self.stream(friendly_name=friendly_name, limit=limit, page_size=page_size, ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TemplateInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter templates using friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return TemplatePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TemplateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return TemplatePage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.TemplateList>'


class TemplatePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TemplatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.template.TemplatePage
        :rtype: twilio.rest.verify.v2.template.TemplatePage
        """
        super(TemplatePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TemplateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.template.TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplateInstance
        """
        return TemplateInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.TemplatePage>'


class TemplateInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the TemplateInstance

        :returns: twilio.rest.verify.v2.template.TemplateInstance
        :rtype: twilio.rest.verify.v2.template.TemplateInstance
        """
        super(TemplateInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'translations': payload.get('translations'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Template
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A string to describe the verification template
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def translations(self):
        """
        :returns: Ojbect with the template translations.
        :rtype: dict
        """
        return self._properties['translations']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.TemplateInstance>'
