class ResourceAlreadyExistsException(Exception):
    pass

class InvalidCredentialsException(Exception):
    pass

class IncompleteProfileException(Exception):
    pass

class AccountBlockedException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass