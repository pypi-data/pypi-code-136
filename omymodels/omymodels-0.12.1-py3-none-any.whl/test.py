from omymodels import create_models


ddl = """
CREATE TABLE "merchants" (
  "id" int PRIMARY KEY,
  "merchant_name" varchar
);

CREATE TABLE "products" (
  "ID" int PRIMARY KEY,
  "MERC" int NOT NULL
);

ALTER TABLE "products" ADD FOREIGN KEY ("merchant_id") REFERENCES "merchants" ("id");
"""
result = create_models(ddl, models_type='pydantic', no_auto_snake_case=True)['code']
print(result)