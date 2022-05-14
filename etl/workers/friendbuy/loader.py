import logging

from etl.common import BaseLoader


class FriendBuyLoader(BaseLoader):
    def __init__(self, payload: object):
        super().__init__(payload)
        # self.logger = logging.getLogger(__name__)

    def execute(self):
        print("begin_loader")
