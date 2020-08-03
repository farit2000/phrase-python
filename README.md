# phrase-api

Phrase is a translation management platform for software projects. You can collaborate on language file translation with your team or order translations through our platform. The API allows you to import locale files, download locale files, tag keys or interact in other ways with the localization data stored in Phrase for your account.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://developers.phrase.com/api/](https://developers.phrase.com/api/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install phrase-api
```

Then import the package:
```python
import phrase_api
```

### pip install from Github repository

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/phrase/phrase-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/phrase/phrase-python.git`)

Then import the package:
```python
import phrase_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import phrase_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import phrase_api
from phrase_api.rest import ApiException
from pprint import pprint

configuration = phrase_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'

# Defining host is optional and default to https://api.phrase.com/v2
configuration.host = "https://api.phrase.com/v2"
# Enter a context with an instance of the API client
with phrase_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = phrase_api.AccountsApi(api_client)
    id = 'id_example' # str | ID (required)
    x_phrase_app_otp = 'x_phrase_app_otp_example' # str | Two-Factor-Authentication token (optional)

    try:
        # Get a single account
        api_response = api_instance.account_show(id, x_phrase_app_otp=x_phrase_app_otp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->account_show: %s\n" % e)
    
```

## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication

```python
import phrase-api

configuration = phrase-api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
```


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

```python
import phrase-api

configuration = phrase-api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'token'
```


## Documentation for API Endpoints

