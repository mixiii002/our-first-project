
print('saloooommmmm!!!!')


'''
для того чтобы поделиться изменением:
git add . 
git commit -m "что-то"
git push

для того чтобы получить изменения с других:
git pull

для того чтобы клонировать актуальный проект:
git clone + ссылка самого проекта (https://github.com/mixiii002/our-first-project.git)
'''


# decorators


def dekorator(func):
    def luboy():
        print("dekorator birinchi")
        func()
        print("dekorator ikkinchi")

    return luboy

@dekorator
def salomlash():
    print("Assalomu alaykum")


salomlash()

