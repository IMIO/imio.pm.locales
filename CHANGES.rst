Changelog
=========


4.1.18.10 (2021-10-28)
----------------------

- Backport from 4.2.x:

  - Fixed typo in french translation of `itemDelayed_mail_body`.
    [gbastien]

4.1.18.9 (2021-09-30)
---------------------

- Backport from 4.2.x:

  - Added translation `ckeditor_style_pm_anonymize`.
    [gbastien]
  - More accurate french translation for `ckeditor_style_pm_anonymize`.
    [gbastien]

4.1.18.8 (2021-05-31)
---------------------

- Backport from 4.2.x:

  - More accurate french translation for `not_able_to_find_meeting_to_present_item_into`.
    [gbastien]

4.1.18.7 (2021-05-20)
---------------------

- Backport from 4.2.x:

  - Added translation for `not_able_to_find_meeting_to_present_item_into`.
    [gbastien]

4.1.18.6 (2021-04-02)
---------------------

- Backport from 4.2.x:

  - Include `item_url` in `holidays_removed_date_in_use_error` translation.
    [gbastien]

4.1.18.5 (2021-03-23)
---------------------

- Backport from 4.2.x:

  - Changed default translation for `move_item_to_given_position`.
    [gbastien]
  - Added translation for `required_groupsInCharge_ko`.
    [gbastien]

4.1.18.4 (2021-02-24)
---------------------

- Backport from 4.2.x:

  - Renamed msgid `You cannot delete the default item template, but you can deactivate it if necessary!` to
    `You cannot delete or move the default item template, but you can deactivate it if necessary!`.
    [gbastien]
  - Added translations for `copy_groups_help_msg`.
    [gbastien]

4.1.18.3 (2021-01-26)
---------------------

- Backport from 4.2.x:
  Removed single quotes for `meeting_state_changed_default_mail_body`.
  [aduchene]

4.1.18.2 (2020-10-19)
---------------------

- Backport from 4.2.x:
  Adapted translations regarding message displayed in Plone users and groups management
  as we greyed actions Remove user/Remove group.

4.1.18.1 (2020-09-22)
---------------------

- Backport from 4.2.x:
  Added translations for meeting attendees validation error message.

4.1.18 (2020-09-14)
-------------------

- Backport from 4.2.x:
  Added translation for `empty_annex_file_content`.
- Added translation for `stored_single_item_template_as_annex`.

4.1.17 (2020-08-21)
-------------------

- Added translation for `Enabled?`.
- Added translation for warning message explaining why a `MeetingConfig` can not be disabled.
- Added translation for `Data that will be used on new item`.
- Renamed msgid `PloneMeeting_label_categoryMappingsWhenCloningToOtherMC` to
  `PloneMeeting_label_category_mapping_when_cloning_to_other_mc`.
- Adapted `MeetingItem.classifier` related translations.
- Shorter translation for `Signature number` in `DataGridField`, now default is `Number`.
- Added translation for `Items have been reordered.`
- Added translation for `ckeditor_style_page_break`.
- Added translation for `redirectToNextMeeting` option.
- Added translation for `meetingconfig_display_groups_and_users_descr`.
- Removed translation for `no_users_in_group` that was moved to `collective.contact.plonegroup`.
- Removed translation for `View linked Plone groups` that was moved to `collective.contact.plonegroup`.
- Added translation for `POD template to annex`.
- Adapted translations for `MeetingConfig.meetingItemTemplatesToStoreAsAnnex`.
- Reworked email notifications subject to always have relevant information at
  the beginning of the subject in case item title is very long.
- Rationalized every field descr using translation `only editable/vieable by MeetingManagers` and
  `only editable by MeetingManagers but viewable by everyone`.
- Added more accurate translation for `warning_adding_org_outside_own_org`.

4.1.16 (2020-06-24)
-------------------

- Added translation for `directory.position_types` validator.

4.1.15 (2020-06-11)
-------------------

- Added translation for "wf_transition_triggered_by_application" msgid in imio.history domain.

4.1.14 (2020-05-26)
-------------------

- Added translations for "Empty item is also created from an item template" functionnality.
- Added translations for "Avoid multiple clicks when creating new item by disabling the icon" functionnality.

4.1.13 (2020-05-08)
-------------------

- Simplified translation "Disabled (greyed) annexes will not be kept on the new duplicated item.".
- Added translation for "Show available items to application users" functionnality.
- The msgid "Preview detailled advice" was renamed to "Preview detailed advice".
- Added translations for email notifications "itemPostponedNextMeeting" and "adviceEditedOwner".

4.1.12 (2020-04-30)
-------------------

- Added back french translation for "Duplicate and keep link" in plone.po.
- Completed translation "Disabled (greyed) annexes will not be kept on the new duplicated item.".

4.1.11 (2020-04-29)
-------------------

- Simplified french translation "${number_of_annexes} annexe(s) a(ont) été stockée(s)." to "${number_of_annexes} annexes ont été stockées.".
- Added translations for the 'Duplicate item with options' functionnality.

4.1.10 (2020-04-20)
-------------------

- Added translations for copyGroups faceted filter related functionnality.

4.1.9 (2020-04-06)
------------------

- Added translations for MeetingItem.decisionSuite field.

4.1.8 (2020-04-02)
------------------

- Added translations for improved edition functionality.
- Added translations for the 'Non attendee' functionnality.
- Added translations for 'MeetingConfig.removeAnnexesPreviewsOnMeetingClosure' related functionnality.
- Added translation for 'wa_meetingmanager_correct_closed_meeting' and removed translations for 'MeetingConfig.meetingManagerMayCorrectClosedMeeting'.

4.1.7 (2020-03-12)
------------------

- Added translation for person.firstname_abbreviated field.
- Added translations for MeetingItem.meetingManagersNotes field.
- Added translation for "Item is signed?" faceted filter.

4.1.6 (2020-02-21)
------------------

- Adapted translation of history message when item was created from item template that includes now the original item template path and title.

4.1.5 (2020-02-18)
------------------

- Added translation for 'Temporary QR code!'.
- Added translations for MeetingConfig.annexRestrictShownAndEditableAttributes related functionnality.
- Added translations for Meeting.convocationDate.

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
