Changelog
=========


4.2.10 (2023-12-11)
-------------------

- Added translations related to new `advice_hide_during_redaction_history`.
  [gbastien]
- Added translation for `No vote for following ${number} item(s)`.
  [gbastien]
- Added translation for faceted filter `Title only`.
  [gbastien]
- Removed translations for the `add_advicecreated_state` WFA.
  [gbastien]

4.2.9 (2023-11-27)
------------------

- Adapted translations for item mail events `lateItem`, `itemUnpresented`,
  `itemDelayed`, `itemPostponedNextMeeting`, `returnedToProposingGroup`,
  `returnedToMeetingManagers` to include last WF action author and comment.
  Added translation for new item mail notification
  `event_item_postponed_next_meeting_owner`.
  [gbastien]
- Added translations for `ToolPloneMeeting.advisersConfig`.
  [gbastien]
- Added translation for `Everyone`.
  [gbastien]
- Added translation for `static_item_meeting_deadline_date`.
  [gbastien]
- Added translation for `annexes_preview_config`.
  [gbastien]
- Added translations for new WFA `wa_postpone_next_meeting_keep_internal_number`
  and `wa_postpone_next_meeting_transfer_annex_scan_id`.
  [gbastien]

4.2.8 (2023-10-27)
------------------

- Added translation for new advice type `Read`.
  [gbastien]
- Added translation for advice behavior `title_advice_accounting_commitment`.
  [gbastien]
- Added translation for `label_advice_given_by`.
  [gbastien]

4.2.7 (2023-10-19)
------------------

- Adapted translations as now we do not use brackets to manage optional advisers
  but label `[auto]` for automatically asked advices.
  [gbastien]
- Added translations for new field `MeetingItem.meetingDeadlineDate` and
  related faceted dashboard column.
  [gbastien]
- Added translations for new advice types `negative_with_remarks` and
  `back_to_proposing_group`.
  [gbastien]

4.2.6 (2023-09-21)
------------------

- Added translation for `Item completeness changed`.
  [gbastien]

4.2.5 (2023-09-12)
------------------

- Adapted translations regarding `ContentCategory` refactoring and possibility
  to not keep an annex when item sent to other MC.
  [gbastien]
- Adapted `other_mc_correspondences_descr` regarding last changes.
  [gbastien]
- Added translations for new `Copy groups` column and `Change copy groups` batch action.
  [gbastien]
- Removed translations for `MeetingConfig.useCopies` as field was removed.
  [gbastien]
- Added translations for `MeetingConfig.annexEditorMayInsertBarcode`.
  [gbastien]

4.2.4 (2023-07-12)
------------------

- Removed unused translation `groups_in_charge_can_not_be_empty_batch_action_warning`,
  is managed by `collective.eeafaceted.batchations` now.
  [gbastien]

4.2.3 (2023-07-07)
------------------

- Completed translations related to the `meeting.category` functionality.
  [gbastien]
- Added translations related to the `itemdecided` workflow adaptation.
  [gbastien]
- Added translations related to the `Update groups in charge` batch action.
  [gbastien]

4.2.2 (2023-06-27)
------------------

- Removed unused translations `show_or_hide_pollTypeObservations` and `Toggle descriptions of items`.
  [gbastien]
- Added translations for `meeting.category` related functionality.
  [gbastien]
- Reworked `advice_given_or_modified` french translation so it is more clear to the user.
  [gbastien]
- Make french translation for `wa_only_creator_may_delete` more accurate.
  [gbastien]
- Added translations related to `meeting_remove_global_access` WFA.
  [gbastien]

4.2.1 (2023-05-31)
------------------

- Adapted translations regarding `@attendees` restapi endpoints.
  [gbastien]
- Renamed translations `item_not_present_type_absent`/`item_not_present_type_excused`/
  `item_not_present_type_non_attendee` by `absent/excused/non_attendee` so it is
  easier to reuse in other contexts.
  [gbastien]
- Added translation for `annex_not_kept_because_only_pdf_annex_type_warning`.
  [gbastien]
