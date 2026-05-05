import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity        
        self.refill_rate = refill_rate   
        self.tokens = capacity          
        self.last_refill_time = time.time()

    def allow_request(self):
        current_time = time.time()
        
        time_passed = current_time - self.last_refill_time
        refill_tokens = time_passed * self.refill_rate
        
        self.tokens = min(self.capacity, self.tokens + refill_tokens)
        self.last_refill_time = current_time
        
        if self.tokens >= 1:
            self.tokens -= 1
            return True  
        return False