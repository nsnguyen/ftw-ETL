import traceback


def stack_trace(args):
  return ''.join(traceback.format_exception(*args))