- Refactored translations related to `MeetingConfig.validate_workflowAdaptations`
  and `MeetingConfig.validate_itemWFValidationLevels` now that states/transitions
  are checked in datagridfields.
  [gbastien]
- Completed `max_shown_...` translations to add warning about selecting a too high value.
  [gbastien]
- Fixed some typos in french translations.
  [gbastien]
- Adpated translation of `compute_item_reference_for_items_out_of_meeting_descr`
  to specify that it will update item reference of items out of meeting.
  [gbastien]

4.2 (2023-03-06)
----------------

- Completed translation `Data that will be used on new item to ${cfg_titles}`.
  [gbastien]
- Do not use `&nbsp;` in committees translations or it is displayed in
  the faceted search filter.
  [gbastien]
- Fixed french translations inversion for `wa_item_validation_shortcuts` and
  `wa_item_validation_no_validate_shortcuts`.
  [gbastien]
- Added translations for `Advice of ${advice_name}`.
  [gbastien]
- Removed unused translation `can_not_remove_attendee_defined_as_signatory`.
  [gbastien]
- Added translation for `title_committees_committee_observations`.
  [gbastien]
- Adapted translation for advice title to include advice label.
  [gbastien]
- Completed translations regarding `committees editors` functionality.
  [gbastien]
- Adapted translations regarding `per vote poll_type` functionality.
  [gbastien]
- Added translations for the `MeetingItem.votesResult` functionality.
  [gbastien]
- Added missing translation for `wa_presented_back_to_wrong_itemWFValidationLevels`.
  [gbastien]
- Added translations regarding `MeetingConfig.itemObserversStates`.
  [gbastien]
- Added trabskations regarding
  WFA `hide_decisions_when_under_writing_check_returned_to_proposing_group`.
  [gbastien]
- Removed translations for field `MeetingConfig.useGroupsAsCategories` that was removed.
  [gbastien]

4.2b31 (2022-09-22)
-------------------

- Added translation for `wa_waiting_advices_given_and_signed_advices_required_to_validate`.
  [gbastien]

4.2b30 (2022-09-19)
-------------------

- Use `"` instead `'` everywhere possible.
  [gbastien]
- For items created from another config, use french term `Créé depuis`
  instead `Reçu depuis`.
  [gbastien]
- Completed attendees changes related translations.
  [gbastien]
- Added translation for `can_not_remove_attendee_defined_as_signatory`.
  [gbastien]

4.2b29 (2022-08-26)
-------------------

- Added translations related to `attendees order by item`.
  [gbastien]
- Removed translations related to field
  `MeetingConfig.transitionsForPresentingAnItem` that was removed.
  [gbastien]
- Added translations related to meeting numbers info and warning messages.
  [gbastien]
- Adapted translations as field `MeetingConfig.yearlyInitMeetingNumber`
  was renamed to `MeetingConfig.yearlyInitMeetingNumbers`.
  [gbastien]
- Added translations related to `item_only` committee.
  [gbastien]
- Adapted `has_required_waiting_advices` to explain to check that
  given advices reached their workflow last step.
  [gbastien]
- Adapted translations for `store_as_annex_type_title` and
  `available_mailing_lists_title` to specify generated format now that
  POD templates are grouped by title in the generationlinks viewlet.
  Added translation for `Please choose a format to generate here next`.
  [gbastien]

4.2b28 (2022-07-01)
-------------------

- Added translations related to `encode votes by group`.
  [gbastien]
- Completed item assembly text related descriptions.
  [gbastien]
- Removed translations for `start_date_before_meeting_date` and
  `end_date_before_meeting_date`.
  [gbastien]

4.2b27 (2022-06-14)
-------------------

- Fixed typos in french for `first_linked_vote_used_vote_values_descr` and
  `next_linked_votes_used_vote_values_descr`.
  [gbastien]
- Added translations for `transfered WF adaptation`.
  [gbastien]

4.2b26 (2022-05-10)
-------------------

