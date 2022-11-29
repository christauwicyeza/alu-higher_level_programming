#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
from io import StringIO
from contextlib import redirect_stdout


class TestBase(unittest.TestCase):
    """Tests for Base"""

    def test_base_id(self):
        """no comments"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_base_id_increment(self):
        """no comments"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    """From Python to JSON"""

    def test_to_json_string(self):
        """no comments"""
        lst = [{'id': 12}]
        lst_str = Base.to_json_string(lst)
        self.assertTrue(lst_str, [{"id": 2}])
        self.assertTrue(lst_str, isinstance(lst_str, str))

    def test_none_to_json_string(self):
        """no comments"""
        lt = None
        lt_str = Base.to_json_string(lt)
        self.assertTrue(lt_str, "[]")
        self.assertTrue(lt_str, isinstance(lt_str, str))

    def test_empty_to_json_string(self):
        """no comments"""
        l = dict()
        l_str = Base.to_json_string(l)
        self.assertTrue(l_str, "[]")
        self.assertTrue(l_str, isinstance(l_str, str))

    """From JSON to Python"""

    def test_from_json_string(self):
        """no comments"""
        j_str = '[{ "id": 89 }]'
        j_list = Base.from_json_string(j_str)
        self.assertTrue(j_list, [{"id": 89}])
        self.assertTrue(j_list, isinstance(j_list, list))

    def test_none_from_json_string(self):
        """no comments"""
        js = None
        js_ls = Base.from_json_string(js)
        self.assertEqual(js_ls, [])
        self.assertTrue(isinstance(js_ls, list))

    def test_empty_from_json_string(self):
        """no comments"""
        j = ""
        j_ls = Base.from_json_string(j)
        self.assertEqual(j_ls, [])
        self.assertTrue(isinstance(j_ls, list))


class TestRectangle(unittest.TestCase):
    """test"""

    def test_rec(self):
        """test"""
        r1 = Rectangle(20, 30, 2, 3, 1)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r2.id, not None)

    def test_validation(self):
        """test"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area_str(self):
        """test"""
        r3 = Rectangle(3, 4, id=1)
        self.assertEqual(r3.area(), 12)
        self.assertEqual(str(r3), '[Rectangle] (1) 0/0 - 3/4')
        with self.assertRaises(ValueError):
            Rectangle(0, 2).area()
        with self.assertRaises(ValueError):
            Rectangle(1, 0).area()

    def test_display(self):
        """Test method: display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(4, 3).display()
            a = bufr.getvalue()
        self.assertEqual(a, '####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_create(self):
        """tests"""
        dic = {"width": 3, "height": 4}
        rect = Rectangle.create(**dic)
        self.assertEqual(rect.area(), 12)

    def test_to_dictionary(self):
        """tests"""
        r4 = Rectangle(3, 4, 2, 5, 1)
        self.assertEqual(r4.to_dictionary(),
                         {"id": 1, "width": 3, "height": 4, "x": 2, "y": 5})

    def test_update(self):
        """tests"""
        r = Rectangle(3, 4,)
        r.update(width=4, height=5, x=2, y=3, id=15)
        self.assertEqual(r.area(), 20)
        dic = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r.update(**dic)
        self.assertEqual(r.area(), 2)

    """Test rectangle - save to file"""

    def test_save_to_file(self):
        """Test"""
        r = Rectangle(10, 7, 2, 8, 99)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps([r.to_dictionary()]), file.read())

    def test_none_save_to_file(self):
        """Test"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_empty_save_to_file(self):
        """Tests"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[]', f.read())

    """Test rectangle - load from file"""

    def test_load_from_file(self):
        """Test load from file"""
        r = Rectangle(10, 11, 3, 4, 8)
        Rectangle.save_to_file([r])
        rec = Rectangle.load_from_file()
        self.assertEqual(len(rec), 1)
        for item in rec:
            self.assertEqual(str(item), '[Rectangle] (8) 3/4 - 10/11')


class TestSquare(unittest.TestCase):
    """tests"""
    def test_rec(self):
        """test"""
        r1 = Square(20, 2, 3, 1)
        r2 = Square(3, 4)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.size, 20)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.size, 3)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)
        self.assertTrue(r2.id, not None)

    def test_validation(self):
        """test"""
        with self.assertRaises(TypeError):
            Square(str(1), 2)
        with self.assertRaises(TypeError):
            Square(1, str(2))
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            Square(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            Square(1, 2, -3, 4)

    def test_area_str_display(self):
        """test"""
        r3 = Square(3, id=1)
        self.assertEqual(r3.area(), 9)
        self.assertEqual(str(r3), '[Square] (1) 0/0 - 3')
        with self.assertRaises(TypeError):
            Square(1, 2, "3", 4).display()

        with self.assertRaises(TypeError):
            Square(6, "7").display()
        r5 = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r5.__str__(1)
        with self.assertRaises(ValueError):
            Square(0).area()

    def test_create(self):
        """tests"""
        """returns an instance with all attributes already set"""
        dic = {"size": 3}
        rect = Square.create(**dic)
        self.assertEqual(rect.area(), 9)

    def test_to_dictionary(self):
        """tests"""
        r4 = Square(3, 2, 5, 1)
        self.assertEqual(r4.to_dictionary(),
                         {"id": 1, "size": 3, "x": 2, "y": 5})

    def test_update(self):
        """tests"""
        r = Square(3, 4,)
        r.update(size=6, x=2, y=3, id=15)
        self.assertEqual(r.area(), 36)
        dic = {'id': 89, 'size': 2, 'x': 3, 'y': 4}
        r.update(**dic)
        self.assertEqual(r.area(), 4)

    def test_save_to_file(self):
        """Test save to file"""
        r = Square(7, 2, 8, 99)
        Square.save_to_file([r])
        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps([r.to_dictionary()]), file.read())

    def test_none_save_to_file(self):
        """Test save None to file"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_empty_save_to_file(self):
        """Test save empty list to file"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_load_from_file(self):
        """Test load from file"""
        r = Square(10, 3, 4, 8)
        Square.save_to_file([r])
        rec = Square.load_from_file()
        self.assertEqual(len(rec), 1)
        for item in rec:
            self.assertEqual(str(item), '[Square] (8) 3/4 - 10')


if __name__ == "__main__":
    unittest.main()
