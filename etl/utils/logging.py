import sys


def stdout_log(text: str):
  """
  SumoLogic currently logs everything that's stdout
  :param text:
  :return:
  """
  sys.stdout.write(text)


def stderr_log(text: str):
  """
  SumoLogic currently logs everything that's stdout
  :param text:
  :return:
  """
  sys.stderr.write(text)
