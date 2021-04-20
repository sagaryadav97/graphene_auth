from user.schema import Mutation
from user.quires import UserQuery
import graphene


class mutation(Mutation):
    pass

class query(UserQuery):
    pass

schema=graphene.Schema(query=query,mutation=mutation)
