# apis_v1/documentation_source/voter_email_address_save_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def voter_email_address_save_doc_template_values(url_root):
    """
    Show documentation about voterEmailAddressSave
    """
    required_query_parameter_list = [
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
        {
            'name':         'voter_device_id',
            'value':        'string',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'text_for_email_address',
            'value':        'string',  # boolean, integer, long, string
            'description':  'The address text a voter enters to identify the location tied to their ballot. '
                            '(Not mailing address.)',
        },
    ]
    optional_query_parameter_list = [
        {
            'name':         'make_primary_email',
            'value':        'boolean',  # boolean, integer, long, string
            'description':  'When this variable is passed in as true, change this (verified) email to be the primary.',
        },
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'Cannot proceed. A valid voter_device_id parameter was not included.',
        },
        {
            'code':         'MISSING_VOTER_ID_OR_ADDRESS_TYPE',
            'description':  'Cannot proceed. Missing variables voter_id or address_type while trying to save.',
        },
    ]

    try_now_link_variables_dict = {
        # 'organization_we_vote_id': 'wv85org1',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "voter_device_id": string (88 characters long),\n' \
                   '  "text_for_email_address": string,\n' \
                   '  "email_address_saved_we_vote_id": string,\n' \
                   '  "email_address_created": boolean,\n' \
                   '  "verification_email_sent": boolean,\n' \
                   '  "email_address_already_owned_by_other_voter": boolean,\n' \
                   '  "email_address_found": boolean,\n' \
                   '  "email_address_list_found": boolean,\n' \
                   '  "email_address_list": list\n' \
                   '   [\n' \
                   '     "normalized_email_address": string,\n' \
                   '     "primary_email": boolean,\n' \
                   '     "email_permanent_bounce": boolean,\n' \
                   '     "email_ownership_is_verified": boolean,\n' \
                   '     "voter_we_vote_id": string,\n' \
                   '     "email_we_vote_id": string,\n' \
                   '   ],\n' \
                   '}'

    template_values = {
        'api_name': 'voterEmailAddressSave',
        'api_slug': 'voterEmailAddressSave',
        'api_introduction':
            "Save or create an email address for the current voter.",
        'try_now_link': 'apis_v1:voterEmailAddressSaveView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
