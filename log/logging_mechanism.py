import logging

# AWS S3 Logging configuration
AWS_s3_logger = logging.getLogger("AWS-S3-Logger")
AWS_s3_logger_handler = logging.StreamHandler()
AWS_s3_logger_handler.setLevel(logging.INFO)
AWS_s3_logger_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
AWS_s3_logger_handler.setFormatter(AWS_s3_logger_formatter)
AWS_s3_logger.addHandler(AWS_s3_logger_handler)

