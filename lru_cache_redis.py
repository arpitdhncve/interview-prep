import redis

# Connect to Redis local instance
client = redis.Redis(host='localhost', port=6379, db=0)

# Set maximum memory and LRU policy
client.config_set('maxmemory', '2mb')  # sets max memory to 1 MB
client.config_set('maxmemory-policy', 'allkeys-lru')

# Function to set a key in the cache
def set_key(key, value, timeout=300):
    """
    Set a key-value pair in Redis with an expiry.
    :param key: The key under which the item should be stored.
    :param value: The value to be stored.
    :param timeout: Time in seconds until the key expires.
    """
    client.set(key, value, ex=timeout)

# Function to get a key from the cache
def get_key(key):
    """
    Get a value from the cache.
    :param key: The key to retrieve.
    :return: The value or None if the key does not exist.
    """
    return client.get(key)

# Example usage
set_key('test', 'hello')
print(get_key('test'))  # Output will be b'hello'




# Connect to Redis local instance
client = redis.Redis(host='localhost', port=6379, db=0)

# Function to add elements to a set
def add_to_set(key, *values):
    """
    Add one or more values to a set stored at 'key'.
    :param key: The key of the set.
    :param values: Elements to add to the set.
    """
    client.sadd(key, *values)

# Function to get all elements from a set
def get_all_from_set(key):
    """
    Retrieve all elements from the set stored at 'key'.
    :param key: The key of the set.
    :return: A set of elements or an empty set if key does not exist.
    """
    return client.smembers(key)

# Function to check membership in a set
def is_member(key, value):
    """
    Check if 'value' is a member of the set stored at 'key'.
    :param key: The key of the set.
    :param value: The value to check for membership.
    :return: True if 'value' is a member of the set, False otherwise.
    """
    return client.sismember(key, value)

# Example usage
add_to_set('fruits', 'apple', 'banana', 'orange')
print(get_all_from_set('fruits'))  # Outputs set of b'apple', b'banana', b'orange'
print(is_member('fruits', 'apple'))  # Outputs True
print(is_member('fruits', 'cherry'))  # Outputs False
