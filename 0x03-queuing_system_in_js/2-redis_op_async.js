import redis from 'redis';
import { promisify } from 'util';

const redisClient = redis.createClient();

const getAsync = promisify(redisClient.get).bind(redisClient);

redisClient.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
})

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
})

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const getReply = await getAsync(schoolName);
    console.log(getReply);
  } catch(err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
