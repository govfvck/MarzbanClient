openapi-python-client generate --path ./openapi.json \
    --config ./generator-config.yaml --custom-template-path=templates \
    --meta=none

rm -r marzban_client/models/*

datamodel-codegen --input openapi.json \
    --input-file-type openapi \
    --output-model-type pydantic_v2.BaseModel \
    --strict-nullable --snake-case-field --capitalize-enum-members \
    --use-union-operator --use-standard-collections \
    >marzban_client/models/__init__.py
