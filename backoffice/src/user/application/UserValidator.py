"""
 *
 * Libraries 
 *
"""

from src.user.domain   import UserRepository
from src.user.domain   import User
from src.shared.domain import UserEmail
from src.user.domain   import UserCode
from src.shared.domain import DomainException
from src.shared.domain import SUCCESSFUL_REQUEST
from src.shared.domain import SERVER_INTERNAL_ERROR
from src.shared.domain import EventBus
from src.user.domain   import UserFinder

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
    ) -> int:
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
        try:
            user = finder.findByEmail( email )
            user.validate( code )
            if repository.update( user ):
                eventBus.publish( user.pullEvents() )
                return SUCCESSFUL_REQUEST
            return SERVER_INTERNAL_ERROR
        except DomainException as exc:
            return exc.code()
