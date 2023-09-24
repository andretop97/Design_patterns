export default class Notify{

    emailNotification(email: string, message: string): boolean{
        console.log(`Sending email to ${email} with message: ${message}`);
        return true;   
    }

    smsNotification(phone: string, message: string): boolean{
        console.log(`Sending sms to ${phone} with message: ${message}`);
        return true;   
    }
}