- Added translation for `advice_hide_during_redaction_set_auto_to_true`.
  [gbastien]

4.2b25 (2022-05-03)
-------------------

- Completed translation `Item WF validation levels extra suffixes description.`.
  [gbastien]

4.2b24 (2022-04-28)
-------------------

- Added translations for new field `Meeting.adopts_next_agenda_of`.
  [gbastien]
- Added translations for every `levelXreviewers` plonegroup suffixes.
  [gbastien]
- Fixed translation for `can_not_delete_organization_groupsincharge`,
  was `can_not_delete_organization_groupincharge` before (missing `s`).
  [gbastien]
- Added translations for new field `Meeting.mid_start_date`.
  [gbastien]
- Removed `icon_help_waiting_advices_from_xxx` translations, no more used.
  [gbastien]
- Added translation for `proposing_group_with_group_in_charge_required`.
  [gbastien]
- Added translation for `can_not_unselect_plone_group_org`.
  [gbastien]
- Added new WFAdaptations related translations (`dependencies validation`,
  `item_validation_no_validate_shortcuts`, `item_validation_shortcuts`,
  `no_decide`, `no_freeze`).
  [gbastien]
- Added translation for `The configuration does not let you add annexes.`.
  [gbastien]
- Completed translation for `This attendee is marked as ${not_present_type}
  for the ${number} following items (${clusters})`.
  [gbastien]

4.2b23 (2022-03-07)
-------------------

- Added translation `All cache was invalidated`.
  [gbastien]

4.2b22 (2022-01-27)
-------------------

- More generic translation for `internal_notes_descr`.
  [gbastien]

4.2b21 (2022-01-21)
-------------------

- Completed `item_reference_format_descr`.
  [gbastien]

4.2b20 (2022-01-14)
-------------------

- Added help message for column header `header_privacy_help` and
  `header_pollType_help` to get narrower columns.
  [gbastien]

4.2b19 (2022-01-14)
-------------------

- Added translation for `header_async_actions`.
  [gbastien]
- Clarified french translation for `remove_advice_inheritance_ask_locally_not_configured`.
  [gbastien]

4.2b18 (2022-01-07)
-------------------

- Added translation for `Used as item initiator for items`.
  [gbastien]

4.2b17 (2022-01-03)
-------------------

- Added translation for `ckeditor_style_table_optimization`.
  [gbastien]

4.2b16 (2022-01-03)
-------------------

- Added translations for `MeetingConfig.enableAdviceProposingGroupComment`.
  [gbastien]
- Added translation for `listingheader_pod_template_or_odt_file`.
  [gbastien]
- Added translations for `MeetingConfig.itemLabelsEditableByProposingGroupForever`.
  [gbastien]
- Added translations for `MeetingConfig.itemInternalNotesEditableBy`.
  [gbastien]
- Fixed typo in french translation of `PloneMeeting_label_orderedItemInitiators`.
  [gbastien]
- Added translations for `ToolPloneMeeting.deferParentReindex`.
  [gbastien]
- Added translations regarding `Meeting in videoconference` functionality.
  [aduchene]

4.2b15 (2021-11-26)
-------------------

- Small fix in e-mail notification sent when a WF transition is triggered,
  avoid use of `"` in `item_state_changed_default_mail_subject` translation as
  it may also be in translated message leading to `""`.
  [gbastien]
- Make some french translations (`Waiting advices WFA` and `Held position label`)
  more accurate.
  [gbastien]

4.2b14 (2021-11-08)
-------------------

- Added translation for `proposing_group_not_available`.
  [gbastien]
- Added translations regarding `Advice proposing group comment` functionality.
  [gbastien]
- Fixed typo in french translation of `itemDelayed_mail_body`.
  [gbastien]
- Adapted translation for `pod_templates_descr` to include link to
  `Show POD templates details`.
  [gbastien]

4.2b13 (2021-09-29)
-------------------

- More accurate french translation for `can_not_switch_polltype_votes_encoded`.
  [gbastien]

