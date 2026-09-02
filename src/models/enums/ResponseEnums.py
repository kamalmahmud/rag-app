from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATE_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceede"
    FILE_UPLOAD_SUCCESS = "file_uploaded_success"
    FILE_UPLOAD_FAILED = "file_uploaded_failed"
    PROCESSING_FAILED = "processing_failed"
    PROCESSING_SUCCESS = "processing_success"