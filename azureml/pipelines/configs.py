from typing import Dict, List, Union

from dataclasses import dataclass, field


@dataclass
class AMLConfig:
    workspace_name: str = str()
    resource_group: str = str()
    subscription_id: str = str()


@dataclass
class PipelineConfig:
    base_experiment_name: str = str()
    tags: Dict[str, str] = field(default_factory=dict)
    default_compute_target: str = str()


@dataclass
class AOAIConfig:
    endpoint: str = str()
    model: str = str()
    compute_target: str = str()


@dataclass
class ZeroShotRunConfig:
    pipeline: PipelineConfig = field(default_factory=PipelineConfig)
    mmlu_dataset: str = str()
    mmlu_split: str = str()
    guidance_program: str = str()
    guidance_workers: int = 4
    max_errors: int = 5
    aoai_config: AOAIConfig = field(default_factory=AOAIConfig)


@dataclass
class FewShotConfig:
    pipeline: PipelineConfig = field(default_factory=PipelineConfig)
    mmlu_dataset: str = str()
    mmlu_split: str = str()
    fewshot_split: str = str()
    guidance_program: str = str()
    guidance_workers: int = 4
    max_errors: int = 5
    aoai_config: AOAIConfig = field(default_factory=AOAIConfig)


@dataclass
class EmbeddingConfig:
    pipeline: PipelineConfig = field(default_factory=PipelineConfig)
    mmlu_dataset: str = str()
    mmlu_split: str = str()
    source_key: str = str()
    destination_key: str = str()
    workers: int = 4
    max_errors: int = 2
    aoai_embedding_config: AOAIConfig = field(default_factory=AOAIConfig)
