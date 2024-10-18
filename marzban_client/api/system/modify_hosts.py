from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import HTTPValidationError, ModifyHostsModifiedHosts, ModifyHostsResponseModifyHostsApiHostsPut
from ...types import Response


def _get_kwargs(
    *,
    body: ModifyHostsModifiedHosts,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/api/hosts",
    }

    _body = body.model_dump()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModifyHostsResponseModifyHostsApiHostsPut.model_validate(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.model_validate(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModifyHostsModifiedHosts,
) -> Response[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    """Modify Hosts

     Modify proxy hosts and update the configuration.

    Args:
        body (ModifyHostsModifiedHosts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModifyHostsModifiedHosts,
) -> Optional[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    """Modify Hosts

     Modify proxy hosts and update the configuration.

    Args:
        body (ModifyHostsModifiedHosts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModifyHostsModifiedHosts,
) -> Response[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    """Modify Hosts

     Modify proxy hosts and update the configuration.

    Args:
        body (ModifyHostsModifiedHosts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModifyHostsModifiedHosts,
) -> Optional[Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]]:
    """Modify Hosts

     Modify proxy hosts and update the configuration.

    Args:
        body (ModifyHostsModifiedHosts):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ModifyHostsResponseModifyHostsApiHostsPut]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
