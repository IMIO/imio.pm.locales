README.txt
==========

Presentation :
--------------
This extension for Products.PloneMeeting add SOAP access to the application :

1) Create a new item
2) Get information about an existing item
3) Search for items
4) Test with a SOAP client

The WSDL describing the SOAP service is available when the package is installed in a Plone Site by accessing "http://my_site_url/ws4pm.wsdl"

1) Create a new item
--------------------

The 'create_item(string:meetingConfigId, string:proposingGroupId, structType:data)' method can be accessed to create an item in the application.

This method must be accessed with a PloneMeeting application connected user.

string:meetingConfigId is the identifier of the meetingConfig where we will create the item.  There can be several different meeting configuration in a PloneMeeting site.
string:proposingGroupId is the identifier of the group the item will be created for.  The connected user must be selected as creator for this proposingGroup in the PloneMeeting configuration.
structType:data is a complex type representing the data used to create the item.  data can contains every field available on the item.  Most often used fields are 'title', 'description' and 'decision'

A special attribute called 'externalIdentifier' can be used to specify a key coming from the appealing application

As usual, you have to escape HTML special chars when using XML.  So <p> becomes &lt;p&gt;  You can use http://escapehtmlforxml.com/ for tests purpose

Let's say we have a PloneMeeting instance running on http://my_site_url.  The sent SOAP enveloppe should looks like this :

*** Outgoing SOAP ******************************************************
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:xsd="http://www.w3.org/1999/XMLSchema"
  xmlns:ws4="http://ws4pm.communesplone.org">
<SOAP-ENV:Body>
      <ws4:createItemRequest>
         <meetingConfigId>meeting-config-foo</meetingConfigId>
         <proposingGroupId>developers</proposingGroupId>
         <creationData>
            <title>Item created using SOAP</title>
            <description>&lt;p&gt;My description&lt;/p&gt;</description>
            <decision>&lt;p&gt;My decision&lt;/p&gt;</decision>
         </creationData>
      </ws4:createItemRequest>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************

If something is wrong, a SOAP envelope containing the error message is returned :

*** Incoming SOAP ******************************************************
<SOAP-ENV:Envelope xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:ZSI="http://www.zolera.com/schemas/ZSI/"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <SOAP-ENV:Header/>
   <SOAP-ENV:Body>
      <SOAP-ENV:Fault>
         <faultcode>SOAP-ENV:Client</faultcode>
         <faultstring>Unknown meetingConfigId : 'meeting-config-foo'!</faultstring>
      </SOAP-ENV:Fault>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************

If everything is right, the freshly created item UID is returned :

*** Incoming SOAP ******************************************************
<SOAP-ENV:Envelope xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" 
                   xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:ZSI="http://www.zolera.com/schemas/ZSI/"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <SOAP-ENV:Header/>
   <SOAP-ENV:Body xmlns:ns1="http://ws4pm.communesplone.org">
      <ns1:createItemResponse>
         <itemUID>952a253442ac649d5465bf72ad0ff83c</itemUID>
      </ns1:createItemResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************


2) Get information on an existing item
--------------------------------------

The 'getItemInfos(string:itemUID)' method can be accessed to get informations about an existing item in the application.

This method must be accessed with a PloneMeeting application connected user.

string:itemUID is the unique identifier of the item to get informations from.  The UID is unique in the application so getting an item using his UID will return a maximum of 1 item

Ths UID is something like : 37be48be730f1b9e94c322a571e9d0f7

The sent SOAP enveloppe should looks like this :

*** Outgoing SOAP ******************************************************
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:xsd="http://www.w3.org/1999/XMLSchema"
  xmlns:ws4="http://ws4pm.communesplone.org">
<SOAP-ENV:Body>
      <ws4:getItemInfosRequest>
         <itemUID>anUidOfAnExistingItemHopefully</itemUID>
         <showExtraInfos>0</showExtraInfos>
         <showAnnexes>0</showAnnexes>
      </ws4:getItemInfosRequest>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************

If 'showExtraInfos' is '1', every available fields are returned, if 'showAnnexes' is '1', item annexes are returned too.

If something is wrong, a SOAP envelope containing the error message is returned :

*** Incoming SOAP ******************************************************
<SOAP-ENV:Envelope xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:ZSI="http://www.zolera.com/schemas/ZSI/"
  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<SOAP-ENV:Header></SOAP-ENV:Header>
<SOAP-ENV:Body>
<SOAP-ENV:Fault>
<faultcode>SOAP-ENV:Client</faultcode>
<faultstring>Given UID 'anUidOfAnExistingItemHopefully' does not correspond to any item the currently logged in user 'pmManager' can access!</faultstring>
</SOAP-ENV:Fault>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************

If everything is right, the basic informations about the searched item are returned :

