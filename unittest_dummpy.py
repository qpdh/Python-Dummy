import sys
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # separator 가 string이 아닐 때
        with self.assertRaises(TypeError):
            s.split(2)


"""
테스트 코드 구조 잡기
"""


class Widget:
    def __init__(self, widget_name: str):
        self.widget_name = widget_name
        self.width = 50
        self.height = 50

    def size(self):
        return self.width, self.height

    def resize(self, width: int, height: int):
        self.width = width
        self.height = height

    def dispose(self):
        pass


class WidgetTestCase(unittest.TestCase):
    # 사전 설정 코드
    def setUp(self):
        print('테스트 케이스 시작')
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

    def test_widget_resize(self):
        self.widget.resize(100, 150)
        self.assertEqual(self.widget.size(), (100, 150),
                         'wrong size after resize')

    # 사후 설정 코드
    def tearDown(self):
        print('테스트 케이스 종료')
        self.widget.dispose()


"""
사용자 설정 테스트 묶음 만들기
"""


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


"""
테스트 스킵하기
"""


def external_resource_available():
    return True


class MyTestCase(unittest.TestCase):
    # 무조건 스킵하기
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    # 조건을 만족하면 스킵하기
    @unittest.skipIf(1 < 4, "not supported in this library version")
    def test_format(self):
        pass

    # 조건을 만족하지 않으면 스킵하기
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass

    # 테스트 메소드 내에서 스킵하기
    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")

# 클래스 단위로 스킵하기


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

# 실패가 예상된다면 -> 테스트 케이스를 만들었으나, 버그|미완성 등으로 동작하지 않는 상태


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(0, 0, "broken")


"""
부분 테스트를 사용하여 테스트 반복 구별 짓기
"""


class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        [0,5] 반복하면서 짝수 체크하기
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # runner = unittest.TextTestRunner()
    # runner.run(suite())
