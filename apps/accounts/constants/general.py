USERNAME_MAX_LENGTH = 30
EMAIL_TO_USERNAME_HASH_LENGTH = USERNAME_MAX_LENGTH

EMAIL_ACTIVATION_KEY_EXPIRATION_HOURS = 48
EMAIL_ACTIVATION_KEY_REUSE_THRESHOLD_HOURS = EMAIL_ACTIVATION_KEY_EXPIRATION_HOURS - 1

SOCIAL_AUTH_PROVIDER_FACEBOOK = 'facebook'
SOCIAL_AUTH_PROVIDER_LINKEDIN = 'linkedin'
SOCIAL_AUTH_PROVIDER_TWITTER = 'twitter'

# ordered lists of social auths
SOCIAL_AUTHS = [
    { 'key': SOCIAL_AUTH_PROVIDER_FACEBOOK, 'name': 'Facebook' },
    { 'key': SOCIAL_AUTH_PROVIDER_TWITTER, 'name': 'Twitter' }
]

UID_XOR = 314159265