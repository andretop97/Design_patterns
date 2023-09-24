import Client from "./Client";
import Notify from "./Notify";


const client = new Client()
const notify = new Notify()

client.create("andre@batata.com", "999999999");

notify.emailNotification(client.email, "Hello World");
notify.smsNotification(client.phone, "Hello World");