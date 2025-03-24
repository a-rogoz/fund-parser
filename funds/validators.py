import magic

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class FileValidator:
    """
    Contains validation methods for uploaded files.
    """

    @staticmethod
    def validate_file_mime_type(file, allowed_mime_types=None):
        """
        Validate if the file type is allowed.
        """
        if allowed_mime_types is None:
            allowed_mime_types = ["text/csv", "text/plain"]
        
        file.seek(0)
        file_mime_type = magic.from_buffer(file.read(1024), mime=True)
        if file_mime_type not in allowed_mime_types:
            raise ValidationError(f"Unsupported mime type: {file_mime_type}.")

    @staticmethod
    def validate_file_size(file, max_size=16):
        """
        Validate file size (max_size in MB).
        """

        # Convert MB to bytes
        limit_size = max_size * 1024 * 1024
        if file.size > limit_size:
            raise ValidationError(f"File too large. Maximum allowed size is {max_size} MB.")


validate_file_extension = FileExtensionValidator(allowed_extensions=["csv"])
