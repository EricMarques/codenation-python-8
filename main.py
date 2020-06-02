import jwt

secret = 'acelera'
data = {'language': 'Python'}


def create_token(data, secret):
    encoded = jwt.encode(data, secret, algorithm='HS256')    
    return encoded

def verify_signature(token):
    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.DecodeError:
        return {'error': 2}
    else:
        return token

new_token = create_token(data,secret)
verify_signature(new_token)
