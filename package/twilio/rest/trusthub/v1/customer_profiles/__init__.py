# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment import CustomerProfilesChannelEndpointAssignmentList
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments import CustomerProfilesEntityAssignmentsList
from twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations import CustomerProfilesEvaluationsList


class CustomerProfilesList(ListResource):

    def __init__(self, version):
        """
        Initialize the CustomerProfilesList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesList
        """
        super(CustomerProfilesList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/CustomerProfiles'.format(**self._solution)

    def create(self, friendly_name, email, policy_sid,
               status_callback=values.unset):
        """
        Create the CustomerProfilesInstance

        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode email: The email address
        :param unicode policy_sid: The unique string of a policy.
        :param unicode status_callback: The URL we call to inform your application of status changes.

        :returns: The created CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Email': email,
            'PolicySid': policy_sid,
            'StatusCallback': status_callback,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return CustomerProfilesInstance(self._version, payload, )

    def stream(self, status=values.unset, friendly_name=values.unset,
               policy_sid=values.unset, limit=None, page_size=None):
        """
        Streams CustomerProfilesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param CustomerProfilesInstance.Status status: The verification status of the Customer-Profile resource
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode policy_sid: The unique string of a policy.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, friendly_name=values.unset,
             policy_sid=values.unset, limit=None, page_size=None):
        """
        Lists CustomerProfilesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param CustomerProfilesInstance.Status status: The verification status of the Customer-Profile resource
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode policy_sid: The unique string of a policy.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance]
        """
        return list(self.stream(
            status=status,
            friendly_name=friendly_name,
            policy_sid=policy_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, friendly_name=values.unset,
             policy_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CustomerProfilesInstance records from the API.
        Request is executed immediately

        :param CustomerProfilesInstance.Status status: The verification status of the Customer-Profile resource
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode policy_sid: The unique string of a policy.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesPage
        """
        data = values.of({
            'Status': status,
            'FriendlyName': friendly_name,
            'PolicySid': policy_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return CustomerProfilesPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CustomerProfilesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CustomerProfilesPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CustomerProfilesContext

        :param sid: The unique string that identifies the resource.

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        """
        return CustomerProfilesContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CustomerProfilesContext

        :param sid: The unique string that identifies the resource.

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        """
        return CustomerProfilesContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesList>'


class CustomerProfilesPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CustomerProfilesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesPage
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesPage
        """
        super(CustomerProfilesPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CustomerProfilesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        return CustomerProfilesInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesPage>'


class CustomerProfilesContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the CustomerProfilesContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the resource.

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        """
        super(CustomerProfilesContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/CustomerProfiles/{sid}'.format(**self._solution)

        # Dependents
        self._customer_profiles_entity_assignments = None
        self._customer_profiles_evaluations = None
        self._customer_profiles_channel_endpoint_assignment = None

    def fetch(self):
        """
        Fetch the CustomerProfilesInstance

        :returns: The fetched CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CustomerProfilesInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, status=values.unset, status_callback=values.unset,
               friendly_name=values.unset, email=values.unset):
        """
        Update the CustomerProfilesInstance

        :param CustomerProfilesInstance.Status status: The verification status of the Customer-Profile resource
        :param unicode status_callback: The URL we call to inform your application of status changes.
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode email: The email address

        :returns: The updated CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        data = values.of({
            'Status': status,
            'StatusCallback': status_callback,
            'FriendlyName': friendly_name,
            'Email': email,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return CustomerProfilesInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the CustomerProfilesInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def customer_profiles_entity_assignments(self):
        """
        Access the customer_profiles_entity_assignments

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        """
        if self._customer_profiles_entity_assignments is None:
            self._customer_profiles_entity_assignments = CustomerProfilesEntityAssignmentsList(
                self._version,
                customer_profile_sid=self._solution['sid'],
            )
        return self._customer_profiles_entity_assignments

    @property
    def customer_profiles_evaluations(self):
        """
        Access the customer_profiles_evaluations

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        """
        if self._customer_profiles_evaluations is None:
            self._customer_profiles_evaluations = CustomerProfilesEvaluationsList(
                self._version,
                customer_profile_sid=self._solution['sid'],
            )
        return self._customer_profiles_evaluations

    @property
    def customer_profiles_channel_endpoint_assignment(self):
        """
        Access the customer_profiles_channel_endpoint_assignment

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment.CustomerProfilesChannelEndpointAssignmentList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment.CustomerProfilesChannelEndpointAssignmentList
        """
        if self._customer_profiles_channel_endpoint_assignment is None:
            self._customer_profiles_channel_endpoint_assignment = CustomerProfilesChannelEndpointAssignmentList(
                self._version,
                customer_profile_sid=self._solution['sid'],
            )
        return self._customer_profiles_channel_endpoint_assignment

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesContext {}>'.format(context)


class CustomerProfilesInstance(InstanceResource):

    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"

    class EndUserType(object):
        INDIVIDUAL = "individual"
        BUSINESS = "business"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CustomerProfilesInstance

        :returns: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        super(CustomerProfilesInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'policy_sid': payload.get('policy_sid'),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'valid_until': deserialize.iso8601_datetime(payload.get('valid_until')),
            'email': payload.get('email'),
            'status_callback': payload.get('status_callback'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CustomerProfilesContext for this CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesContext
        """
        if self._context is None:
            self._context = CustomerProfilesContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def policy_sid(self):
        """
        :returns: The unique string of a policy.
        :rtype: unicode
        """
        return self._properties['policy_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def status(self):
        """
        :returns: The verification status of the Customer-Profile resource
        :rtype: CustomerProfilesInstance.Status
        """
        return self._properties['status']

    @property
    def valid_until(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource will be valid until.
        :rtype: datetime
        """
        return self._properties['valid_until']

    @property
    def email(self):
        """
        :returns: The email address
        :rtype: unicode
        """
        return self._properties['email']

    @property
    def status_callback(self):
        """
        :returns: The URL we call to inform your application of status changes.
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Customer-Profile resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of the Assigned Items of the Customer-Profile resource
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the CustomerProfilesInstance

        :returns: The fetched CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        return self._proxy.fetch()

    def update(self, status=values.unset, status_callback=values.unset,
               friendly_name=values.unset, email=values.unset):
        """
        Update the CustomerProfilesInstance

        :param CustomerProfilesInstance.Status status: The verification status of the Customer-Profile resource
        :param unicode status_callback: The URL we call to inform your application of status changes.
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode email: The email address

        :returns: The updated CustomerProfilesInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.CustomerProfilesInstance
        """
        return self._proxy.update(
            status=status,
            status_callback=status_callback,
            friendly_name=friendly_name,
            email=email,
        )

    def delete(self):
        """
        Deletes the CustomerProfilesInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def customer_profiles_entity_assignments(self):
        """
        Access the customer_profiles_entity_assignments

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        """
        return self._proxy.customer_profiles_entity_assignments

    @property
    def customer_profiles_evaluations(self):
        """
        Access the customer_profiles_evaluations

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        """
        return self._proxy.customer_profiles_evaluations

    @property
    def customer_profiles_channel_endpoint_assignment(self):
        """
        Access the customer_profiles_channel_endpoint_assignment

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment.CustomerProfilesChannelEndpointAssignmentList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_channel_endpoint_assignment.CustomerProfilesChannelEndpointAssignmentList
        """
        return self._proxy.customer_profiles_channel_endpoint_assignment

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesInstance {}>'.format(context)
