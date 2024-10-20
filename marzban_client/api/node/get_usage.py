from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models import Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/nodes/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NodesUsageResponse.model_validate(response.json())

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
) -> Response[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Response[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    """Get Usage

     Retrieve usage statistics for nodes within a specified date range.

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Optional[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    """Get Usage

     Retrieve usage statistics for nodes within a specified date range.

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Response[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    """Get Usage

     Retrieve usage statistics for nodes within a specified date range.

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = "",
    end: Union[Unset, str] = "",
) -> Optional[Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]]:
    """Get Usage

     Retrieve usage statistics for nodes within a specified date range.

    Args:
        start (Union[Unset, str]):  Default: ''.
        end (Union[Unset, str]):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Forbidden, HTTPValidationError, NodesUsageResponse, Unauthorized]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
        )
    ).parsed
