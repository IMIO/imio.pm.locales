Changelog
=========


4.2a1 (2020-02-06)
------------------

- Adapted translations for mail notification (now that item validation roles are removed, MeetingMember does not exist anymore for example).
- Added translations for default item WF validation levels defined in MeetingConfig.itemWFValidationLevels.
- Added translation for MeetingItem.validate_groupsInCharge error message.

4.1.4 (2020-01-10)
------------------

- Added translation for MeetingItem.validate_groupsInCharge error message.
- Adapted translation of 'searchallmeetings' and added translation for 'searchnotdecidedmeetings'.
- Simplified french translation for MeetingItem.manuallyLinkedItems description.
- Added translations for MeetingConfig.includeGroupsInChargeDefinedOnProposingGroup and MeetingConfig.includeGroupsInChargeDefinedOnCategory.

4.1.3 (2019-11-19)
------------------

- Fixed typo in 'manually_linked_items_descr' french translation.

4.1.2 (2019-11-04)
------------------

- Added translation for portal_message warning when a ftw.labels label can not be removed because used by an item.
- Adapted translation of 'Holidays warning' collective.messagesviewlet message to be less panicking.

4.1.1 (2019-10-14)
------------------

- Adapted translation of field IPMHeldPosition.secondary_position_type so it is clear that it is not an additional held_position.

4.1 (2019-10-04)
----------------

