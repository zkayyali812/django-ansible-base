from rest_framework.test import APIClient

from ansible_base.lib.utils.response import get_relative_url


def check_feature_flag(response, key, state, description):
    assert key in response.data
    assert 'state' in response.data[key]
    assert state == response.data[key]['state']
    assert 'description' in response.data[key]
    assert description == response.data[key]['description']


def test_feature_flags_api_list(admin_api_client: APIClient):
    """
    Test that we can list all feature flags
    """
    url = get_relative_url("featureflags-list")
    response = admin_api_client.get(url)
    assert response.status_code == 200
    check_feature_flag(response=response, key='SOME_PLATFORM_FLAG', state=False, description='This is a dummy flag, shown as an example.')


def test_feature_flags_api_get(admin_api_client):
    """
    Test that we can get an individual feature flag
    """
    url = get_relative_url("featureflags-detail", args=['SOME_PLATFORM_FLAG'])
    response = admin_api_client.get(url)
    assert response.status_code == 200
    check_feature_flag(response=response, key='SOME_PLATFORM_FLAG', state=False, description='This is a dummy flag, shown as an example.')


def test_feature_flags_api_patch(admin_api_client):
    """
    Test that we can toggle a feature flags state
    """
    url = get_relative_url("featureflags-detail", args=['SOME_PLATFORM_FLAG'])
    response = admin_api_client.get(url)
    assert response.status_code == 200
    check_feature_flag(response=response, key='SOME_PLATFORM_FLAG', state=False, description='This is a dummy flag, shown as an example.')
    response = admin_api_client.patch(url, args=['SOME_PLATFORM_FLAG'], data={"state": True}, format='json')
    check_feature_flag(response=response, key='SOME_PLATFORM_FLAG', state=True, description='This is a dummy flag, shown as an example.')
    assert response.status_code == 200
