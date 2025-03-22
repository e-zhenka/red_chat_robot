import os
from typing import Dict, Union

import yaml
from pydantic import BaseModel, Field


class Config(BaseModel):
    model: str = Field(
        default="ivan",
        alias="llm_model",
        title="LLM model deployed in ollama container"
    )
    keep_alive: int = Field(
        default=60,
        title="The amount of time the model remains loaded into memory"
    )
    stream: bool = Field(
        default=True,
        title="Stream data transferring"
    )
    options: Dict[str, Union[bool, int, float, str]] = Field(
        default={"f16_kv": True, "num_batch": 256, "num_thread": 10},
        title="configuration parameters"
    )

    @classmethod
    def from_yaml(cls, path: str) -> "Config":
        data = cls()._load_yaml(path)
        return cls(**data)

    def _load_yaml(self, path: str) -> Dict[str, Union[str, bool, int, float]]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} does not exist")
        try:
            with open(path, 'r', encoding="utf-8") as f:
                data = yaml.safe_load(f)
            if data is None:
                raise ValueError(f"Failed to load YAML from {path}")
            return data
        except Exception as e:
            raise ValueError(f"Failed to parse YAML: {e}")
