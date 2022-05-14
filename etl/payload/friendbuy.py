class FriendBuyPayload:
    """
    This class is a ledger of work done in a single ETL job.
    """

    def __init__(self):
        # this is Kafka Extractor object
        self.kafka = None

        # worker version
        self.version = None

        # extraction source is where it will extract data from a kafka topic.
        self.extraction_source = None

        # this is group name for kafka message
        self.group_source = None

        # load destination is where it will load data to a kafka topic.
        self.load_destination = None

        # this is typically the raw data extracted from a source.
        self.extracted_data = None

        # this is where the transformed data is ready to write into final source.
        self.transformed_data = None

        # this is time (seconds) to wait after each cycle. It is intended to throttle each batch
        self.wait_after_completion = 0

        # parameters for each work
        self.parameters = {}

        # redlock locking mechanism
        self.lock = None
