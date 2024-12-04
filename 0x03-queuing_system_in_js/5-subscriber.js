import redis from 'redis';

const redisSubscriber = redis.createClient();

redisSubscriber.on('connect', () => {
  console.log('Redis client connected to the server');
})

redisSubscriber.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
})

redisSubscriber.subscribe('holberton school channel');

redisSubscriber.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    if (message === 'KILL_SERVER') {
      redisSubscriber.quit();
    } else {
      console.log(message);
    }
  }
})
