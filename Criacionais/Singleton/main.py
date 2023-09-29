from Singleton import Singleton
from LazySingleton import LazySingleton
from SingletonMonostate import Borg, SingletonMonostate


def main():
    singleton = Singleton()
    print(f'Object created {singleton}')
    singleton2 = Singleton()
    print(f'Object created {singleton2}')

    lazySingleton = LazySingleton()
    print(f'Object Created, {LazySingleton.getInstance()}')
    lazySingleton2 = LazySingleton()

    singletonMonostate = SingletonMonostate()
    singletonMonostate2 = SingletonMonostate()

    singletonMonostate2.x = 4

    print(f'Borg object singletonMonostate : {singletonMonostate}')
    print(f'Borg object singletonMonostate2 : {singletonMonostate2}')

    print(
        f'Borg object singletonMonostate State: {singletonMonostate.__dict__}')
    print(
        f'Borg object singletonMonostate2 State: {singletonMonostate2.__dict__}')

    borg = Borg()
    borg2 = Borg()

    borg2.x = 4

    print(f'Borg object borg : {borg}')
    print(f'Borg object borg2 : {borg2}')

    print(
        f'Borg object borg State: {borg.__dict__}')
    print(
        f'Borg object borg2 State: {borg2.__dict__}')


if __name__ == "__main__":
    main()
