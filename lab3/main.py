from task1_adapter import Logger, FileWriter, FileLoggerAdapter
from task2_decorator import Warrior, Mage, Sword, Shield
from task3_bridge import Circle, Square, VectorRender, RasterRender
from task4_proxy import SmartTextChecker, SmartTextReaderLocker
from task5_composite import LightElementNode, LightTextNode
from task6_flyweight import LightHTML

def main():
    # Тестування Адаптера
    logger = Logger()
    file_writer = FileWriter()
    file_logger = FileLoggerAdapter(file_writer)

    file_logger.Log("This is a log message.")
    file_logger.Error("This is an error message.")
    file_logger.Warn("This is a warning message.")

    # Тестування Декоратора
    warrior = Warrior("Warrior")
    mage = Mage("Mage")
    warrior_with_sword = Sword(warrior)
    mage_with_shield = Shield(mage)

    print(warrior_with_sword)
    print(mage_with_shield)

    # Тестування Мосту
    vector_render = VectorRender()
    raster_render = RasterRender()
    circle = Circle()
    square = Square()

    vector_render.render()
    circle.render()

    raster_render.render()
    square.render()

    # Тестування Проксі
    checker = SmartTextChecker()
    locker = SmartTextReaderLocker(r".*\.txt$")

    checker.read("example.txt")
    locker.read("example.pdf")

    # Тестування Компонувальника
    html = LightHTML()
    text = """The Project Gutenberg eBook of Romeo and Juliet

    This ebook is for the use of anyone anywhere in the United States and
    most other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this ebook or online
    at www.gutenberg.org. If you are not located in the United States,
    you will have to check the laws of the country where you are located
    before using this eBook.

    Title: Romeo and Juliet
    Author: William Shakespeare
    Release date: November 1, 1998 [eBook #1513]
                    Most recently updated: June 19, 2024

    Language: English

    Credits: the PG Shakespeare Team, a team of about twenty Project Gutenberg volunteers

    *** START OF THE PROJECT GUTENBERG EBOOK ROMEO AND JULIET ***

    THE TRAGEDY OF ROMEO AND JULIET
    by William Shakespeare

    Contents

    THE PROLOGUE.

    ACT I
    Scene I. A public place.
    Scene II. A Street.
    Scene III. Room in Capulet’s House.
    Scene IV. A Street.
    Scene V. A Hall in Capulet’s House.

    ACT II
    CHORUS.
    Scene I. An open place adjoining Capulet’s Garden.
    Scene II. Capulet’s Garden.
    Scene III. Friar Lawrence’s Cell.
    Scene IV. A Street.
    Scene V. Capulet’s Garden.
    Scene VI. Friar Lawrence’s Cell.

    ACT III
    Scene I. A public Place.
    Scene II. A Room in Capulet’s House.
    Scene III. Friar Lawrence’s cell.
    Scene IV. A Room in Capulet’s House.
    Scene V. An open Gallery to Juliet’s Chamber, overlooking the Garden.

    ACT IV
    Scene I. Friar Lawrence’s Cell.
    Scene II. Hall in Capulet’s House.
    Scene III. Juliet’s Chamber.
    Scene IV. Hall in Capulet’s House.
    Scene V. Juliet’s Chamber; Juliet on the bed.

    ACT V
    Scene I. Mantua. A Street.
    Scene II. Friar Lawrence’s Cell.
    Scene III. A churchyard; in it a Monument belonging to the Capulets.

    Dramatis Personae

    ESCALUS, Prince of Verona.
    MERCUTIO, kinsman to the Prince, and friend to Romeo.
    PARIS, a young Nobleman, kinsman to the Prince.
    Page to Paris.

    MONTAGUE, head of a Veronese family at feud with the Capulets.
    LADY MONTAGUE, wife to Montague.
    ROMEO, son to Montague.
    BENVOLIO, nephew to Montague, and friend to Romeo.
    ABRAM, servant to Montague.
    BALTHASAR, servant to Romeo.

    CAPULET, head of a Veronese family at feud with the Montagues.
    LADY CAPULET, wife to Capulet.
    JULIET, daughter to Capulet.
    TYBALT, nephew to Lady Capulet.
    CAPULET’S COUSIN, an old man.
    NURSE to Juliet.
    PETER, servant to Juliet’s Nurse.
    SAMPSON, servant to Capulet.
    GREGORY, servant to Capulet.
    Servants.

    FRIAR LAWRENCE, a Franciscan.
    FRIAR JOHN, of the same Order.
    An Apothecary.
    CHORUS.
    Three Musicians.
    An Officer.
    Citizens of Verona; several Men and Women, relations to both houses;
    Maskers, Guards, Watchmen and Attendants."""

    for line in text.split("\n"):
        html.add_line(line)

    html.render()

    # Тестування Легковаговика
    light_html = LightHTML()
    for line in text.split("\n"):
        light_html.add_line(line)
    light_html.render()

if __name__ == "__main__":
    main()
