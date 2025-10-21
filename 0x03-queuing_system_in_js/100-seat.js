import { createClient } from "redis";
import { createQueue } from "kue";
import express from "express";
import { promisify } from "util";

const client = createClient();
const queue = createQueue();

client.on('error', (err) => {
  console.log(`Failed to connect to redis: ${err}`);
});

const setFunc = promisify(client.set).bind(client);
const getFunc = promisify(client.get).bind(client);

function reserveSeat(number) {
  return setFunc('available_seats', number);
}

function getCurrentAvailableSeats() {
  return getFunc('available_seats');
}

let reservationEnabled = true;

const app = express();
const port = 1245;

(async () => {
  await reserveSeat(50);
})();

app.get('/available_seats', async(req, res) => {
  const available = await getCurrentAvailableSeats();
  return res.json({"numberOfAvailableSeats": available});
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ "status": "Reservation are blocked" });
  }

  const job = queue.create('reserve_seat', 1);

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  
  job.on('failed', (error) => {
    console.log(`Seat reservation job ${job.id} failed: ${error}`);
  });

 job.save((err) => {
   if (err) {
     return res.json({"status": "Reservation failed"});
   }
   return res.json({"status": "Reservation in process"});
 });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const available = parseInt(await getCurrentAvailableSeats());

    if (available <= 0) {
      return done(new Error('Not enough seats available'));
    }

    const newSeatCount = available - 1;
    await reserveSeat(newSeatCount);

    if (newSeatCount === 0) {
      reservationEnabled = false;
    }
    
    done();
  });
  res.json({"status": "Queue processing"})
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