All URIs are relative to *https://api.phrase.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**account_show**](docs/AccountsApi.md#account_show) | **GET** /accounts/{id} | Get a single account
*AccountsApi* | [**accounts_list**](docs/AccountsApi.md#accounts_list) | **GET** /accounts | List accounts
*AuthorizationsApi* | [**authorization_create**](docs/AuthorizationsApi.md#authorization_create) | **POST** /authorizations | Create an authorization
*AuthorizationsApi* | [**authorization_delete**](docs/AuthorizationsApi.md#authorization_delete) | **DELETE** /authorizations/{id} | Delete an authorization
*AuthorizationsApi* | [**authorization_show**](docs/AuthorizationsApi.md#authorization_show) | **GET** /authorizations/{id} | Get a single authorization
*AuthorizationsApi* | [**authorization_update**](docs/AuthorizationsApi.md#authorization_update) | **PATCH** /authorizations/{id} | Update an authorization
*AuthorizationsApi* | [**authorizations_list**](docs/AuthorizationsApi.md#authorizations_list) | **GET** /authorizations | List authorizations
*BitbucketSyncApi* | [**bitbucket_sync_export**](docs/BitbucketSyncApi.md#bitbucket_sync_export) | **POST** /bitbucket_syncs/{id}/export | Export from Phrase to Bitbucket
*BitbucketSyncApi* | [**bitbucket_sync_import**](docs/BitbucketSyncApi.md#bitbucket_sync_import) | **POST** /bitbucket_syncs/{id}/import | Import to Phrase from Bitbucket
*BitbucketSyncApi* | [**bitbucket_syncs_list**](docs/BitbucketSyncApi.md#bitbucket_syncs_list) | **GET** /bitbucket_syncs | List Bitbucket syncs
*BlacklistedKeysApi* | [**blacklisted_key_create**](docs/BlacklistedKeysApi.md#blacklisted_key_create) | **POST** /projects/{project_id}/blacklisted_keys | Create a blacklisted key
*BlacklistedKeysApi* | [**blacklisted_key_delete**](docs/BlacklistedKeysApi.md#blacklisted_key_delete) | **DELETE** /projects/{project_id}/blacklisted_keys/{id} | Delete a blacklisted key
*BlacklistedKeysApi* | [**blacklisted_key_show**](docs/BlacklistedKeysApi.md#blacklisted_key_show) | **GET** /projects/{project_id}/blacklisted_keys/{id} | Get a single blacklisted key
*BlacklistedKeysApi* | [**blacklisted_key_update**](docs/BlacklistedKeysApi.md#blacklisted_key_update) | **PATCH** /projects/{project_id}/blacklisted_keys/{id} | Update a blacklisted key
*BlacklistedKeysApi* | [**blacklisted_keys_list**](docs/BlacklistedKeysApi.md#blacklisted_keys_list) | **GET** /projects/{project_id}/blacklisted_keys | List blacklisted keys
*BranchesApi* | [**branch_compare**](docs/BranchesApi.md#branch_compare) | **GET** /projects/{project_id}/branches/{name}/compare | Compare branches
*BranchesApi* | [**branch_create**](docs/BranchesApi.md#branch_create) | **POST** /projects/{project_id}/branches | Create a branch
*BranchesApi* | [**branch_delete**](docs/BranchesApi.md#branch_delete) | **DELETE** /projects/{project_id}/branches/{name} | Delete a branch
*BranchesApi* | [**branch_merge**](docs/BranchesApi.md#branch_merge) | **PATCH** /projects/{project_id}/branches/{name}/merge | Merge a branch
*BranchesApi* | [**branch_show**](docs/BranchesApi.md#branch_show) | **GET** /projects/{project_id}/branches/{name} | Get a single branch
*BranchesApi* | [**branch_update**](docs/BranchesApi.md#branch_update) | **PATCH** /projects/{project_id}/branches/{name} | Update a branch
*BranchesApi* | [**branches_list**](docs/BranchesApi.md#branches_list) | **GET** /projects/{project_id}/branches | List branches
*CommentsApi* | [**comment_create**](docs/CommentsApi.md#comment_create) | **POST** /projects/{project_id}/keys/{key_id}/comments | Create a comment
*CommentsApi* | [**comment_delete**](docs/CommentsApi.md#comment_delete) | **DELETE** /projects/{project_id}/keys/{key_id}/comments/{id} | Delete a comment
*CommentsApi* | [**comment_mark_check**](docs/CommentsApi.md#comment_mark_check) | **GET** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Check if comment is read
*CommentsApi* | [**comment_mark_read**](docs/CommentsApi.md#comment_mark_read) | **PATCH** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Mark a comment as read
*CommentsApi* | [**comment_mark_unread**](docs/CommentsApi.md#comment_mark_unread) | **DELETE** /projects/{project_id}/keys/{key_id}/comments/{id}/read | Mark a comment as unread
*CommentsApi* | [**comment_show**](docs/CommentsApi.md#comment_show) | **GET** /projects/{project_id}/keys/{key_id}/comments/{id} | Get a single comment
*CommentsApi* | [**comment_update**](docs/CommentsApi.md#comment_update) | **PATCH** /projects/{project_id}/keys/{key_id}/comments/{id} | Update a comment
*CommentsApi* | [**comments_list**](docs/CommentsApi.md#comments_list) | **GET** /projects/{project_id}/keys/{key_id}/comments | List comments
*DistributionsApi* | [**distribution_create**](docs/DistributionsApi.md#distribution_create) | **POST** /accounts/{account_id}/distributions | Create a distribution
*DistributionsApi* | [**distribution_delete**](docs/DistributionsApi.md#distribution_delete) | **DELETE** /accounts/{account_id}/distributions/{id} | Delete a distribution
*DistributionsApi* | [**distribution_show**](docs/DistributionsApi.md#distribution_show) | **GET** /accounts/{account_id}/distributions/{id} | Get a single distribution
*DistributionsApi* | [**distribution_update**](docs/DistributionsApi.md#distribution_update) | **PATCH** /accounts/{account_id}/distributions/{id} | Update a distribution
*DistributionsApi* | [**distributions_list**](docs/DistributionsApi.md#distributions_list) | **GET** /accounts/{account_id}/distributions | List distributions
*FormatsApi* | [**formats_list**](docs/FormatsApi.md#formats_list) | **GET** /formats | List formats
*GitLabSyncApi* | [**gitlab_sync_delete**](docs/GitLabSyncApi.md#gitlab_sync_delete) | **DELETE** /gitlab_syncs/{id} | Delete single Sync Setting
*GitLabSyncApi* | [**gitlab_sync_export**](docs/GitLabSyncApi.md#gitlab_sync_export) | **POST** /gitlab_syncs/{gitlab_sync_id}/export | Export from Phrase to GitLab
*GitLabSyncApi* | [**gitlab_sync_history**](docs/GitLabSyncApi.md#gitlab_sync_history) | **GET** /gitlab_syncs/{gitlab_sync_id}/history | History of single Sync Setting
*GitLabSyncApi* | [**gitlab_sync_import**](docs/GitLabSyncApi.md#gitlab_sync_import) | **POST** /gitlab_syncs/{gitlab_sync_id}/import | Import from GitLab to Phrase
*GitLabSyncApi* | [**gitlab_sync_list**](docs/GitLabSyncApi.md#gitlab_sync_list) | **GET** /gitlab_syncs | List GitLab syncs
*GitLabSyncApi* | [**gitlab_sync_show**](docs/GitLabSyncApi.md#gitlab_sync_show) | **GET** /gitlab_syncs/{id} | Get single Sync Setting
*GitLabSyncApi* | [**gitlab_sync_update**](docs/GitLabSyncApi.md#gitlab_sync_update) | **PUT** /gitlab_syncs/{id} | Update single Sync Setting
*GlossariesApi* | [**glossaries_list**](docs/GlossariesApi.md#glossaries_list) | **GET** /accounts/{account_id}/glossaries | List glossaries
*GlossariesApi* | [**glossary_create**](docs/GlossariesApi.md#glossary_create) | **POST** /accounts/{account_id}/glossaries | Create a glossary
*GlossariesApi* | [**glossary_delete**](docs/GlossariesApi.md#glossary_delete) | **DELETE** /accounts/{account_id}/glossaries/{id} | Delete a glossary
*GlossariesApi* | [**glossary_show**](docs/GlossariesApi.md#glossary_show) | **GET** /accounts/{account_id}/glossaries/{id} | Get a single glossary
*GlossariesApi* | [**glossary_update**](docs/GlossariesApi.md#glossary_update) | **PATCH** /accounts/{account_id}/glossaries/{id} | Update a glossary
*GlossaryTermTranslationsApi* | [**glossary_term_translation_create**](docs/GlossaryTermTranslationsApi.md#glossary_term_translation_create) | **POST** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations | Create a glossary term translation
*GlossaryTermTranslationsApi* | [**glossary_term_translation_delete**](docs/GlossaryTermTranslationsApi.md#glossary_term_translation_delete) | **DELETE** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations/{id} | Delete a glossary term translation
*GlossaryTermTranslationsApi* | [**glossary_term_translation_update**](docs/GlossaryTermTranslationsApi.md#glossary_term_translation_update) | **PATCH** /accounts/{account_id}/glossaries/{glossary_id}/terms/{term_id}/translations/{id} | Update a glossary term translation
*GlossaryTermsApi* | [**glossary_term_create**](docs/GlossaryTermsApi.md#glossary_term_create) | **POST** /accounts/{account_id}/glossaries/{glossary_id}/terms | Create a glossary term
*GlossaryTermsApi* | [**glossary_term_delete**](docs/GlossaryTermsApi.md#glossary_term_delete) | **DELETE** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Delete a glossary term
*GlossaryTermsApi* | [**glossary_term_show**](docs/GlossaryTermsApi.md#glossary_term_show) | **GET** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Get a single glossary term
*GlossaryTermsApi* | [**glossary_term_update**](docs/GlossaryTermsApi.md#glossary_term_update) | **PATCH** /accounts/{account_id}/glossaries/{glossary_id}/terms/{id} | Update a glossary term
*GlossaryTermsApi* | [**glossary_terms_list**](docs/GlossaryTermsApi.md#glossary_terms_list) | **GET** /accounts/{account_id}/glossaries/{glossary_id}/terms | List glossary terms
*InvitationsApi* | [**invitation_create**](docs/InvitationsApi.md#invitation_create) | **POST** /accounts/{account_id}/invitations | Create a new invitation
*InvitationsApi* | [**invitation_delete**](docs/InvitationsApi.md#invitation_delete) | **DELETE** /accounts/{account_id}/invitations/{id} | Delete an invitation
*InvitationsApi* | [**invitation_resend**](docs/InvitationsApi.md#invitation_resend) | **POST** /accounts/{account_id}/invitations/{id}/resend | Resend an invitation
*InvitationsApi* | [**invitation_show**](docs/InvitationsApi.md#invitation_show) | **GET** /accounts/{account_id}/invitations/{id} | Get a single invitation
*InvitationsApi* | [**invitation_update**](docs/InvitationsApi.md#invitation_update) | **PATCH** /accounts/{account_id}/invitations/{id} | Update an invitation
*InvitationsApi* | [**invitations_list**](docs/InvitationsApi.md#invitations_list) | **GET** /accounts/{account_id}/invitations | List invitations
*JobLocalesApi* | [**job_locale_complete**](docs/JobLocalesApi.md#job_locale_complete) | **POST** /projects/{project_id}/jobs/{job_id}/locales/{id}/complete | Complete a job locale
*JobLocalesApi* | [**job_locale_delete**](docs/JobLocalesApi.md#job_locale_delete) | **DELETE** /projects/{project_id}/jobs/{job_id}/locales/{id} | Delete a job locale
*JobLocalesApi* | [**job_locale_reopen**](docs/JobLocalesApi.md#job_locale_reopen) | **POST** /projects/{project_id}/jobs/{job_id}/locales/{id}/reopen | Reopen a job locale
*JobLocalesApi* | [**job_locale_show**](docs/JobLocalesApi.md#job_locale_show) | **GET** /projects/{project_id}/jobs/{job_id}/locale/{id} | Get a single job locale
*JobLocalesApi* | [**job_locale_update**](docs/JobLocalesApi.md#job_locale_update) | **PATCH** /projects/{project_id}/jobs/{job_id}/locales/{id} | Update a job locale
*JobLocalesApi* | [**job_locales_create**](docs/JobLocalesApi.md#job_locales_create) | **POST** /projects/{project_id}/jobs/{job_id}/locales | Create a job locale
*JobLocalesApi* | [**job_locales_list**](docs/JobLocalesApi.md#job_locales_list) | **GET** /projects/{project_id}/jobs/{job_id}/locales | List job locales
*JobsApi* | [**job_complete**](docs/JobsApi.md#job_complete) | **POST** /projects/{project_id}/jobs/{id}/complete | Complete a job
*JobsApi* | [**job_create**](docs/JobsApi.md#job_create) | **POST** /projects/{project_id}/jobs | Create a job
*JobsApi* | [**job_delete**](docs/JobsApi.md#job_delete) | **DELETE** /projects/{project_id}/jobs/{id} | Delete a job
*JobsApi* | [**job_keys_create**](docs/JobsApi.md#job_keys_create) | **POST** /projects/{project_id}/jobs/{id}/keys | Add keys to job
*JobsApi* | [**job_keys_delete**](docs/JobsApi.md#job_keys_delete) | **DELETE** /projects/{project_id}/jobs/{id}/keys | Remove keys from job
*JobsApi* | [**job_reopen**](docs/JobsApi.md#job_reopen) | **POST** /projects/{project_id}/jobs/{id}/reopen | Reopen a job
*JobsApi* | [**job_show**](docs/JobsApi.md#job_show) | **GET** /projects/{project_id}/jobs/{id} | Get a single job
*JobsApi* | [**job_start**](docs/JobsApi.md#job_start) | **POST** /projects/{project_id}/jobs/{id}/start | Start a job
*JobsApi* | [**job_update**](docs/JobsApi.md#job_update) | **PATCH** /projects/{project_id}/jobs/{id} | Update a job
*JobsApi* | [**jobs_list**](docs/JobsApi.md#jobs_list) | **GET** /projects/{project_id}/jobs | List jobs
*KeysApi* | [**key_create**](docs/KeysApi.md#key_create) | **POST** /projects/{project_id}/keys | Create a key
*KeysApi* | [**key_delete**](docs/KeysApi.md#key_delete) | **DELETE** /projects/{project_id}/keys/{id} | Delete a key
*KeysApi* | [**key_show**](docs/KeysApi.md#key_show) | **GET** /projects/{project_id}/keys/{id} | Get a single key
*KeysApi* | [**key_update**](docs/KeysApi.md#key_update) | **PATCH** /projects/{project_id}/keys/{id} | Update a key
*KeysApi* | [**keys_delete**](docs/KeysApi.md#keys_delete) | **DELETE** /projects/{project_id}/keys | Delete collection of keys
*KeysApi* | [**keys_list**](docs/KeysApi.md#keys_list) | **GET** /projects/{project_id}/keys | List keys
*KeysApi* | [**keys_search**](docs/KeysApi.md#keys_search) | **POST** /projects/{project_id}/keys/search | Search keys
*KeysApi* | [**keys_tag**](docs/KeysApi.md#keys_tag) | **PATCH** /projects/{project_id}/keys/tag | Add tags to collection of keys
*KeysApi* | [**keys_untag**](docs/KeysApi.md#keys_untag) | **PATCH** /projects/{project_id}/keys/untag | Remove tags from collection of keys
*LocalesApi* | [**locale_create**](docs/LocalesApi.md#locale_create) | **POST** /projects/{project_id}/locales | Create a locale
*LocalesApi* | [**locale_delete**](docs/LocalesApi.md#locale_delete) | **DELETE** /projects/{project_id}/locales/{id} | Delete a locale
*LocalesApi* | [**locale_download**](docs/LocalesApi.md#locale_download) | **GET** /projects/{project_id}/locales/{id}/download | Download a locale
*LocalesApi* | [**locale_show**](docs/LocalesApi.md#locale_show) | **GET** /projects/{project_id}/locales/{id} | Get a single locale
*LocalesApi* | [**locale_update**](docs/LocalesApi.md#locale_update) | **PATCH** /projects/{project_id}/locales/{id} | Update a locale
*LocalesApi* | [**locales_list**](docs/LocalesApi.md#locales_list) | **GET** /projects/{project_id}/locales | List locales
*MembersApi* | [**member_delete**](docs/MembersApi.md#member_delete) | **DELETE** /accounts/{account_id}/members/{id} | Remove a user from the account
*MembersApi* | [**member_show**](docs/MembersApi.md#member_show) | **GET** /accounts/{account_id}/members/{id} | Get single member
*MembersApi* | [**member_update**](docs/MembersApi.md#member_update) | **PATCH** /accounts/{account_id}/members/{id} | Update a member
*MembersApi* | [**members_list**](docs/MembersApi.md#members_list) | **GET** /accounts/{account_id}/members | List members
*OrdersApi* | [**order_confirm**](docs/OrdersApi.md#order_confirm) | **PATCH** /projects/{project_id}/orders/{id}/confirm | Confirm an order
*OrdersApi* | [**order_create**](docs/OrdersApi.md#order_create) | **POST** /projects/{project_id}/orders | Create a new order
*OrdersApi* | [**order_delete**](docs/OrdersApi.md#order_delete) | **DELETE** /projects/{project_id}/orders/{id} | Cancel an order
*OrdersApi* | [**order_show**](docs/OrdersApi.md#order_show) | **GET** /projects/{project_id}/orders/{id} | Get a single order
*OrdersApi* | [**orders_list**](docs/OrdersApi.md#orders_list) | **GET** /projects/{project_id}/orders | List orders
*ProjectsApi* | [**project_create**](docs/ProjectsApi.md#project_create) | **POST** /projects | Create a project
*ProjectsApi* | [**project_delete**](docs/ProjectsApi.md#project_delete) | **DELETE** /projects/{id} | Delete a project
*ProjectsApi* | [**project_show**](docs/ProjectsApi.md#project_show) | **GET** /projects/{id} | Get a single project
*ProjectsApi* | [**project_update**](docs/ProjectsApi.md#project_update) | **PATCH** /projects/{id} | Update a project
*ProjectsApi* | [**projects_list**](docs/ProjectsApi.md#projects_list) | **GET** /projects | List projects
*ReleasesApi* | [**release_create**](docs/ReleasesApi.md#release_create) | **POST** /accounts/{account_id}/distributions/{distribution_id}/releases | Create a release
*ReleasesApi* | [**release_delete**](docs/ReleasesApi.md#release_delete) | **DELETE** /accounts/{account_id}/distributions/{distribution_id}/releases/{id} | Delete a release
*ReleasesApi* | [**release_publish**](docs/ReleasesApi.md#release_publish) | **POST** /accounts/{account_id}/distributions/{distribution_id}/releases/{id}/publish | Publish a release
*ReleasesApi* | [**release_show**](docs/ReleasesApi.md#release_show) | **GET** /accounts/{account_id}/distributions/{distribution_id}/releases/{id} | Get a single release
*ReleasesApi* | [**release_update**](docs/ReleasesApi.md#release_update) | **PATCH** /accounts/{account_id}/distributions/{distribution_id}/releases/{id} | Update a release
*ReleasesApi* | [**releases_list**](docs/ReleasesApi.md#releases_list) | **GET** /accounts/{account_id}/distributions/{distribution_id}/releases | List releases
*ScreenshotMarkersApi* | [**screenshot_marker_create**](docs/ScreenshotMarkersApi.md#screenshot_marker_create) | **POST** /projects/{project_id}/screenshots/{screenshot_id}/markers | Create a screenshot marker
*ScreenshotMarkersApi* | [**screenshot_marker_delete**](docs/ScreenshotMarkersApi.md#screenshot_marker_delete) | **DELETE** /projects/{project_id}/screenshots/{screenshot_id}/markers | Delete a screenshot marker
*ScreenshotMarkersApi* | [**screenshot_marker_show**](docs/ScreenshotMarkersApi.md#screenshot_marker_show) | **GET** /projects/{project_id}/screenshots/{screenshot_id}/markers/{id} | Get a single screenshot marker
*ScreenshotMarkersApi* | [**screenshot_marker_update**](docs/ScreenshotMarkersApi.md#screenshot_marker_update) | **PATCH** /projects/{project_id}/screenshots/{screenshot_id}/markers | Update a screenshot marker
*ScreenshotMarkersApi* | [**screenshot_markers_list**](docs/ScreenshotMarkersApi.md#screenshot_markers_list) | **GET** /projects/{project_id}/screenshots/{id}/markers | List screenshot markers
*ScreenshotsApi* | [**screenshot_create**](docs/ScreenshotsApi.md#screenshot_create) | **POST** /projects/{project_id}/screenshots | Create a screenshot
*ScreenshotsApi* | [**screenshot_delete**](docs/ScreenshotsApi.md#screenshot_delete) | **DELETE** /projects/{project_id}/screenshots/{id} | Delete a screenshot
*ScreenshotsApi* | [**screenshot_show**](docs/ScreenshotsApi.md#screenshot_show) | **GET** /projects/{project_id}/screenshots/{id} | Get a single screenshot
*ScreenshotsApi* | [**screenshot_update**](docs/ScreenshotsApi.md#screenshot_update) | **PATCH** /projects/{project_id}/screenshots/{id} | Update a screenshot
*ScreenshotsApi* | [**screenshots_list**](docs/ScreenshotsApi.md#screenshots_list) | **GET** /projects/{project_id}/screenshots | List screenshots
*SpacesApi* | [**space_create**](docs/SpacesApi.md#space_create) | **POST** /accounts/{account_id}/spaces | Create a Space
*SpacesApi* | [**space_delete**](docs/SpacesApi.md#space_delete) | **DELETE** /accounts/{account_id}/spaces/{id} | Delete Space
*SpacesApi* | [**space_show**](docs/SpacesApi.md#space_show) | **GET** /accounts/{account_id}/spaces/{id} | Get Space
*SpacesApi* | [**space_update**](docs/SpacesApi.md#space_update) | **PATCH** /accounts/{account_id}/spaces/{id} | Update Space
*SpacesApi* | [**spaces_list**](docs/SpacesApi.md#spaces_list) | **GET** /accounts/{account_id}/spaces | List Spaces
*SpacesApi* | [**spaces_projects_create**](docs/SpacesApi.md#spaces_projects_create) | **POST** /accounts/{account_id}/spaces/{space_id}/projects | Add Project
*SpacesApi* | [**spaces_projects_delete**](docs/SpacesApi.md#spaces_projects_delete) | **DELETE** /accounts/{account_id}/spaces/{space_id}/projects/{id} | Remove Project
*SpacesApi* | [**spaces_projects_list**](docs/SpacesApi.md#spaces_projects_list) | **GET** /accounts/{account_id}/spaces/{space_id}/projects | List Projects
*StyleGuidesApi* | [**styleguide_create**](docs/StyleGuidesApi.md#styleguide_create) | **POST** /projects/{project_id}/styleguides | Create a style guide
*StyleGuidesApi* | [**styleguide_delete**](docs/StyleGuidesApi.md#styleguide_delete) | **DELETE** /projects/{project_id}/styleguides/{id} | Delete a style guide
*StyleGuidesApi* | [**styleguide_show**](docs/StyleGuidesApi.md#styleguide_show) | **GET** /projects/{project_id}/styleguides/{id} | Get a single style guide
*StyleGuidesApi* | [**styleguide_update**](docs/StyleGuidesApi.md#styleguide_update) | **PATCH** /projects/{project_id}/styleguides/{id} | Update a style guide
*StyleGuidesApi* | [**styleguides_list**](docs/StyleGuidesApi.md#styleguides_list) | **GET** /projects/{project_id}/styleguides | List style guides
*TagsApi* | [**tag_create**](docs/TagsApi.md#tag_create) | **POST** /projects/{project_id}/tags | Create a tag
*TagsApi* | [**tag_delete**](docs/TagsApi.md#tag_delete) | **DELETE** /projects/{project_id}/tags/{name} | Delete a tag
*TagsApi* | [**tag_show**](docs/TagsApi.md#tag_show) | **GET** /projects/{project_id}/tags/{name} | Get a single tag
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /projects/{project_id}/tags | List tags
*TeamsApi* | [**team_create**](docs/TeamsApi.md#team_create) | **POST** /accounts/{account_id}/teams | Create a Team
*TeamsApi* | [**team_delete**](docs/TeamsApi.md#team_delete) | **DELETE** /accounts/{account_id}/teams/{team_id} | Delete Team
*TeamsApi* | [**team_show**](docs/TeamsApi.md#team_show) | **GET** /accounts/{account_id}/teams/{team_id} | Get Team
*TeamsApi* | [**team_update**](docs/TeamsApi.md#team_update) | **PATCH** /accounts/{account_id}/teams/{team_id} | Update Team
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /accounts/{account_id}/teams | List Teams
*TeamsApi* | [**teams_projects_create**](docs/TeamsApi.md#teams_projects_create) | **POST** /accounts/{account_id}/teams/{team_id}/projects | Add Project
*TeamsApi* | [**teams_projects_delete**](docs/TeamsApi.md#teams_projects_delete) | **DELETE** /accounts/{account_id}/teams/{team_id}/projects/{id} | Remove Project
*TeamsApi* | [**teams_spaces_create**](docs/TeamsApi.md#teams_spaces_create) | **POST** /accounts/{account_id}/teams/{team_id}/spaces | Add Space
*TeamsApi* | [**teams_spaces_delete**](docs/TeamsApi.md#teams_spaces_delete) | **DELETE** /accounts/{account_id}/teams/{team_id}/spaces/{id} | Remove Space
*TeamsApi* | [**teams_users_create**](docs/TeamsApi.md#teams_users_create) | **POST** /accounts/{account_id}/teams/{team_id}/users | Add User
*TeamsApi* | [**teams_users_delete**](docs/TeamsApi.md#teams_users_delete) | **DELETE** /accounts/{account_id}/teams/{team_id}/users/{id} | Remove User
*TranslationsApi* | [**translation_create**](docs/TranslationsApi.md#translation_create) | **POST** /projects/{project_id}/translations | Create a translation
*TranslationsApi* | [**translation_exclude**](docs/TranslationsApi.md#translation_exclude) | **PATCH** /projects/{project_id}/translations/{id}/exclude | Exclude a translation from export
*TranslationsApi* | [**translation_include**](docs/TranslationsApi.md#translation_include) | **PATCH** /projects/{project_id}/translations/{id}/include | Revoke exclusion of a translation in export
*TranslationsApi* | [**translation_review**](docs/TranslationsApi.md#translation_review) | **PATCH** /projects/{project_id}/translations/{id}/review | Review a translation
*TranslationsApi* | [**translation_show**](docs/TranslationsApi.md#translation_show) | **GET** /projects/{project_id}/translations/{id} | Get a single translation
*TranslationsApi* | [**translation_unverify**](docs/TranslationsApi.md#translation_unverify) | **PATCH** /projects/{project_id}/translations/{id}/unverify | Mark a translation as unverified
*TranslationsApi* | [**translation_update**](docs/TranslationsApi.md#translation_update) | **PATCH** /projects/{project_id}/translations/{id} | Update a translation
*TranslationsApi* | [**translation_verify**](docs/TranslationsApi.md#translation_verify) | **PATCH** /projects/{project_id}/translations/{id}/verify | Verify a translation
*TranslationsApi* | [**translations_by_key**](docs/TranslationsApi.md#translations_by_key) | **GET** /projects/{project_id}/keys/{key_id}/translations | List translations by key
*TranslationsApi* | [**translations_by_locale**](docs/TranslationsApi.md#translations_by_locale) | **GET** /projects/{project_id}/locales/{locale_id}/translations | List translations by locale
*TranslationsApi* | [**translations_exclude**](docs/TranslationsApi.md#translations_exclude) | **PATCH** /projects/{project_id}/translations/exclude | Set exclude from export flag on translations selected by query
*TranslationsApi* | [**translations_include**](docs/TranslationsApi.md#translations_include) | **PATCH** /projects/{project_id}/translations/include | Remove exlude from import flag from translations selected by query
*TranslationsApi* | [**translations_list**](docs/TranslationsApi.md#translations_list) | **GET** /projects/{project_id}/translations | List all translations
*TranslationsApi* | [**translations_review**](docs/TranslationsApi.md#translations_review) | **PATCH** /projects/{project_id}/translations/review | Review translations selected by query
*TranslationsApi* | [**translations_search**](docs/TranslationsApi.md#translations_search) | **POST** /projects/{project_id}/translations/search | Search translations
*TranslationsApi* | [**translations_unverify**](docs/TranslationsApi.md#translations_unverify) | **PATCH** /projects/{project_id}/translations/unverify | Mark translations selected by query as unverified
*TranslationsApi* | [**translations_verify**](docs/TranslationsApi.md#translations_verify) | **PATCH** /projects/{project_id}/translations/verify | Verify translations selected by query
*UploadsApi* | [**upload_create**](docs/UploadsApi.md#upload_create) | **POST** /projects/{project_id}/uploads | Upload a new file
*UploadsApi* | [**upload_show**](docs/UploadsApi.md#upload_show) | **GET** /projects/{project_id}/uploads/{id} | View upload details
*UploadsApi* | [**uploads_list**](docs/UploadsApi.md#uploads_list) | **GET** /projects/{project_id}/uploads | List uploads
*UsersApi* | [**show_user**](docs/UsersApi.md#show_user) | **GET** /user | Show current User
*VersionsHistoryApi* | [**version_show**](docs/VersionsHistoryApi.md#version_show) | **GET** /projects/{project_id}/translations/{translation_id}/versions/{id} | Get a single version
*VersionsHistoryApi* | [**versions_list**](docs/VersionsHistoryApi.md#versions_list) | **GET** /projects/{project_id}/translations/{translation_id}/versions | List all versions
*WebhooksApi* | [**webhook_create**](docs/WebhooksApi.md#webhook_create) | **POST** /projects/{project_id}/webhooks | Create a webhook
*WebhooksApi* | [**webhook_delete**](docs/WebhooksApi.md#webhook_delete) | **DELETE** /projects/{project_id}/webhooks/{id} | Delete a webhook
*WebhooksApi* | [**webhook_show**](docs/WebhooksApi.md#webhook_show) | **GET** /projects/{project_id}/webhooks/{id} | Get a single webhook
*WebhooksApi* | [**webhook_test**](docs/WebhooksApi.md#webhook_test) | **POST** /projects/{project_id}/webhooks/{id}/test | Test a webhook
*WebhooksApi* | [**webhook_update**](docs/WebhooksApi.md#webhook_update) | **PATCH** /projects/{project_id}/webhooks/{id} | Update a webhook
*WebhooksApi* | [**webhooks_list**](docs/WebhooksApi.md#webhooks_list) | **GET** /projects/{project_id}/webhooks | List webhooks


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountDetails](docs/AccountDetails.md)
 - [AccountDetails1](docs/AccountDetails1.md)
 - [AffectedCount](docs/AffectedCount.md)
 - [AffectedResources](docs/AffectedResources.md)
 - [Authorization](docs/Authorization.md)
 - [AuthorizationCreateParameters](docs/AuthorizationCreateParameters.md)
 - [AuthorizationUpdateParameters](docs/AuthorizationUpdateParameters.md)
 - [AuthorizationWithToken](docs/AuthorizationWithToken.md)
 - [AuthorizationWithToken1](docs/AuthorizationWithToken1.md)
 - [BitbucketSync](docs/BitbucketSync.md)
 - [BitbucketSyncExportParameters](docs/BitbucketSyncExportParameters.md)
 - [BitbucketSyncExportResponse](docs/BitbucketSyncExportResponse.md)
 - [BitbucketSyncImportParameters](docs/BitbucketSyncImportParameters.md)
 - [BlacklistedKey](docs/BlacklistedKey.md)
 - [BlacklistedKeyCreateParameters](docs/BlacklistedKeyCreateParameters.md)
 - [BlacklistedKeyUpdateParameters](docs/BlacklistedKeyUpdateParameters.md)
 - [Branch](docs/Branch.md)
 - [BranchCreateParameters](docs/BranchCreateParameters.md)
 - [BranchMergeParameters](docs/BranchMergeParameters.md)
 - [BranchUpdateParameters](docs/BranchUpdateParameters.md)
 - [Comment](docs/Comment.md)
 - [CommentCreateParameters](docs/CommentCreateParameters.md)
 - [CommentMarkReadParameters](docs/CommentMarkReadParameters.md)
 - [CommentUpdateParameters](docs/CommentUpdateParameters.md)
 - [Distribution](docs/Distribution.md)
 - [DistributionCreateParameters](docs/DistributionCreateParameters.md)
 - [DistributionPreview](docs/DistributionPreview.md)
 - [DistributionUpdateParameters](docs/DistributionUpdateParameters.md)
 - [Format](docs/Format.md)
 - [GitlabSync](docs/GitlabSync.md)
 - [GitlabSyncExport](docs/GitlabSyncExport.md)
 - [GitlabSyncExportParameters](docs/GitlabSyncExportParameters.md)
 - [GitlabSyncHistory](docs/GitlabSyncHistory.md)
 - [GitlabSyncImportParameters](docs/GitlabSyncImportParameters.md)
 - [Glossary](docs/Glossary.md)
 - [GlossaryCreateParameters](docs/GlossaryCreateParameters.md)
 - [GlossaryTerm](docs/GlossaryTerm.md)
 - [GlossaryTermCreateParameters](docs/GlossaryTermCreateParameters.md)
 - [GlossaryTermTranslation](docs/GlossaryTermTranslation.md)
 - [GlossaryTermTranslationCreateParameters](docs/GlossaryTermTranslationCreateParameters.md)
 - [GlossaryTermTranslationUpdateParameters](docs/GlossaryTermTranslationUpdateParameters.md)
 - [GlossaryTermUpdateParameters](docs/GlossaryTermUpdateParameters.md)
 - [GlossaryUpdateParameters](docs/GlossaryUpdateParameters.md)
 - [Invitation](docs/Invitation.md)
 - [InvitationCreateParameters](docs/InvitationCreateParameters.md)
 - [InvitationUpdateParameters](docs/InvitationUpdateParameters.md)
 - [Job](docs/Job.md)
 - [JobCompleteParameters](docs/JobCompleteParameters.md)
 - [JobCreateParameters](docs/JobCreateParameters.md)
 - [JobDetails](docs/JobDetails.md)
 - [JobDetails1](docs/JobDetails1.md)
 - [JobKeysCreateParameters](docs/JobKeysCreateParameters.md)
 - [JobLocale](docs/JobLocale.md)
 - [JobLocaleCompleteParameters](docs/JobLocaleCompleteParameters.md)
 - [JobLocaleReopenParameters](docs/JobLocaleReopenParameters.md)
 - [JobLocaleUpdateParameters](docs/JobLocaleUpdateParameters.md)
 - [JobLocalesCreateParameters](docs/JobLocalesCreateParameters.md)
 - [JobPreview](docs/JobPreview.md)
 - [JobReopenParameters](docs/JobReopenParameters.md)
 - [JobStartParameters](docs/JobStartParameters.md)
 - [JobUpdateParameters](docs/JobUpdateParameters.md)
 - [KeyCreateParameters](docs/KeyCreateParameters.md)
 - [KeyPreview](docs/KeyPreview.md)
 - [KeyUpdateParameters](docs/KeyUpdateParameters.md)
 - [KeysSearchParameters](docs/KeysSearchParameters.md)
 - [KeysTagParameters](docs/KeysTagParameters.md)
 - [KeysUntagParameters](docs/KeysUntagParameters.md)
 - [Locale](docs/Locale.md)
 - [LocaleCreateParameters](docs/LocaleCreateParameters.md)
 - [LocaleDetails](docs/LocaleDetails.md)
 - [LocaleDetails1](docs/LocaleDetails1.md)
 - [LocalePreview](docs/LocalePreview.md)
 - [LocaleStatistics](docs/LocaleStatistics.md)
 - [LocaleUpdateParameters](docs/LocaleUpdateParameters.md)
 - [Member](docs/Member.md)
 - [MemberUpdateParameters](docs/MemberUpdateParameters.md)
 - [OrderConfirmParameters](docs/OrderConfirmParameters.md)
 - [OrderCreateParameters](docs/OrderCreateParameters.md)
 - [Project](docs/Project.md)
 - [ProjectCreateParameters](docs/ProjectCreateParameters.md)
 - [ProjectDetails](docs/ProjectDetails.md)
 - [ProjectDetails1](docs/ProjectDetails1.md)
 - [ProjectLocales](docs/ProjectLocales.md)
 - [ProjectLocales1](docs/ProjectLocales1.md)
 - [ProjectShort](docs/ProjectShort.md)
 - [ProjectUpdateParameters](docs/ProjectUpdateParameters.md)
 - [Release](docs/Release.md)
 - [ReleaseCreateParameters](docs/ReleaseCreateParameters.md)
 - [ReleasePreview](docs/ReleasePreview.md)
 - [ReleaseUpdateParameters](docs/ReleaseUpdateParameters.md)
 - [Screenshot](docs/Screenshot.md)
 - [ScreenshotCreateParameters](docs/ScreenshotCreateParameters.md)
 - [ScreenshotMarker](docs/ScreenshotMarker.md)
 - [ScreenshotMarkerCreateParameters](docs/ScreenshotMarkerCreateParameters.md)
 - [ScreenshotMarkerUpdateParameters](docs/ScreenshotMarkerUpdateParameters.md)
 - [ScreenshotUpdateParameters](docs/ScreenshotUpdateParameters.md)
 - [Space](docs/Space.md)
 - [SpaceCreateParameters](docs/SpaceCreateParameters.md)
 - [SpaceUpdateParameters](docs/SpaceUpdateParameters.md)
 - [SpacesProjectsCreateParameters](docs/SpacesProjectsCreateParameters.md)
 - [Styleguide](docs/Styleguide.md)
 - [StyleguideCreateParameters](docs/StyleguideCreateParameters.md)
 - [StyleguideDetails](docs/StyleguideDetails.md)
 - [StyleguideDetails1](docs/StyleguideDetails1.md)
 - [StyleguidePreview](docs/StyleguidePreview.md)
 - [StyleguideUpdateParameters](docs/StyleguideUpdateParameters.md)
 - [Tag](docs/Tag.md)
 - [TagCreateParameters](docs/TagCreateParameters.md)
 - [TagWithStats](docs/TagWithStats.md)
 - [TagWithStats1](docs/TagWithStats1.md)
 - [TagWithStats1Statistics](docs/TagWithStats1Statistics.md)
 - [TagWithStats1Statistics1](docs/TagWithStats1Statistics1.md)
 - [Team](docs/Team.md)
 - [TeamCreateParameters](docs/TeamCreateParameters.md)
 - [TeamDetail](docs/TeamDetail.md)
 - [TeamUpdateParameters](docs/TeamUpdateParameters.md)
 - [TeamsProjectsCreateParameters](docs/TeamsProjectsCreateParameters.md)
 - [TeamsSpacesCreateParameters](docs/TeamsSpacesCreateParameters.md)
 - [TeamsUsersCreateParameters](docs/TeamsUsersCreateParameters.md)
 - [Translation](docs/Translation.md)
 - [TranslationCreateParameters](docs/TranslationCreateParameters.md)
 - [TranslationDetails](docs/TranslationDetails.md)
 - [TranslationDetails1](docs/TranslationDetails1.md)
 - [TranslationExcludeParameters](docs/TranslationExcludeParameters.md)
 - [TranslationIncludeParameters](docs/TranslationIncludeParameters.md)
 - [TranslationKey](docs/TranslationKey.md)
 - [TranslationKeyDetails](docs/TranslationKeyDetails.md)
 - [TranslationKeyDetails1](docs/TranslationKeyDetails1.md)
 - [TranslationOrder](docs/TranslationOrder.md)
 - [TranslationReviewParameters](docs/TranslationReviewParameters.md)
 - [TranslationUnverifyParameters](docs/TranslationUnverifyParameters.md)
 - [TranslationUpdateParameters](docs/TranslationUpdateParameters.md)
 - [TranslationVerifyParameters](docs/TranslationVerifyParameters.md)
 - [TranslationVersion](docs/TranslationVersion.md)
 - [TranslationVersionWithUser](docs/TranslationVersionWithUser.md)
 - [TranslationVersionWithUser1](docs/TranslationVersionWithUser1.md)
 - [TranslationsExcludeParameters](docs/TranslationsExcludeParameters.md)
 - [TranslationsIncludeParameters](docs/TranslationsIncludeParameters.md)
 - [TranslationsReviewParameters](docs/TranslationsReviewParameters.md)
 - [TranslationsSearchParameters](docs/TranslationsSearchParameters.md)
 - [TranslationsUnverifyParameters](docs/TranslationsUnverifyParameters.md)
 - [TranslationsVerifyParameters](docs/TranslationsVerifyParameters.md)
 - [Upload](docs/Upload.md)
 - [UploadCreateParameters](docs/UploadCreateParameters.md)
 - [UploadSummary](docs/UploadSummary.md)
 - [User](docs/User.md)
 - [UserPreview](docs/UserPreview.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookCreateParameters](docs/WebhookCreateParameters.md)
 - [WebhookUpdateParameters](docs/WebhookUpdateParameters.md)


## Author

support@phrase.com


