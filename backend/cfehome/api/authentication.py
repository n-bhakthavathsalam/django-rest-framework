from rest_framework.authentication import TokenAuthentication as BasicTokenAuth


class TokenAuthentication(BasicTokenAuth):
    keyword = 'Token'