4.2b12 (2021-09-28)
-------------------

- More accurate french translation for `ckeditor_style_pm_anonymize`.
  [gbastien]

4.2b11 (2021-09-28)
-------------------

- Completed french translation for `transition_event_history_aware`.
  [gbastien]
- Added translation for `users_in_suffixed_group` used in
  `MeetingConfig.listSelectableAdvisers` to display number
  of users in advisers Plone group.
  [gbastien]
- Fixed typo in french translation of `PloneMeeting_label_selectableAdviserUsers`.
  [gbastien]
- Completed mail notifications translations `item_state_changed_default_mail_subject`
  and `item_state_changed_default_mail_body` to include transition infos
  (title, actor, comments) now that it is available in received `translationMapping`.
  [gbastien]
- Added translation `ckeditor_style_pm_anonymize`.
  [gbastien]

4.2b10 (2021-09-09)
-------------------

- Added translations for `MeetingConfig.itemPreferredMeetingStates`.
  [aduchene]
- Added translations regarding the `Ask advice to specific users` functionality.
  [gbastien]
- Added translations regarding the `Deadlines to validate items for a meeting` functionality.
  [gbastien]
- Accurate french translations for item navigation widget `Go to next/previous/... item`.
  [gbastien]
- Completed `MeetingConfig.hideHistoryTo` field description.
  [gbastien]
- Adapted translation of field `MeetingCategory.category_id` from `Category identifier`
  to `Category secondary identifier` to avoid confusion with category identifier (id).
  [gbastien]
- Added translations for new mail notification settings.
  [aduchene]
- Completed translations of error messages returned by `MeetingConfig.validate_itemWFValidationLevels`.
  [gbastien]
- Added translations for `MeetingConfig.computeItemReferenceForItemsOutOfMeeting`.
  [gbastien]
- Added translation for `error_some_values_are_not_integers` validation error message.
  [gbastien]

4.2b9 (2021-07-16)
------------------

- Added translations for `Not completed votes` and `Completed votes`.
  [gbastien]
- Removed single quotes for `meeting_state_changed_default_mail_body`.
  [aduchene]
- Added translations now that `Preferred meeting date` column is abbreviated.
  [gbastien]
- Renamed msgid `You cannot delete the default item template, but you can deactivate it if necessary!` to
  `You cannot delete or move the default item template, but you can deactivate it if necessary!`.
  [gbastien]
- Added translations for `copy_groups_help_msg`.
  [gbastien]
- Adapted translations now that Meeting was moved from AT to DX.
  [gbastien]
- Added translations regarding the `Committees` management.
  [gbastien]
- Changed default translation for `move_item_to_given_position`.
  [gbastien]
- Added translations for annexes faceted filter vocabulary.
  [gbastien]
- Added translation for `required_groupsInCharge_ko`.
  [gbastien]
- Include `item_url` in `holidays_removed_date_in_use_error` translation.
  [gbastien]
- Added translation related to advice behavior that changed (delay no more reinitialized for a given advice).
  [gbastien]
- Removed msgids beginning with `list_type_` in the `PloneMeeting` domain, seem no more used.
  [gbastien]
- Added translations related to `Redefine attendee position on item`.
  [gbastien]
- Changed translation for `no_shown_items` from `No visible item for now.`
  to `You do not have access to these items.`.
  [gbastien]
- Added translation for warning displayed on the meeting view when `assembly/signatures` are not correct.
  [gbastien]
- More accurate translation for `Meeting.meeting_number` and `Meeting.first_item_number`
  description, explaining it is managed by the application.
  [gbastien]
- Added translations for new static columns selectable in `MeetingConfig.meetingColumns`.
  [gbastien]
- Added translations for `not_confidential_annexes`.
  [gbastien]
- Added translations for `Read more/Read less`, removed useless translation
  `This is an extract of the comment, access full comment if necessary...`.
  [gbastien]
- Added translation for `marginal_notes_column`.
  [gbastien]
- Added translation for `not_able_to_find_meeting_to_present_item_into`.
  [gbastien]
