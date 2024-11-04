# generated by datamodel-codegen:
#   filename:  openapi.json
#   timestamp: 2024-11-04T20:48:45+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_serializer, model_validator


class Admin(BaseModel):
    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: int | None = Field(None, title="Telegram Id")
    discord_webhook: str | None = Field(None, title="Discord Webhook")


class AdminCreate(BaseModel):
    username: str = Field(..., title="Username")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: int | None = Field(None, title="Telegram Id")
    discord_webhook: str | None = Field(None, title="Discord Webhook")
    password: str = Field(..., title="Password")


class AdminModify(BaseModel):
    password: str | None = Field(None, title="Password")
    is_sudo: bool = Field(..., title="Is Sudo")
    telegram_id: int | None = Field(None, title="Telegram Id")
    discord_webhook: str | None = Field(None, title="Discord Webhook")


class BodyAdminTokenApiAdminTokenPost(BaseModel):
    grant_type: str | None = Field(None, pattern="password", title="Grant Type")
    username: str = Field(..., title="Username")
    password: str = Field(..., title="Password")
    scope: str = Field("", title="Scope")
    client_id: str | None = Field(None, title="Client Id")
    client_secret: str | None = Field(None, title="Client Secret")


class Conflict(BaseModel):
    detail: str = Field("'Entity' already exists", title="Detail")


class CoreStats(BaseModel):
    version: str = Field(..., title="Version")
    started: bool = Field(..., title="Started")
    logs_websocket: str = Field(..., title="Logs Websocket")


class Forbidden(BaseModel):
    detail: str = Field("You're not allowed 'to ...'", title="Detail")


class HTTPException(BaseModel):
    detail: str = Field(..., title="Detail")


class NodeCreate(BaseModel):
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    api_port: int = Field(62051, title="Api Port")
    usage_coefficient: float = Field(1.0, gt=0.0, title="Usage Coefficient")
    add_as_new_host: bool = Field(True, title="Add As New Host")


class NodeSettings(BaseModel):
    min_node_version: str = Field("v0.2.0", title="Min Node Version")
    certificate: str = Field(..., title="Certificate")


class NodeStatus(str, Enum):
    CONNECTED = "connected"
    CONNECTING = "connecting"
    ERROR = "error"
    DISABLED = "disabled"


class NodeUsageResponse(BaseModel):
    node_id: int | None = Field(None, title="Node Id")
    node_name: str = Field(..., title="Node Name")
    uplink: int = Field(..., title="Uplink")
    downlink: int = Field(..., title="Downlink")


class NodesUsageResponse(BaseModel):
    usages: list[NodeUsageResponse] = Field(..., title="Usages")


class NotFound(BaseModel):
    detail: str = Field("'Entity' '{}' not found", title="Detail")


class ProxyHostALPN(Enum):
    FIELD_ = ""
    H3 = "h3"
    H2 = "h2"
    HTTP_1_1 = "http/1.1"
    H3_H2_HTTP_1_1 = "h3,h2,http/1.1"
    H3_H2 = "h3,h2"
    H2_HTTP_1_1 = "h2,http/1.1"


class ProxyHostFingerprint(Enum):
    FIELD_ = ""
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    IOS = "ios"
    ANDROID = "android"
    EDGE = "edge"
    FIELD_360 = "360"
    QQ = "qq"
    RANDOM = "random"
    RANDOMIZED = "randomized"


class ProxyHostSecurity(str, Enum):
    INBOUND_DEFAULT = "inbound_default"
    NONE = "none"
    TLS = "tls"


class ProxySettings(BaseModel):
    pass


class ProxyTypes(str, Enum):
    VMESS = "vmess"
    VLESS = "vless"
    TROJAN = "trojan"
    SHADOWSOCKS = "shadowsocks"


class SystemStats(BaseModel):
    version: str = Field(..., title="Version")
    mem_total: int = Field(..., title="Mem Total")
    mem_used: int = Field(..., title="Mem Used")
    cpu_cores: int = Field(..., title="Cpu Cores")
    cpu_usage: float = Field(..., title="Cpu Usage")
    total_user: int = Field(..., title="Total User")
    users_active: int = Field(..., title="Users Active")
    incoming_bandwidth: int = Field(..., title="Incoming Bandwidth")
    outgoing_bandwidth: int = Field(..., title="Outgoing Bandwidth")
    incoming_bandwidth_speed: int = Field(..., title="Incoming Bandwidth Speed")
    outgoing_bandwidth_speed: int = Field(..., title="Outgoing Bandwidth Speed")


class Token(BaseModel):
    access_token: str = Field(..., title="Access Token")
    token_type: str = Field("bearer", title="Token Type")