*** Incoming SOAP ******************************************************
<SOAP-ENV:Envelope xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
                   xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
                   xmlns:ZSI="http://www.zolera.com/schemas/ZSI/"
                   xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
   <SOAP-ENV:Header/>
   <SOAP-ENV:Body xmlns:ns1="http://ws4pm.communesplone.org">
      <ns1:getItemInfosResponse>
         <itemInfo xsi:type="ns1:ItemInfo">
            <UID>37be48be730f1b9e94c322a571e9d0f7</UID>
            <id>title-of-my-item</id>
            <title>Title of my item</title>
            <category>item-category</category>
            <description>&lt;p>Description with escaped HTML special characters&lt;/p></description>
            <decision>&lt;p>Decision with esacepd HTML special characters&lt;/p></decision>
            <review_state>accepted_but_modified</review_state>
            <meeting_date>2013-02-01T00:00:00.004Z</meeting_date>
            <absolute_url>http://my_site_url/Members/secretaire/mymeetings/meeting-config-college/point-a-envoyer-vers-le-conseil-communal</absolute_url>
            <externalIdentifier>ext_003</externalIdentifier>
            <extraInfos>
               <message xsi:type="xsd:string">If you want extra informations about this item, set 'showExtraInfos' to 1.</message>
            </extraInfos>
         </itemInfo>
         </itemInfo>
      </ns1:getItemInfosResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************

Returned informations about the item are :
'UID', 'id', 'title', 'category', 'description', 'decision', 'review_state', 'meeting_date', 'absolute_url', 'externalIdentifier', 'extraInfos'

Every available informations can be retrieved by setting 'showExtraInfos' to '1'.  Annexes can be retrieved by setting 'showAnnexes' to '1'

3) Search for items
-------------------

The 'searchItems(structType:SearchItems)' method can be accessed to search items in the application.

This method must be accessed with a PloneMeeting application connected user.

Here a following optional attributes to query :
string: Creator
string: Description
string: SearhableText
string: Title
string: UID
string: getCategory
string: getDecision
string: getProposingGroup
string: portal_type
string: review_state
string: meetingConfigId
string: externalIdentifier

The UID is something like : 37be48be730f1b9e94c322a571e9d0f7
The 'externalIdentifier' only exists if this item was created from an external application

The sent SOAP enveloppe should looks like this :

*** Outgoing SOAP ******************************************************
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
  SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:xsd="http://www.w3.org/1999/XMLSchema"
  xmlns:ws4="http://ws4pm.communesplone.org">
<SOAP-ENV:Body>
      <ws4:searchItemsRequest>
         <!--Optional:-->
         <Creator/>
         <!--Optional:-->
         <Description>2</Description>
         <!--Optional:-->
         <SearchableText/>
         <!--Optional:-->
         <Title/>
         <!--Optional:-->
         <UID/>
         <!--Optional:-->
         <getCategory/>
         <!--Optional:-->
         <getDecision/>
         <!--Optional:-->
         <getProposingGroup/>
         <!--Optional:-->
         <portal_type/>
         <!--Optional:-->
         <review_state/>
         <!--Optional:-->
         <meetingConfigId></meetingConfigId>
         <!--Optional:-->
         <externalIdentifier></externalIdentifier>
      </ws4:searchItemsRequest>
</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
************************************************************************


4) Test with a SOAP client
--------------------------
Here above are presented 2 ways to test : the first directly accessing the SOAP methods without the WSDL (SOAPpy) and the second using the WSDL (suds)

A successfull test has also been realized with soapUI, a SOAP client written in Java (www.soapui.org)

With a default test PloneMeeting 3.0 site, you can :
- createItem : create an item for 'pmCreator1' from group 'developers' with some data
- getItemInfos : get informations about the freshly created item or any created item in the application you know the UID of.
                 The connected user must also have the permission to access the item
- searchItems : search for existing items in the PloneMeeting application
- getConfigInfos : retrieve informations on the current PloneMeeting configuration : existing groups (MeetingGroups) and meeting configurations (MeetingConfigs)

In any case, you have to be connected to access theses methods

Test SOAP methods with SOAPpy
-----------------------------
Add the package "SOAPpy" to your buildout or to any existing python or virtualenv then :

>>> from SOAPpy import SOAPProxy, URLopener
>>> url = 'http://pmCreator1:meeting@my_site_url/myplonemeetingsite'
>>> namespace = 'http://ws4pm.communesplone.org/'
>>> server = SOAPProxy(url) 
# 2 following lines will show complete request/response SOAP messages
>>> server.config.dumpSOAPOut = 1
>>> server.config.dumpSOAPIn = 1
# to create an item
>>> server._ns(namespace).create_item('plonegov-assembly', 'developers', {'title': 'Test SOAP title', 'description': '<p>Description of the item</p>'})
# this will return the freshly created item UID or an error message if something wrong occurs
# to get informations about an item
>>> server._ns(namespace).getItemInfos('anUIDcorrespondingToAnExistingItemTheUserCanAccess')
# this will return the informations about the item

Test using the WSDL with suds (0.4+)
------------------------------------
Add the package "suds" to your buildout or to any existing python or virtualenv then :

>>> from suds.client import Client
>>> from suds.xsd.doctor import ImportDoctor, Import
>>> from suds.transport.http import HttpAuthenticated
>>> imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
>>> d = ImportDoctor(imp)
>>> url = "http://my_site_url/ws4pm.wsdl"
>>> t = HttpAuthenticated(username='pmManager', password='meeting')
>>> client = Client(url, doctor=d, transport=t)
>>> print client
# enable verbose logging
>>> import logging
>>> logging.basicConfig(level=logging.INFO)
>>> logging.getLogger('suds.client').setLevel(logging.DEBUG)
# createItem will return the freshly created item UID
>>> client.service.createItem('plonegov-assembly', 'developers', {'title': 'My new item title', 'description': 'My new item description', 'decision': 'My decision'})
>>> client.service.getItemInfos('anUIDcorrespondingToAnExistingItemTheUserCanAccess')
# this will return the informations about the item
