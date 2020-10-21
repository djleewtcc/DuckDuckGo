import pytest
from duckduckgo.presidents_query import query_presidents


presidents_list = ['Hoover', 'Lincoln', 'Ford', 'Reagan', 'Grant', 'Bush', 'Clinton', 'Buchanan', 'Roosevelt',
                   'Jackson', 'Adams', 'Truman', 'Obama', 'McKinley', 'Carter', 'Buren', 'Harrison', 'Pierce',
                   'Johnson', 'Trump', 'Harding', 'Arthur', 'Tyler', 'Garfield', 'Taylor', 'Jefferson', 'Fillmore',
                   'Wilson', 'Kennedy', 'Hayes', 'Madison', 'Cleveland', 'Monroe', 'Coolidge', 'Washington', 'Nixon',
                   'Eisenhower', 'Taft', 'Polk']


def test_ddg0():
    for name in presidents_list:
        assert name in query_presidents()
