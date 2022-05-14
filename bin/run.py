import argparse
import importlib
import os
import sys
import traceback
from typing import Optional, Tuple

import yaml

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")


def load_parameters(path: str) -> dict:
    with open(path) as p:
        return yaml.safe_load(p)


def load_worker(worker):
    worker_module = importlib.import_module("etl.workers.{}".format(worker))
    return worker_module.Extractor, worker_module.Transformer, worker_module.Loader


def load_payload(worker):
    payload_module = importlib.import_module("etl.payload.{}".format(worker))
    return payload_module


class EtlController:
    def __init__(self, worker: str):
        self.extractor_cls, self.transformer_cls, self.loader_cls = load_worker(worker)
        self.payload = load_payload(worker)

    def process(self, source, parameters: dict) -> None:
        extractor = self.extractor_cls(self.payload)
        transformer = self.transformer_cls(self.payload)
        loader = self.loader_cls(self.payload)

        try:
            # begin extraction
            extractor.execute()

            # begin transformer
            transformer.execute()

            # beging loader
            loader.execute()

        except Exception as e:
            print(e)


def run_etl(pipeline: str):
    """
    :param manifest: path to job that will be used in E-T-L

    """
    worker_manifest = f"manifests/service/{pipeline}.yaml"
    manifest = load_parameters(worker_manifest)

    source = manifest["source"]
    worker = manifest["worker"]
    parameters = manifest["parameters"]

    try:
        controller = EtlController(worker)
        controller.process(source=source, parameters=parameters)
    except ImportError as e:
        print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL batch job")
    parser.add_argument(
        "--pipeline",
        dest="pipeline",
        required=True,
        help="name of pipeline",
    )
    args = parser.parse_args()
    pipeline = args.pipeline
    run_etl(pipeline=pipeline)
