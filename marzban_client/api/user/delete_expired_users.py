import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, Unauthorized
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    expired_after: Union[Unset, datetime.datetime] = UNSET,
    expired_before: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_expired_after: Union[Unset, str] = UNSET
    if not isinstance(expired_after, Unset):
        json_expired_after = expired_after.isoformat()
    params["expired_after"] = json_expired_after

    json_expired_before: Union[Unset, str] = UNSET
    if not isinstance(expired_before, Unset):
        json_expired_before = expired_before.isoformat()
    params["expired_before"] = json_expired_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/api/users/expired",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List[str], Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.model_validate(response.json())

        return response_401
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, List[str], Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    expired_after: Union[Unset, datetime.datetime] = UNSET,
    expired_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[HTTPValidationError, List[str], Unauthorized]]:
    """Delete Expired Users

     Delete users who have expired within the specified date range.

    - **expired_after** UTC datetime (optional)
    - **expired_before** UTC datetime (optional)
    - At least one of expired_after or expired_before must be provided

    Args:
        expired_after (Union[Unset, datetime.datetime]):
        expired_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[str], Unauthorized]]
    """

    kwargs = _get_kwargs(
        expired_after=expired_after,
        expired_before=expired_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    expired_after: Union[Unset, datetime.datetime] = UNSET,
    expired_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[HTTPValidationError, List[str], Unauthorized]]:
    """Delete Expired Users

     Delete users who have expired within the specified date range.

    - **expired_after** UTC datetime (optional)
    - **expired_before** UTC datetime (optional)
    - At least one of expired_after or expired_before must be provided

    Args:
        expired_after (Union[Unset, datetime.datetime]):
        expired_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[str], Unauthorized]
    """

    return sync_detailed(
        client=client,
        expired_after=expired_after,
        expired_before=expired_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    expired_after: Union[Unset, datetime.datetime] = UNSET,
    expired_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[HTTPValidationError, List[str], Unauthorized]]:
    """Delete Expired Users

     Delete users who have expired within the specified date range.

    - **expired_after** UTC datetime (optional)
    - **expired_before** UTC datetime (optional)
    - At least one of expired_after or expired_before must be provided

    Args:
        expired_after (Union[Unset, datetime.datetime]):
        expired_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[str], Unauthorized]]
    """

    kwargs = _get_kwargs(
        expired_after=expired_after,
        expired_before=expired_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    expired_after: Union[Unset, datetime.datetime] = UNSET,
    expired_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[HTTPValidationError, List[str], Unauthorized]]:
    """Delete Expired Users

     Delete users who have expired within the specified date range.

    - **expired_after** UTC datetime (optional)
    - **expired_before** UTC datetime (optional)
    - At least one of expired_after or expired_before must be provided

    Args:
        expired_after (Union[Unset, datetime.datetime]):
        expired_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[str], Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            expired_after=expired_after,
            expired_before=expired_before,
        )
    ).parsed
