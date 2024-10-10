# -*- coding: utf-8 -*-
from datetime import timedelta

from feast.entity import Entity
from feast.types import String, Int64, Float64
from feast.feature_view import FeatureView
from feast.field import Field
from feast.infra.offline_stores.file_source import FileSource

# customer entity.
customer = Entity(name="customer")

# train file source
train_source = FileSource(
    name="train_source",
    path="data/train.parquet",
    timestamp_field="ts",
    created_timestamp_column="created",
)

# test file source
test_source = FileSource(
    name="test_source",
    path="data/test.parquet",
    timestamp_field="ts",
    created_timestamp_column="created",
)

# validate file source
validate_source = FileSource(
    name="validate_source",
    path="data/validate.parquet",
    timestamp_field="ts",
    created_timestamp_column="created",
)


training_fv = FeatureView(
    name="training_fv",
    entities=[customer],
    # entities=[],
    ttl=timedelta(days=1),
    schema=[
        Field(name="customer_id", dtype=Int64),
        Field(name="distance_from_last_transaction", dtype=Float64),
        Field(name="ratio_to_median_purchase_price", dtype=Float64),
        Field(name="used_chip", dtype=Float64),
        Field(name="used_pin_number", dtype=Float64),
        Field(name="online_order", dtype=Float64),
        Field(name="fraud", dtype=Float64),
    ],
    online=True,
    source=train_source,
    tags={"team": "training"},
)


test_fv = FeatureView(
    name="test_fv",
    entities=[customer],
    # entities=[],
    ttl=timedelta(days=1),
    schema=[
        Field(name="customer_id", dtype=Int64),
        Field(name="distance_from_last_transaction", dtype=Float64),
        Field(name="ratio_to_median_purchase_price", dtype=Float64),
        Field(name="used_chip", dtype=Float64),
        Field(name="used_pin_number", dtype=Float64),
        Field(name="online_order", dtype=Float64),
        Field(name="fraud", dtype=Float64),
    ],
    online=True,
    source=test_source,
    tags={"team": "testing"},
)


validation_fv = FeatureView(
    name="validation_fv",
    entities=[customer],
    # entities=[],
    ttl=timedelta(days=1),
    schema=[
        Field(name="customer_id", dtype=Int64),
        Field(name="distance_from_last_transaction", dtype=Float64),
        Field(name="ratio_to_median_purchase_price", dtype=Float64),
        Field(name="used_chip", dtype=Float64),
        Field(name="used_pin_number", dtype=Float64),
        Field(name="online_order", dtype=Float64),
        Field(name="fraud", dtype=Float64),
    ],
    online=True,
    source=validate_source,
    tags={"team": "validation"},
)
