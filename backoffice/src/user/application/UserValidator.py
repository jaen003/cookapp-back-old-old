"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRepository
from src.user.domain   import User
from src.shared.domain import UserEmail
from src.user.domain   import UserCode
from src.shared.domain import EventBus
from src.user.domain   import UserFinder
from src.shared.domain import ServerInternalErrorException
from src.user.domain   import UserNotFoundException

"""
 *
 * Classes 
 *
"""

class UserValidator:

    """
     *
     * Parameters 
     *
    """

    __repository         : UserRepository
    __volatileRepository : UserRepository
    __eventBus           : EventBus

    """
     *
     * Methods 
     *
    """

    def __init__( 
        self, 
        repository         : UserRepository,
        volatileRepository : UserRepository,
        eventBus           : EventBus, 
    ) -> None:
        self.__repository         = repository
        self.__volatileRepository = volatileRepository
        self.__eventBus           = eventBus
    
    def validate( 
        self,
        email : UserEmail,
        code  : UserCode,
    ) -> None:
        # Variables
        repository         : UserRepository
        user               : User
        eventBus           : EventBus
        volatileRepository : UserRepository
        finder             : UserFinder
        # Code
        eventBus           = self.__eventBus
        repository         = self.__repository
        volatileRepository = self.__volatileRepository
        finder             = UserFinder( volatileRepository )
        user               = finder.findByEmail( email )
        if user is None:
            raise UserNotFoundException( email )
        user.validate( code )
        if not repository.update( user ):
            raise ServerInternalErrorException()
        eventBus.publish( user.pullEvents() )
