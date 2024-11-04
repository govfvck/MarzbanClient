class AdditionalResponse(BaseModel):
    additional_properties: dict[str, Any] = {}

    @model_validator(mode="before")
    def _additional_properties(cls, data: dict[str, Any]):
        return {"additional_properties": data}

    @model_serializer()
    def _additional_properties(self):
        return self.additional_properties


class InboundsResponse(AdditionalResponse):
    additional_properties: dict[str, ProxyInbound] = {}