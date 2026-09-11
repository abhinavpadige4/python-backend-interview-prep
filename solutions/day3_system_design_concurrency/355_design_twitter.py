"""
LeetCode #355: Design Twitter
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user 
and is able to see the 10 most recent tweets in the user's news feed.

Time Complexity: 
- postTweet: O(1)
- getNewsFeed: O(f * log f) where f is number of followees (due to heap merge)
- follow/unfollow: O(1)
Space Complexity: O(u + t) where u is users, t is tweets
"""

from typing import List
import heapq
from collections import defaultdict
import itertools

class Twitter:
    """
    Twitter implementation using:
    - Hash map for user tweets (user_id -> list of tweets)
    - Hash map for follow relationships (follower_id -> set of followee_ids)
    - Global timestamp counter for ordering tweets
    - Min-heap for merging k sorted lists (news feed)
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = itertools.count(step=-1)  # Negative for max-heap behavior
        self.tweets = defaultdict(list)  # user_id -> list of (timestamp, tweetId)
        self.followees = defaultdict(set)  # follower_id -> set of followee_ids
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        
        Args:
            userId: ID of user posting tweet
            tweetId: ID of the tweet
        """
        self.tweets[userId].append((next(self.timestamp), tweetId))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        
        Args:
            userId: ID of user whose news feed to retrieve
            
        Returns:
            List of up to 10 most recent tweet IDs
        """
        # Get users to fetch tweets from (user + followees)
        users = self.followees[userId].copy()
        users.add(userId)  # Include user's own tweets
        
        # Use min-heap to merge k sorted lists (tweets are in chronological order)
        # We'll store (-timestamp, tweetId, user_id, tweet_index) for max-heap behavior
        max_heap = []
        
        # Add most recent tweet from each user to heap
        for user_id in users:
            if self.tweets[user_id]:
                timestamp, tweet_id = self.tweets[user_id][-1]  # Most recent tweet
                heapq.heappush(max_heap, (timestamp, tweet_id, user_id, len(self.tweets[user_id]) - 1))
        
        result = []
        # Extract up to 10 most recent tweets
        while max_heap and len(result) < 10:
            timestamp, tweet_id, user_id, tweet_idx = heapq.heappop(max_heap)
            result.append(tweet_id)
            
            # Add next tweet from same user if available
            if tweet_idx > 0:
                next_timestamp, next_tweet_id = self.tweets[user_id][tweet_idx - 1]
                heapq.heappush(max_heap, (next_timestamp, next_tweet_id, user_id, tweet_idx - 1))
        
        return result
    
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        
        Args:
            followerId: ID of follower user
            followeeId: ID of followee user
        """
        if followerId != followeeId:  # Prevent self-following (optional based on requirements)
            self.followees[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        
        Args:
            followerId: ID of follower user
            followeeId: ID of followee user
        """
        self.followees[followerId].discard(followeeId)  # discard doesn't raise error if not present

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic Twitter functionality
    print("Test Case 1: Basic Twitter Operations")
    twitter = Twitter()
    
    # User 1 posts a tweet
    twitter.postTweet(1, 5)
    print(f"User 1 posts tweet 5")
    
    # User 1's news feed should return [5]
    feed1 = twitter.getNewsFeed(1)
    print(f"User 1's news feed: {feed1}")  # Expected: [5]
    print()
    
    # User 1 follows user 2
    twitter.follow(1, 2)
    print(f"User 1 follows user 2")
    
    # User 2 posts a tweet
    twitter.postTweet(2, 6)
    print(f"User 2 posts tweet 6")
    
    # User 1's news feed should return [6, 5] (6 is more recent)
    feed2 = twitter.getNewsFeed(1)
    print(f"User 1's news feed: {feed2}")  # Expected: [6, 5]
    print()
    
    # User 1 unfollows user 2
    twitter.unfollow(1, 2)
    print(f"User 1 unfollows user 2")
    
    # User 1's news feed should return [5] again
    feed3 = twitter.getNewsFeed(1)
    print(f"User 1's news feed: {feed3}")  # Expected: [5]
    print()
    
    # Test case 2: Multiple tweets and users
    print("Test Case 2: Multiple Users and Tweets")
    twitter2 = Twitter()
    
    # User 1 posts tweets 1, 2, 3
    twitter2.postTweet(1, 1)
    twitter2.postTweet(1, 2)
    twitter2.postTweet(1, 3)
    
    # User 2 posts tweets 4, 5
    twitter2.postTweet(2, 4)
    twitter2.postTweet(2, 5)
    
    # User 1 follows user 2
    twitter2.follow(1, 2)
    
    # User 1's news feed should show most recent 10 tweets
    feed4 = twitter2.getNewsFeed(1)
    print(f"User 1's news feed: {feed4}")  # Expected: [5, 4, 3, 2, 1] or similar order
    print()
    
    # Test case 3: Self-tweets included
    print("Test Case 3: Self-Tweets Included")
    twitter3 = Twitter()
    
    twitter3.postTweet(1, 10)
    twitter3.postTweet(1, 20)
    twitter3.follow(1, 2)
    twitter3.postTweet(2, 30)
    
    feed5 = twitter3.getNewsFeed(1)
    print(f"User 1's news feed: {feed5}")  # Should include user 1's own tweets