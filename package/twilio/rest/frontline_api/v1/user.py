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


class UserList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.frontline_api.v1.user.UserList
        :rtype: twilio.rest.frontline_api.v1.user.UserList
        """
        super(UserList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, sid):
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FrontlineApi.V1.UserList>'


class UserPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.frontline_api.v1.user.UserPage
        :rtype: twilio.rest.frontline_api.v1.user.UserPage
        """
        super(UserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.frontline_api.v1.user.UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        return UserInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FrontlineApi.V1.UserPage>'


class UserContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.frontline_api.v1.user.UserContext
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        super(UserContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Users/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the UserInstance

        :returns: The fetched UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, friendly_name=values.unset, avatar=values.unset,
               state=values.unset, is_available=values.unset):
        """
        Update the UserInstance

        :param unicode friendly_name: The string that you assigned to describe the User
        :param unicode avatar: The avatar URL which will be shown in Frontline application
        :param UserInstance.StateType state: Current state of this user
        :param bool is_available: Whether the User is available for new conversations

        :returns: The updated UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Avatar': avatar,
            'State': state,
            'IsAvailable': is_available,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return UserInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FrontlineApi.V1.UserContext {}>'.format(context)


class UserInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class StateType(object):
        ACTIVE = "active"
        DEACTIVATED = "deactivated"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the UserInstance

        :returns: twilio.rest.frontline_api.v1.user.UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        super(UserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'identity': payload.get('identity'),
            'friendly_name': payload.get('friendly_name'),
            'avatar': payload.get('avatar'),
            'state': payload.get('state'),
            'is_available': payload.get('is_available'),
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

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the User
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def avatar(self):
        """
        :returns: The avatar URL which will be shown in Frontline application
        :rtype: unicode
        """
        return self._properties['avatar']

    @property
    def state(self):
        """
        :returns: Current state of this user
        :rtype: UserInstance.StateType
        """
        return self._properties['state']

    @property
    def is_available(self):
        """
        :returns: Whether the User is available for new conversations
        :rtype: bool
        """
        return self._properties['is_available']

    @property
    def url(self):
        """
        :returns: An absolute URL for this user.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the UserInstance

        :returns: The fetched UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, avatar=values.unset,
               state=values.unset, is_available=values.unset):
        """
        Update the UserInstance

        :param unicode friendly_name: The string that you assigned to describe the User
        :param unicode avatar: The avatar URL which will be shown in Frontline application
        :param UserInstance.StateType state: Current state of this user
        :param bool is_available: Whether the User is available for new conversations

        :returns: The updated UserInstance
        :rtype: twilio.rest.frontline_api.v1.user.UserInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            avatar=avatar,
            state=state,
            is_available=is_available,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FrontlineApi.V1.UserInstance {}>'.format(context)
