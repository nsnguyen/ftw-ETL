import argh
import yaml
import traceback
import sys
import os
import importlib
import pdb
from typing import Optional, Tuple

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def load_parameters(path: str) -> dict:
  with open(path) as p:
    return yaml.safe_load(p)


def load_worker(worker):
  worker_module = importlib.import_module('etl.workers.{}'.format(worker))
  return worker_module.Extractor, worker_module.Transformer, worker_module.Loader


class EtlController:
  def __init__(self, worker: str):
    self.extractor_cls, self.transformer_cls, self.loader_cls = load_worker(worker)

  def process(self, source, parameters: dict) -> None:

    extractor = self.extractor_cls()
    transformer = self.transformer_cls()
    loader = self.loader_cls()

    # run E-T-L
    try:
      # begin extraction
      extractor.execute()

      # begin transformer
      transformer.execute()

      # beging loader

      loader.execute()

    except Exception as e:
      print(e)


def etl(manifest: str,
        print_traceback: Optional[bool] = False):
  """

  :param manifest: path to job that will be used in E-T-L
  :param env:
  :param service:
  :param print_traceback:
  :return:
  """

  manifest = load_parameters(manifest)

  source = manifest['source']
  worker = manifest['worker']
  parameters = manifest['parameters']

  try:
    controller = EtlController(worker)
    controller.process(source=source, parameters=parameters)
  except ImportError as e:
    print(e)




argh.dispatch_command(etl)
