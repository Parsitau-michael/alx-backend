import { createQueue } from "kue";

const queue = createQueue();

const job_data = {
  phoneNumber: "+2547 97 836 891",
  message: "You Gut it G! Keep pushing",
}

const job = queue.create("push_notification_code", job_data).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on("complete",() => console.log("Notification job completed"));
job.on("failed", () => console.log("Notification job failed"));
