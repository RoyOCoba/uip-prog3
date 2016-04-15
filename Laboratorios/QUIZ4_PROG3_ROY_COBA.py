import unittest

class registro:
    try:
        def registro(self,usuario,edad):
            usuario=input("escribe tu nombre")
            edad=input("escribe tu edad")
            return {"usuario:":usuario,"apellido":usuario+"coba","edad:":edad}
    except Exception:
        print("ERROR")

class NotificationsTestCase(unittest.TestCase):
    try:

        def test_user_repository(self):
            users=registro()
            user=users.registro("roy","26")

            self.assertEquals("roycoba",user['apellido'])
    except Exception:
        print("ERROR")

if __name__ == '__main__':
        unittest.main()