class Unauthorized(BaseModel):
    detail: str = Field("Not authenticated", title="Detail")


class UserDataLimitResetStrategy(str, Enum):
    NO_RESET = "no_reset"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class UserStatus(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    LIMITED = "limited"
    EXPIRED = "expired"
    ON_HOLD = "on_hold"


class UserStatusCreate(str, Enum):
    ACTIVE = "active"
    ON_HOLD = "on_hold"


class UserStatusModify(str, Enum):
    ACTIVE = "active"
    DISABLED = "disabled"
    ON_HOLD = "on_hold"


class UserTemplateCreate(BaseModel):
    name: str | None = Field(None, title="Name")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    expire_duration: int | None = Field(
        None,
        description="expire_duration can be 0 or greater in seconds",
        ge=0,
        title="Expire Duration",
    )
    username_prefix: str | None = Field(None, max_length=20, min_length=1, title="Username Prefix")
    username_suffix: str | None = Field(None, max_length=20, min_length=1, title="Username Suffix")
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")


class UserTemplateModify(BaseModel):
    name: str | None = Field(None, title="Name")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    expire_duration: int | None = Field(
        None,
        description="expire_duration can be 0 or greater in seconds",
        ge=0,
        title="Expire Duration",
    )
    username_prefix: str | None = Field(None, max_length=20, min_length=1, title="Username Prefix")
    username_suffix: str | None = Field(None, max_length=20, min_length=1, title="Username Suffix")
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")


class UserTemplateResponse(BaseModel):
    name: str | None = Field(None, title="Name")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    expire_duration: int | None = Field(
        None,
        description="expire_duration can be 0 or greater in seconds",
        ge=0,
        title="Expire Duration",
    )
    username_prefix: str | None = Field(None, max_length=20, min_length=1, title="Username Prefix")
    username_suffix: str | None = Field(None, max_length=20, min_length=1, title="Username Suffix")
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")
    id: int = Field(..., title="Id")


class UserUsageResponse(BaseModel):
    node_id: int | None = Field(None, title="Node Id")
    node_name: str = Field(..., title="Node Name")
    used_traffic: int = Field(..., title="Used Traffic")


class UserUsagesResponse(BaseModel):
    username: str = Field(..., title="Username")
    usages: list[UserUsageResponse] = Field(..., title="Usages")


class UsersUsagesResponse(BaseModel):
    usages: list[UserUsageResponse] = Field(..., title="Usages")


class ValidationError(BaseModel):
    loc: list[str | int] = Field(..., title="Location")
    msg: str = Field(..., title="Message")
    type: str = Field(..., title="Error Type")


class HTTPValidationError(BaseModel):
    detail: list[ValidationError] | None = Field(None, title="Detail")


class NodeModify(BaseModel):
    name: str | None = Field(None, title="Name")
    address: str | None = Field(None, title="Address")
    port: int | None = Field(None, title="Port")
    api_port: int | None = Field(None, title="Api Port")
    usage_coefficient: float | None = Field(None, title="Usage Coefficient")
    status: NodeStatus | None = None


class NodeResponse(BaseModel):
    name: str = Field(..., title="Name")
    address: str = Field(..., title="Address")
    port: int = Field(62050, title="Port")
    api_port: int = Field(62051, title="Api Port")
    usage_coefficient: float = Field(1.0, gt=0.0, title="Usage Coefficient")
    id: int = Field(..., title="Id")
    xray_version: str | None = Field(None, title="Xray Version")
    status: NodeStatus
    message: str | None = Field(None, title="Message")


class ProxyHost(BaseModel):
    remark: str = Field(..., title="Remark")
    address: str = Field(..., title="Address")
    port: int | None = Field(None, title="Port")
    sni: str | None = Field(None, title="Sni")
    host: str | None = Field(None, title="Host")
    path: str | None = Field(None, title="Path")
    security: ProxyHostSecurity = "inbound_default"
    alpn: ProxyHostALPN = ""
    fingerprint: ProxyHostFingerprint = ""
    allowinsecure: bool | None = Field(None, title="Allowinsecure")
    is_disabled: bool | None = Field(None, title="Is Disabled")
    mux_enable: bool | None = Field(None, title="Mux Enable")
    fragment_setting: str | None = Field(None, title="Fragment Setting")
    noise_setting: str | None = Field(None, title="Noise Setting")
    random_user_agent: bool | None = Field(None, title="Random User Agent")


class ProxyInbound(BaseModel):
    tag: str = Field(..., title="Tag")
    protocol: ProxyTypes
    network: str = Field(..., title="Network")
    tls: str = Field(..., title="Tls")
    port: int | str = Field(..., title="Port")


class SubscriptionUserResponse(BaseModel):
    proxies: dict[str, Any] = Field(..., title="Proxies")
    expire: int | None = Field(None, title="Expire")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    data_limit_reset_strategy: UserDataLimitResetStrategy = "no_reset"
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")
    note: str | None = Field(None, title="Note")
    sub_updated_at: datetime | None = Field(None, title="Sub Updated At")
    sub_last_user_agent: str | None = Field(None, title="Sub Last User Agent")
    online_at: datetime | None = Field(None, title="Online At")
    on_hold_expire_duration: int | None = Field(None, title="On Hold Expire Duration")
    on_hold_timeout: datetime | None = Field(None, title="On Hold Timeout")
    auto_delete_in_days: int | None = Field(None, title="Auto Delete In Days")
    username: str = Field(..., title="Username")
    status: UserStatus
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    links: list[str] = Field([], title="Links")
    subscription_url: str = Field("", title="Subscription Url")
    excluded_inbounds: dict[str, list[str]] = Field({}, title="Excluded Inbounds")
    admin: Admin | None = None


class UserCreate(BaseModel):
    proxies: dict[str, ProxySettings] = Field({}, title="Proxies")
    expire: int | None = Field(None, title="Expire")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    data_limit_reset_strategy: UserDataLimitResetStrategy = "no_reset"
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")
    note: str | None = Field(None, title="Note")
    sub_updated_at: datetime | None = Field(None, title="Sub Updated At")
    sub_last_user_agent: str | None = Field(None, title="Sub Last User Agent")
    online_at: datetime | None = Field(None, title="Online At")
    on_hold_expire_duration: int | None = Field(None, title="On Hold Expire Duration")
    on_hold_timeout: datetime | None = Field(None, title="On Hold Timeout")
    auto_delete_in_days: int | None = Field(None, title="Auto Delete In Days")
    username: str = Field(..., title="Username")
    status: UserStatusCreate | None = None


class UserModify(BaseModel):
    proxies: dict[str, ProxySettings] = Field({}, title="Proxies")
    expire: int | None = Field(None, title="Expire")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    data_limit_reset_strategy: UserDataLimitResetStrategy | None = None
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")
    note: str | None = Field(None, title="Note")
    sub_updated_at: datetime | None = Field(None, title="Sub Updated At")
    sub_last_user_agent: str | None = Field(None, title="Sub Last User Agent")
    online_at: datetime | None = Field(None, title="Online At")
    on_hold_expire_duration: int | None = Field(None, title="On Hold Expire Duration")
    on_hold_timeout: datetime | None = Field(None, title="On Hold Timeout")
    auto_delete_in_days: int | None = Field(None, title="Auto Delete In Days")
    status: UserStatusModify | None = None


class UserResponse(BaseModel):
    proxies: dict[str, Any] = Field(..., title="Proxies")
    expire: int | None = Field(None, title="Expire")
    data_limit: int | None = Field(None, description="data_limit can be 0 or greater", ge=0, title="Data Limit")
    data_limit_reset_strategy: UserDataLimitResetStrategy = "no_reset"
    inbounds: dict[str, list[str]] = Field({}, title="Inbounds")
    note: str | None = Field(None, title="Note")
    sub_updated_at: datetime | None = Field(None, title="Sub Updated At")
    sub_last_user_agent: str | None = Field(None, title="Sub Last User Agent")
    online_at: datetime | None = Field(None, title="Online At")
    on_hold_expire_duration: int | None = Field(None, title="On Hold Expire Duration")
    on_hold_timeout: datetime | None = Field(None, title="On Hold Timeout")
    auto_delete_in_days: int | None = Field(None, title="Auto Delete In Days")
    username: str = Field(..., title="Username")
    status: UserStatus
    used_traffic: int = Field(..., title="Used Traffic")
    lifetime_used_traffic: int = Field(0, title="Lifetime Used Traffic")
    created_at: datetime = Field(..., title="Created At")
    links: list[str] = Field([], title="Links")
    subscription_url: str = Field("", title="Subscription Url")
    excluded_inbounds: dict[str, list[str]] = Field({}, title="Excluded Inbounds")
    admin: Admin | None = None


class UsersResponse(BaseModel):
    users: list[UserResponse] = Field(..., title="Users")
    total: int = Field(..., title="Total")


class AdditionalResponse(BaseModel):
    additional_properties: dict[str, Any] = {}

    @model_validator(mode="before")
    def _additional_properties_val(cls, data: dict[str, Any]):
        return {"additional_properties": data}

    @model_serializer()
    def _additional_properties_ser(self):
        return self.additional_properties


class InboundsResponse(AdditionalResponse):
    additional_properties: dict[str, list[ProxyInbound]] = {}
