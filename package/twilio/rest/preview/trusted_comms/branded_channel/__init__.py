# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.preview.trusted_comms.branded_channel.channel import ChannelList


class BrandedChannelList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the BrandedChannelList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelList
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelList
        """
        super(BrandedChannelList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, sid):
        """
        Constructs a BrandedChannelContext

        :param sid: Branded Channel Sid.

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        """
        return BrandedChannelContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a BrandedChannelContext

        :param sid: Branded Channel Sid.

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        """
        return BrandedChannelContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BrandedChannelList>'


class BrandedChannelPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the BrandedChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelPage
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelPage
        """
        super(BrandedChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BrandedChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        """
        return BrandedChannelInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.BrandedChannelPage>'


class BrandedChannelContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the BrandedChannelContext

        :param Version version: Version that contains the resource
        :param sid: Branded Channel Sid.

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        """
        super(BrandedChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/BrandedChannels/{sid}'.format(**self._solution)

        # Dependents
        self._channels = None

    def fetch(self):
        """
        Fetch the BrandedChannelInstance

        :returns: The fetched BrandedChannelInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BrandedChannelInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.preview.trusted_comms.branded_channel.channel.ChannelList
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.channel.ChannelList
        """
        if self._channels is None:
            self._channels = ChannelList(self._version, branded_channel_sid=self._solution['sid'], )
        return self._channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.BrandedChannelContext {}>'.format(context)


class BrandedChannelInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the BrandedChannelInstance

        :returns: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        """
        super(BrandedChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'business_sid': payload.get('business_sid'),
            'brand_sid': payload.get('brand_sid'),
            'sid': payload.get('sid'),
            'links': payload.get('links'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: BrandedChannelContext for this BrandedChannelInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelContext
        """
        if self._context is None:
            self._context = BrandedChannelContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def business_sid(self):
        """
        :returns: Business Sid.
        :rtype: unicode
        """
        return self._properties['business_sid']

    @property
    def brand_sid(self):
        """
        :returns: Brand Sid.
        :rtype: unicode
        """
        return self._properties['brand_sid']

    @property
    def sid(self):
        """
        :returns: Branded Channel Sid.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the BrandedChannelInstance

        :returns: The fetched BrandedChannelInstance
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.BrandedChannelInstance
        """
        return self._proxy.fetch()

    @property
    def channels(self):
        """
        Access the channels

        :returns: twilio.rest.preview.trusted_comms.branded_channel.channel.ChannelList
        :rtype: twilio.rest.preview.trusted_comms.branded_channel.channel.ChannelList
        """
        return self._proxy.channels

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.BrandedChannelInstance {}>'.format(context)
