export default class Client {
    public email: string;
    public phone: string;

    create(email:string , phone:string): void {
        this.email = email;
        this.phone = phone;
    }
    read(): void {}
    update(): void {}
    delete(): void {}
}