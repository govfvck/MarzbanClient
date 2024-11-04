from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Admin, AdminModify, Forbidden, HTTPValidationError, Unauthorized
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    body: AdminModify,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/admin/{username}",
    }

    _body = body.model_dump()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Admin.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = Unauthorized.model_validate(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Forbidden.model_validate(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: AdminModify,
) -> Response[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    """Modify Admin

     Modify an existing admin's details.

    Args:
        username (str):
        body (AdminModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    body: AdminModify,
) -> Optional[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    """Modify Admin

     Modify an existing admin's details.

    Args:
        username (str):
        body (AdminModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Admin, Forbidden, HTTPValidationError, Unauthorized]
    """

    return sync_detailed(
        username=username,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: AdminModify,
) -> Response[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    """Modify Admin

     Modify an existing admin's details.

    Args:
        username (str):
        body (AdminModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]
    """

    kwargs = _get_kwargs(
        username=username,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    body: AdminModify,
) -> Optional[Union[Admin, Forbidden, HTTPValidationError, Unauthorized]]:
    """Modify Admin

     Modify an existing admin's details.

    Args:
        username (str):
        body (AdminModify):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Admin, Forbidden, HTTPValidationError, Unauthorized]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            body=body,
        )
    ).parsed