- Added translations for `error_default_poll_type_must_be_among_used_poll_types`,
  `error_first_linked_vote_used_vote_values_must_be_among_used_vote_values` and
  `error_next_linked_votes_used_vote_values_must_be_among_used_vote_values`.
  [gbastien]
- Added translation for `title_meetingmanagers_notes`.
  [gbastien]
- Added translation for `MeetingConfig.enabledAnnexesBatchActions`.
  [gbastien]
- Adapted translations for `MeetingConfig.includeGroupsInChargeDefinedOnProposingGroup`
  and `MeetingConfig.includeGroupsInChargeDefinedOnCategory` fields description
  now that, when enabled, selected `groupsInCharge` will be stored on the item.
  [gbastien]
- Completed french translation for the help message about copy groups on the item view.
  [gbastien]
- Added translations for `MeetingConfig.selectableRedefinedPositionTypes` and
  `directory.position_types` invariant `removed_redefined_position_type_in_use_error` error message.
  [gbastien]

4.2b8 (2021-01-14)
------------------

- Accurate french translation for `Position type to use as label for the signature.`.
  [gbastien]

4.2b7 (2021-01-06)
------------------

- Added translations regarding being able to define a `position_type`
  while redefining a signatory on an item.
  [gbastien]
- Added translation for warning message displayed when an item could not be
  presented using the `@@present-several-items` view.
  [gbastien]
- Added translations for dashboard header title help messages.
  [gbastien]

4.2b6 (2020-12-08)
------------------

- Reworked `Return to proposing group` related translations.
  [gbastien]
- Added translations for `DX quick edit` related functionality.
  [gbastien]
- Added translations for `votes` functionality.
  [gbastien]
- Added translations for `committeeObservations/votesObservations`
  `Meeting/MeetingItem` fields.
  [gbastien]
- Translate `MeetingCategory` in `PloneMeeting` domain.
  [gbastien]
- Added translation for message displayed on over of redefined
  signatory on meeting or item.
  [gbastien]
- Added translations for MeetingConfig field `itemsVisibleFields`,
  `itemsNotViewableVisibleFields` and `itemsNotViewableVisibleFieldsTALExpr`.
  [gbastien]

4.2b5 (2020-11-19)
------------------

- Added translations for email notifications `itemPresentedOwner`,
  `itemUnpresentedOwner`, `itemDelayedOwner` and `returnedToProposingGroupOwner`.
  [gbastien]

4.2b4 (2020-10-26)
------------------

- Better french translation for `only_for_meeting_managers_descr`.
- Adapted translations regarding message displayed in Plone users and groups management
  as we greyed actions Remove user/Remove group.
- Adapted french translation of `meetingconfig_display_groups_and_users_descr`.
- Added translations for `MeetingConfig.keepAccessToItemWhenAdvice` related functionality.
- Added translation for `Currently selected meeting config`.

4.2b3 (2020-10-02)
------------------

- Added translation for `empty_annex_file_content`.
- Fixed french translations, replace translation `donneur` by `émetteur` everywhere.
- Added translation for `stored_single_item_template_as_annex`.
- Added translations for `held_position.represented_organizations` related functionality.
- Added translations for meeting attendees validation error message.
- Added translations for `waiting_advices` item WF prettylink icon down/up WF.
- Added translations for new fields `MeetingItem.decisionEnd`,
  `MeetingItem.meetingManagersNotesSuite`, `MeetingItem.meetingManagersNotesEnd` and
  `MeetingItem.otherMeetingConfigsClonableToFieldDecisionEnd`.
- Added translations for `waiting_advices` complementary WFAdaptations.

4.2b2 (2020-09-10)
------------------

- Added translation for `To discuss?` faceted filter.
- Added translations for `To top of the page` and `To bottom of the page`.

4.2b1 (2020-08-24)
------------------

- Added translation for `has_required_waiting_advices`.
- Merged changes from 4.1.17
- Removed translations for `PloneMeeting_label_itemDecidedStates` and
  `PloneMeeting_label_itemDecidedStates` as corresponding fields were removed
  from MeetingConfig.

