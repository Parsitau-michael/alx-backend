import redis from 'redis';

const redisPublisher = redis.createClient();

redisPublisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisPublisher.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

function publishMessage(message, time) {
  setTimeout(() => {
    redisPublisher.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
