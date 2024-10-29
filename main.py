import time
from collections import defaultdict, deque



class TokenBucketRateLimiter:

    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = defaultdict(lambda:capacity)
        self.last_refill = defaultdict(lambda: time.time())


    def allow_request(self, userId):
        now = time.time()
        time_passed = now - self.last_refill[userId]
        self.tokens[userId] = min(self.capacity, self.tokens[userId]+(time_passed*self.rate))
        self.last_refill[userId] = now

        if self.tokens[userId] >= 1:
            self.tokens[userId] -= 1
            return True
        return False



class FixedWindowRateLimiter:

    def __init__(self, window_size, capacity):
        self.window_size = window_size
        self.requests = defaultdict(int)
        self.capacity = capacity
        self.start_time = time.time()

    
    def allow_request(self, userId):
        now = time.time()
        if now - self.start_time > self.window_size:
            self.requests.clear()
            self.window_start = now
        
        if self.requests[userId] < self.capacity:
            self.requests[userId] += 1
            return True
        
        return False


class SlidingWindowLogRateLimiter:

    def __init__(self, window_size, max_request):
        self.window_size = window_size
        self.max_request = max_request
        self.requests = defaultdict(deque)

    
    def allow_request(self, userId):
        now = time.time()
        while self.requests[userId] and self.requests[userId][0] <= now - self.window_size:
            self.requests[userId].popleft()

        
        if len(self.requests[userId]) < self.max_request:
            self.requests[userId].append(now)
            return True

        return False


class SlidingWindowCounterRateLimiter:

    def __init__(self, capacity, window_size):
        self.capacity = capacity
        self.window_size = window_size
        self.requests = defaultdict(lambda: [0, time.time()])

    
    def allow_request(self, userId):
        now = time.time()
        count, timestamp = self.requests[userId]

        if now - timestamp >= self.window_size:
            self.requests[userId] = [1, now]
            return True
        

        if count < self.capacity:
            self.requests[userId][0] += 1
            return True
        return False




def main():

    #TokenBucketrateLimiter

    # token_bucket = TokenBucketRateLimiter(rate=1, capacity=5)
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True
    # time.sleep(1)
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True
    # print(token_bucket.allow_request("user1"))  # True

    # print("Fixed Window Rate Limiter")

    # #Fixed Window Rate Limit
    # fixed_window_bucket = FixedWindowRateLimiter(5, 5)
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))
    # time.sleep(5)
    # print(fixed_window_bucket.allow_request("user1"))
    # print(fixed_window_bucket.allow_request("user1"))


    # print("sliding Window Log Limiter")

    # #sliding window log
    # sliding_window_log = SlidingWindowLogRateLimiter(10, 5)
    # print(sliding_window_log.allow_request("user1"))
    # time.sleep(2)
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # time.sleep(12)
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))
    # print(sliding_window_log.allow_request("user1"))



    sliding_window_counter = SlidingWindowCounterRateLimiter(5, 30)

    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))
    print(sliding_window_counter.allow_request("user1"))




    






if __name__ == "__main__":
    main()


    
