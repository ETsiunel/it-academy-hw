"""Conftest"""


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report Library"


# To run:
#   pytest test_library.py --log-cli-level=ERROR
#       --html=report.html --self-contained-html
#           - вывод уровня ERROR и выше в консоль,
#           - в html-отчете уровни по дефолту
#   pytest test_library.py --log-level=ERROR
#       --html=report.html --self-contained-html
#           - вывод уровня ERROR и выше в html-отчет
#           - в консоли лог не пишет
#   pytest test_library.py --log-cli-level=ERROR
#       --html=report.html --self-contained-html --log-level=ERROR
#           - вывод уровня ERROR и выше везде