4.2a5 (2020-06-24)
------------------
- Merged changes from 4.1.8
- Merged changes from 4.1.9
- Merged changes from 4.1.10
- Merged changes from 4.1.11
- Merged changes from 4.1.12
- Merged changes from 4.1.13
- Merged changes from 4.1.14
- Merged changes from 4.1.15
- Merged changes from 4.1.16

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

- Added translations for "Empty item is also created from an item template" functionality.
- Added translations for "Avoid multiple clicks when creating new item by disabling the icon" functionality.

4.1.13 (2020-05-08)
-------------------

- Simplified translation "Disabled (greyed) annexes will not be kept on the new duplicated item.".
- Added translation for "Show available items to application users" functionality.
- The msgid "Preview detailled advice" was renamed to "Preview detailed advice".
- Added translations for email notifications "itemPostponedNextMeeting" and "adviceEditedOwner".

4.1.12 (2020-04-30)
-------------------

- Added back french translation for "Duplicate and keep link" in plone.po.
- Completed translation "Disabled (greyed) annexes will not be kept on the new duplicated item.".

4.1.11 (2020-04-29)
-------------------

- Simplified french translation "${number_of_annexes} annexe(s) a(ont) été stockée(s)." to "${number_of_annexes} annexes ont été stockées.".
- Added translations for the 'Duplicate item with options' functionality.

4.1.10 (2020-04-20)
-------------------

- Added translations for copyGroups faceted filter related functionality.

4.1.9 (2020-04-06)
------------------

- Added translations for MeetingItem.decisionSuite field.

4.1.8 (2020-04-02)
------------------

- Added translations for improved edition functionality.
- Added translations for the 'Non attendee' functionality.
- Added translations for 'MeetingConfig.removeAnnexesPreviewsOnMeetingClosure' related functionality.
- Added translation for 'wa_meetingmanager_correct_closed_meeting' and removed translations for 'MeetingConfig.meetingManagerMayCorrectClosedMeeting'.

4.2a4 (2020-03-13)
------------------

- Merged changes from 4.1.7

4.2a3 (2020-02-21)
------------------

- Merged changes from 4.1.6

4.2a2 (2020-02-21)
------------------

- Merged changes from 4.1.5

4.2a1 (2020-02-06)
------------------

- Adapted translations for mail notification (now that item validation roles are removed, MeetingMember does not exist anymore for example).
- Added translations for default item WF validation levels defined in MeetingConfig.itemWFValidationLevels.
- Added translation for MeetingItem.validate_groupsInCharge error message.

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
- Added translations for MeetingConfig.annexRestrictShownAndEditableAttributes related functionality.
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
- Added translations for MeetingItem.groupsInCharge and MeetingConfig.orderedGroupsInCharge fields and functionalities.
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
- Added translations for 'Unread' ftw.labels related functionality.
- Added translations for action 'Initialize personal label on existing items'.
- Added translations for person.userid field.
- Adapted translation for MeetingConfig.customAdvisers 'gives_auto_advice_on' column.
- Added translations for 'ToolPloneMeeting.enableScanDocs' field.
- Added translations regarding 'MeetingConfig.powerObservers' functionality.
- Removed translations related to ToolPloneMeeting removed fields 'extractTextFromFiles',
  'availableOcrLanguages', 'defaultOcrLanguage' and 'enableUserPreferences'
- Adapted translation for POD template mailing_list description to explain use of 'group:' in recipients
- Added translation for 'can_not_delete_meetingcategory_other_category_mapping'
- Review message used as 'title' on a HTML tag to always use same format (especially no '.' at the end)
- Added translations for MeetingConfig.meetingPresentItemWhenNoCurrentMeetingStates related functionality.
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
- Added translations for MeetingConfig.usingGroup related functionality.
- Added translations for MeetingItem.textCheckList related functionality.
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
  inheritance removal related functionality.
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