- Added missing translation for 'backTo_returned_to_proposing_group_from_returned_to_proposing_group_prevalidated'.
- Replaced translations containing strings between quotes (') by strings between double quotes (").
- Added translation for 'can_not_select_optional_adviser_same_group_as_inherited'.
- Removed empty translation file 'collective.contact.core.pot' and associated .po files.

4.1rc6 (2019-09-23)
-------------------

- Added translations for held_position.secondary_position_type field.
- Added translations for new inserting methods 'on_item_title', 'on_item_decision_first_words' and 'on_item_creator'.

4.1rc5 (2019-09-12)
-------------------

- Added translations for new advice types "cautious" and "positive_with_comments".
- Adapted translation for "Taken over by" faceted filter title.
- Adapted translations of MeetingConfig.onMeetingTransitionItemTransitionToTrigger that was moved to MeetingConfig.onMeetingTransitionItemActionToExecute.

4.1rc4 (2019-08-13)
-------------------

- Added translations for 'Groups in charge' and 'Acronym of groups in charge' dashboard columns.
- Moved translations from collective.contact.core to PloneMeeting domain, only use collective.contact.core to override existing translations.
- Adapted translation of held_position.position_type description so link displayed to edit contacts directory works while adding/editing a held_position.
- Added translations for "Associated groups" dashboard column and faceted filter.
- Added translations for "items to follow" faceted search.
- Changed translation of "Group in charge" eea faceted filter for "Groups in charge".

4.1rc3 (2019-07-19)
-------------------

- Added an empty translation for MeetingItem.groupsInCharge field description.

4.1rc2 (2019-07-01)
-------------------

- Added translation for IPMHeldPosition.position description.
- Added translations for new inserting method 'on_all_associated_groups' and related changes (MeetingConfig.orderedAssociatedOrganizations).
- Added translations for MeetingItem.groupsInCharge and MeetingConfig.orderedGroupsInCharge fields and functionnalities.
- Use same ${item_url} for messages can_not_delete_organization_meetingitem and can_not_delete_organization_config_meetingitem.

4.1rc1 (2019-06-11)
-------------------

- Adapted translations for MeetingConfig.defaultAdviceHiddenDuringRedaction label.

4.1b13 (2019-05-17)
-------------------

- Changed translation for header_getItemNumber from empty space to non-breaking spaces.
- Added translation for "Edit contacts".
- Added translation for contact usage "asker", removed some useless MeetingUsers translations.
- Added translations for MeetingConfig.orderedItemInitiators field and completed assembly/attendees
  related translations.
- Added translation for error message when mailing lists wrongly defined on POD template.
- Added translations for 'Reinitialize advice delay' action.
- Added translations for MeetingConfig 'Update items and meetings' action.
- Added translations for ToolPloneMeeting 'Invalidate all cache' action.
- Added translations for 'Update local roles' batch action.
- Added translations for 'Unread' ftw.labels related functionnality.
- Added translations for action 'Initialize personal label on existing items'.
- Added translations for person.userid field.
- Adapted translation for MeetingConfig.customAdvisers 'gives_auto_advice_on' column.
- Added translations for 'ToolPloneMeeting.enableScanDocs' field.
- Added translations regarding 'MeetingConfig.powerObservers' functionnality.
- Removed translations related to ToolPloneMeeting removed fields 'extractTextFromFiles',
  'availableOcrLanguages', 'defaultOcrLanguage' and 'enableUserPreferences'
- Adapted translation for POD template mailing_list description to explain use of 'group:' in recipients
- Added translation for 'can_not_delete_meetingcategory_other_category_mapping'
- Review message used as 'title' on a HTML tag to always use same format (especially no '.' at the end)
- Added translations for MeetingConfig.meetingPresentItemWhenNoCurrentMeetingStates related functionnality.
- Changed translation for users who recive mail when item is delayed or an advice was given
- Put the status before the title in the email topics
- Added missing transaltions (restrict_access_to_secret_items_to_descr, PloneMeeting_label_restrictAccessToSecretItemsTo)

4.1b12 (2019-01-31)
-------------------

- Added translation for datagridfield column ToolPloneMeeting.configGroups.full_label.
- Added translation for @@reorder-items action.
- Added translations for integration of collective.quickupload
  to upload several annexes at the same time.
- Override held_position.label field description.
- Added translations for "held_position used by" viewlet.
- Translate held_position.position_type field description.
- Translate deactivated WF state id so it is translated in the review_state z3ctable column.

4.1b11 (2019-01-14)
-------------------

- Accurate translation when a user is adding an organization outside 'My organization'.
- Added translations for MeetingConfig.usingGroup related functionnality.
- Added translations for MeetingItem.textCheckList related functionnality.
- Removed translations for MeetingConfig.defaultMeetingItemMotivation as field was removed.
- Added translations for new columns selectable in the MeetingConfig.meetingColumns.
- Removed useless msgids eventOccurred_mail_subject and eventOccurred_mail_body
- Added translations for 'Ordered groups' and 'Ordered categories'

4.1b10 (2018-12-04)
-------------------

- Added missing contacts new fields translations.

4.1b9 (2018-11-20)
------------------

- Added 'Style templates' label translation.
- Added translations for column held_position added to organization.certified_signatures
  and MeetingConfig.certifiedSignatures datagrid fields.
- Added translations regarding being able to manage excused by item.
- Added translations about item guests.

4.1b8 (2018-08-31)
------------------

- Added translations regarding collective.contact integration.
- Removed a lot of useless translations.
- Added translations for MeetingConfig before delete exceptions.
- Added translations for MeetingConfig.groupsHiddenInDashboardFilter.
- Added translations for MeetingConfig.inheritedAdviceRemoveableByAdviser and advice
  inheritance removal related functionnality.
- Use shorter msgids for "advice hidden during redaction" and "advice considered not
  given" sentences
- Added translation for item advice addable states displayed in "?" of advice popup
- Added translations for new field MeetingConfig.usersHiddenInDashboardFilter

4.1b7 (2018-05-04)
------------------

- Added translation for plone.app.querystring field index 'getProposingGroup'.
  Translations of plone.app.querystring PM related indexes are now translated
  in the PloneMeeting domain.
- Added translations for MeetingConfig.hideHistoryTo.
- Added translations regarding WFAdaptations 'accepted_out_of_meeting'.
- Added translations for new field MeetingConfig.contentsKeptOnSentToOtherMC and related.

4.1b6 (2018-03-19)
------------------

- Added translations for WFA 'wa_presented_item_back_to_itemcreated',
  'wa_presented_item_back_to_prevalidated' and 'wa_presented_item_back_to_itemcreated'.

4.1b5 (2018-02-23)
------------------

- Added translation for 'Review state (title)' dashboard column.
- Added translation for 'transition_event'.
- Added translations for 'MeetingConfig.itemFieldsToKeepConfigSortingFor'.
- Added translations for new CKeditor styles 'highlight-blue' and 'highlight-green'.

4.1b4 (2018-01-31)
------------------

- Added translations for 'Labels' faceted filter.
- Moved 'budget_infos_column' and 'item_reference_column' msgids from
  'PloneMeeting' domain to 'collective.eeafaceted.z3ctable' domain

4.1b3 (2018-01-23)
------------------

- Added translations for 'copyGroups' mail notification.
- Normalized backTo state translations.

4.1b2 (2017-12-07)
------------------

- Added translations for 'refused' WFAdaptation.
- Added translations for 'Has annexes to sign?' faceted filter
  [gbastien]

4.1b1 (2017-12-01)
------------------

- Updated translations.
  [gbastien]

4.0 (2017-08-04)
----------------
- Updated translations

3.3 (2015-02-27)
----------------

- Added new strings for localizations and Updated Spanish translations
  [lcaballero, macagua]
- Updated README files
  [lcaballero, macagua]
- Added more strings classifiers and metadata items for imio.pm.locales package
  [lcaballero, macagua]
- Updated regarding changes in PloneMeeting 3.3
  [gbastien]

3.2.0 (2014-02-12)
------------------
- Updated translations

3.1.0 (2013-11-04)
------------------
- Updated translations

3.0.3 (2013-08-19)
------------------
- Updated translations

3.0.2 (2013-06-21)
------------------
- Updated translations

3.0.1 (2013-06-07)
------------------
- Updated translations

0.1 2013-03-01
--------------
- Initial release
